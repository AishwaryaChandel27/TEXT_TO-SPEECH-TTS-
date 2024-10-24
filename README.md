# Coqui TTS Fine-Tuning App

This is a Gradio application that allows users to generate speech from fine-tuned Text-to-Speech (TTS) models for English technical vocabulary and a regional language using Coqui TTS.

## Table of Contents
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Notes](#notes)

## Features
- Select between English technical vocabulary and regional language models.
- Input text area for entering the text to be synthesized.
- Generate and play audio from the input text.

## Dependencies
To run this project, you need to have the following dependencies installed:
- Python 3.8 or later
- Gradio
- SoundFile
- Coqui TTS

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AishwaryaChandel27/TEXT_TO-SPEECH-TTS
   cd TEXT_TO-SPEECH-TTS
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   You can install the dependencies using pip:
   ```bash
   pip install gradio soundfile TTS
   ```

## Usage
1. **Run the Gradio application:**
   After installing the dependencies, run the application with the following command:
   ```bash
   python app.py
   ```

2. **Access the app:**
   Open your web browser and navigate to the URL provided in the terminal (typically http://localhost:7860) to access the application.

3. **Using the app:**
   - Select the desired TTS model (English technical vocabulary or regional language).
   - Enter the text you want to synthesize in the provided input area.
   - Click the "Generate" button to create the audio.
   - Use the audio player to listen to the generated speech.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Notes
- Ensure you have all the necessary permissions and models for the TTS systems you are using.
- For any issues, please refer to the documentation of the respective dependencies or open an issue on the repository.
