# interact.py
import torch
from TTS.api import TTS
import random  # Import random for selecting a technical word

# Check if a CUDA-capable device is available and use it if possible
device = "cuda" if torch.cuda.is_available() else "cpu"

# Sample dataset of technical words
technical_words = [
    "Linear Regression",
    "Neural Networks",
    "Support Vector Machines",
    "Random Forest",
    "Gradient Descent",
    "Convolutional Neural Networks",
    "Natural Language Processing",
    "Data Mining",
    "Artificial Intelligence"
]


def extract_technical_word():
    """Function to randomly select a technical word from the dataset."""
    return random.choice(technical_words)


def generate_audio(text="What is Linear Regression, and how is it used in technology"):
    # Extract a technical word from the dataset
    tech_word = extract_technical_word()
    # Generate the audio using the TTS API
    tts = TTS(model_name='tts_models/en/ljspeech/fast_pitch').to(device)

    # Replace the term "Linear Regression" with the randomly selected technical word
    updated_text = text.replace("Linear Regression", tech_word)

    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Generate the audio file
    file_path = f"{output_dir}/output.wav"
    tts.tts_to_file(text=updated_text, file_path=file_path)

    return file_path


def generate_audio_english():
    return None
