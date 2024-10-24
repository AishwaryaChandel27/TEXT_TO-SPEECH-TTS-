import torch
from TTS.api import TTS
import gradio as gr
import random  # Import random for selecting a technical word

# Check if a CUDA-capable device is available and use it if possible
device = "cuda" if torch.cuda.is_available() else "cpu"

# Sample dataset of technical words in Hindi
technical_words_hindi = [
    "रेखीय प्रतिगमन",  # Linear Regression
    "न्यूरल नेटवर्क",  # Neural Networks
    "समर्थन वेक्टर मशीन",  # Support Vector Machines
    "रैंडम फॉरेस्ट",  # Random Forest
    "ग्रेडियंट अवरोहण",  # Gradient Descent
    "संविधानिक न्यूरल नेटवर्क",  # Convolutional Neural Networks
    "प्राकृतिक भाषा प्रसंस्करण",  # Natural Language Processing
    "डेटा खनन",  # Data Mining
    "कृत्रिम बुद्धिमत्ता"  # Artificial Intelligence
]


def extract_technical_word():
    """Function to randomly select a technical word from the Hindi dataset."""
    return random.choice(technical_words_hindi)


def generate_audio(text="रेखीय प्रतिगमन क्या है, और इसका प्रौद्योगिकी में कैसे उपयोग किया जाता है"):
    # Extract a technical word from the dataset
    tech_word = extract_technical_word()

    # Generate the audio using the TTS API with a Hindi model
    tts = TTS(model_name='tts_models/hi/hi_tts').to(device)  # Use a Hindi TTS model
    # Replace a sample word in the input text with a randomly selected technical word
    updated_text = text.replace("रेखीय प्रतिगमन", tech_word)

    # Create the output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Generate the audio file
    file_path = f"{output_dir}/output.wav"
    tts.tts_to_file(text=updated_text, file_path=file_path)

    return file_path


# Create a Gradio interface
demo = gr.Interface(
    fn=generate_audio,
    inputs=[gr.Textbox(label="Text (in Hindi)", placeholder="Type your text here...")],
    outputs=[gr.Audio(label="Generated Audio")]
)

# Launch the Gradio interface
if __name__ == "__main__":
    demo.launch()


def generate_audio_hindi():
    return None
