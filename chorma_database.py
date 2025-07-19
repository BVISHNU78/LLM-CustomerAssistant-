import chromadb
from chromadb.config import Settings
import os
from dotenv import load_dotenv
load_dotenv()

def get_chroma_client():
    """
    Initialize and return a ChromaDB client with the specified settings.
    """
    chroma_host = os.getenv("CHROMA_HOST", "localhost")
    chroma_port = os.getenv("CHROMA_PORT", "8000")
    
    settings = Settings(
        chroma_host=chroma_host,
        chroma_port=chroma_port,
        persist_directory=os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")
    )
    
    return chormadb.Client(settings)