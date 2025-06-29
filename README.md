# 🤖 Smart Assistant for Research Summarization

An AI-powered assistant that transforms lengthy research papers into digestible summaries, enables contextual Q&A, generates logic-based questions, and evaluates answers with justifications — all through a simple web interface.

## 🚀 Features

- 📄 **Document Upload**: Supports PDF and TXT files for research input.
- ✂️ **Auto Summarization**: Generates structured, concise summaries.
- 💬 **Contextual Q&A**: Asks and answers questions using document context.
- 🧠 **AI-Generated Questions**: Creates logical, concept-based questions.
- ✅ **Answer Evaluation**: Grades responses and gives AI-based feedback.
- 🌐 **Web Interface**: Clean frontend with document preview & interaction.

## 🛠️ Tech Stack

### Backend:
- Python (FastAPI / Flask)
- LangChain + LLM (OpenAI/GPT)
- PyPDF2 / PDFMiner / unstructured
- SQLite / PostgreSQL (optional)

### Frontend:
- React / Next.js
- Tailwind CSS + ShadCN UI
- Framer Motion / AOS (animations)

## 📁 Folder Structure

smart_assistant_project/
├── app/
│ ├── main.py # FastAPI backend entrypoint
│ ├── logic.py # AI logic: summary, Q&A, evaluation
│ └── utils/ # PDF/TXT parsers, embeddings
├── frontend/
│ ├── public/ # Static files
│ ├── src/ # React components, API calls
│ └── App.tsx # Main UI logic
├── requirements.txt
└── README.md 


## 📦 Installation

```bash
# Backend
cd smart_assistant_project
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
