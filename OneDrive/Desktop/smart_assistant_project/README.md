# Smart Assistant for Research Summarization

## Overview
An AI assistant that processes PDF/TXT documents to:
- Summarize within 150 words
- Answer user questions with context
- Generate logic-based questions
- Evaluate user answers with justification

## Tech Stack
- Frontend: Gradio
- Backend: FastAPI
- LLM: OpenAI GPT-4
- Embeddings: OpenAI text-embedding-ada-002
- Vector Store: FAISS

## Setup
```bash
git clone <repo-url>
cd smart_assistant_project
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
