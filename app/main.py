from fastapi import FastAPI, UploadFile, File

from app.qa import generate_answer
from app.text_utils import read_txt, read_pdf, chunk_text
from app.vector_store import store_chunks
from app.vector_store import semantic_search

app = FastAPI(title="Document Vector API")

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    if file.filename.endswith(".txt"):
        text = read_txt(content)
    elif file.filename.endswith(".pdf"):
        text = read_pdf(content)
    else:
        return {"error": "Unsupported file type"}

    chunks = chunk_text(text)
    store_chunks(chunks)

    return {
        "filename": file.filename,
        "chunks_stored": len(chunks)
    }

@app.post("/query")
def query_document(question: str):
    retrieved_chunks = semantic_search(question)
    answer = generate_answer(question, retrieved_chunks)

    return {
        "question": question,
        "answer": answer,
        "sources": retrieved_chunks
    }
