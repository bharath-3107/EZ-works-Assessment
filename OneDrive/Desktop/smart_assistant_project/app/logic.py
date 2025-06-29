import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document 
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI


doc_chunks = []
retriever = None
llm = ChatOpenAI(temperature=0)

def process_document(file_path):
    global retriever
    text = ""
    if file_path.endswith(".pdf"):
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    else:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([text])
    doc_chunks.extend(chunks)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(chunks, embeddings)
    retriever = db.as_retriever()

    summary_prompt = f"Summarize the following in under 150 words:\n{text[:3000]}"
    return llm.predict(summary_prompt)

def answer_question(q):
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
    result = chain({"query": q})
    return {"answer": result['result']}

def generate_questions():
    prompt = f"Generate three comprehension or logic-based questions from the following:\n{doc_chunks[0].page_content}"
    return llm.predict(prompt)

def evaluate_answer(question, user_answer):
    prompt = f"Q: {question}\nUser's Answer: {user_answer}\nEvaluate the answer and justify using document content:"
    return llm.predict(prompt)
