import os, traceback
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

load_dotenv()

embedding_model_name = "BAAI/bge-base-en-v1.5"
ollama_model = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
pdf_path = os.getenv("PDF_PATH", "D:/coding/pi data/Boulouio_data.pdf")
chroma_db_path = os.getenv("CHROMA_DB_PATH", "./chroma_store")
chroma_collection_name = os.getenv("CHROMA_COLLECTION_NAME", "kb")
urls = os.getenv("URLS", "https://boulou.io/about,https://boulou.io/faq").split(",")

embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)

loader = PyPDFLoader(pdf_path)
documents = loader.load()

url_loader = WebBaseLoader(urls)
url_docs = url_loader.load()

all_docs = documents + url_docs
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(all_docs)

vectorstore = Chroma.from_documents(
    texts,
    embedding=embedding_model,
    persist_directory=chroma_db_path,
    collection_name=chroma_collection_name
)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
llm = Ollama(model=ollama_model)
retriever = vectorstore.as_retriever()

qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory
)

def run(query: str) -> str:
    try:
        response = qa.invoke({"question": query})
        return response["answer"]
    except Exception as e:
        traceback.print_exc()
        return f"Error: {str(e)}"

if __name__ == "__main__":
    while True:
        q = input("Ask a question (or type 'exit'): ").strip()
        if q.lower() in ("exit", "quit"):
            break
        print("Answer:", run(q))
