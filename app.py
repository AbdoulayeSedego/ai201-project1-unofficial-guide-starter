import gradio as gr
from generate import ask


def handle_query(question: str):
    if not question.strip():
        return "Please enter a question.", ""

    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources


with gr.Blocks(title="John Jay Unofficial Guide") as demo:
    gr.Markdown("# John Jay College — Unofficial Student Guide")
    gr.Markdown(
        "Ask anything about student life, clubs, career fairs, "
        "graduation rates, research opportunities, or on-campus jobs."
    )

    with gr.Row():
        inp = gr.Textbox(
            label="Your question",
            placeholder="e.g. What clubs can I join at John Jay?",
            lines=2,
        )

    btn = gr.Button("Ask", variant="primary")

    with gr.Row():
        answer  = gr.Textbox(label="Answer", lines=10)
        sources = gr.Textbox(label="Retrieved from", lines=10)

    btn.click(handle_query, inputs=inp, outputs=[answer, sources])
    inp.submit(handle_query, inputs=inp, outputs=[answer, sources])

if __name__ == "__main__":
    demo.launch()
