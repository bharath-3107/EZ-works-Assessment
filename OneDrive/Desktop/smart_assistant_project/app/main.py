from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.logic import process_document, answer_question, generate_questions, evaluate_answer
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

UPLOAD_DIR = "sample_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    summary = process_document(file_path)
    return {"filename": file.filename, "summary": summary}

@app.get("/ask/")
async def ask(q: str):
    return answer_question(q)

@app.get("/challenge/")
async def challenge():
    return {"questions": generate_questions()}

@app.post("/evaluate/")
async def evaluate(data: dict):
    feedback = evaluate_answer(data["question"], data["user_answer"])
    return {"feedback": feedback}
