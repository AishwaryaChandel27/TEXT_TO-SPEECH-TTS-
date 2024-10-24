import gradio as gr
from fine_tune_regional import generate_audio_hindi  # Ensure this function exists
from fine_tune_english import generate_audio_english  # Ensure this function exists

def launch_interface():
    def generate_audio(selected_model, text):
        if selected_model == "English":
            return generate_audio_english(text)
        elif selected_model == "Hindi":
            return generate_audio_hindi(text)

    demo = gr.Interface(
        fn=generate_audio,
        inputs=[
            gr.Radio(choices=["English", "Hindi"], label="Select Language"),
            gr.Textbox(label="Input Text", placeholder="Type your text here...")
        ],
        outputs=[gr.Audio(label="Generated Audio")]
    )
    demo.launch()

if __name__ == "__main__":
    launch_interface()
