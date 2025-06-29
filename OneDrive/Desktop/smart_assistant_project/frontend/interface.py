import gradio as gr
import requests

backend_url = "http://localhost:8000"

def upload_doc(file):
    files = {"file": file}
    response = requests.post(f"{backend_url}/upload/", files=files)
    return response.json()["summary"]

def ask_question(question):
    response = requests.get(f"{backend_url}/ask/", params={"q": question})
    return response.json()["answer"]

def start_challenge():
    response = requests.get(f"{backend_url}/challenge/")
    return response.json()["questions"]

def evaluate_answer(question, user_answer):
    response = requests.post(f"{backend_url}/evaluate/", json={"question": question, "user_answer": user_answer})
    return response.json()["feedback"]

with gr.Blocks() as demo:
    gr.Markdown("## 📄 Smart Research Assistant")
    
    with gr.Tab("Upload Document"):
        file_input = gr.File()
        summary_output = gr.Textbox(label="150-Word Summary")
        file_input.change(fn=upload_doc, inputs=file_input, outputs=summary_output)
    
    with gr.Tab("Ask Anything"):
        question = gr.Textbox(label="Ask a Question")
        answer = gr.Textbox(label="Answer")
        question.submit(fn=ask_question, inputs=question, outputs=answer)

    with gr.Tab("Challenge Me"):
        q_list = gr.Textbox(label="Generated Questions")
        get_q_btn = gr.Button("Start Challenge")
        get_q_btn.click(fn=start_challenge, outputs=q_list)

        user_q = gr.Textbox(label="Enter Question")
        user_a = gr.Textbox(label="Your Answer")
        feedback = gr.Textbox(label="Feedback")
        submit_btn = gr.Button("Submit Answer")
        submit_btn.click(fn=evaluate_answer, inputs=[user_q, user_a], outputs=feedback)

demo.launch(server_name="0.0.0.0", server_port=7860, share=True)


