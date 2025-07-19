import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
import main

load_dotenv()
app = FastAPI()

class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(question: Question):
    try:
        answer = main.run(question.query)
        return {"question": question.query, "answer": answer}
    except Exception as e:
        return {"error": str(e), "answer": "Something went wrong."}

@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>BoulouGPT API</title></head>
    <body>
        <h1>Welcome to BoulouGPT API</h1>
        <p>POST to /ask with JSON {"query": "your question"} to get an answer.</p>
    </body>
    </html>
    """
