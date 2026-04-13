# AI Doctor with Vision and Voice.

**AI Doctor** is a multimodal application that acts as a virtual medical assistant. It combines **computer vision**, **speech recognition**, and **generative AI** to simulate a doctor's consultation. Users can upload medical images (e.g., skin conditions) and ask questions via voice. The AI analyzes the visuals and the audio query to provide a spoken response.

> **⚠️ DISCLAIMER:** This project is for **educational and learning purposes only**. It is not a replacement for professional medical advice, diagnosis, or treatment. Always consult a real medical professional for health concerns.

---

## 🌟 Features

- **Multimodal Analysis**: Analyzes both **Images** (X-rays, skin issues, etc.) and **Audio** (patient's verbal description) simultaneously.
- **Speech-to-Text (STT)**: Converts patient voice input into text using Groq's implementation of **Whisper-large-v3**.
- **Vision AI**: Uses Llama-based vision models (via Groq) to inspect images for medical anomalies.
- **Text-to-Speech (TTS)**: The AI "Doctor" responds with a realistic voice using **ElevenLabs** (primary).
- **Interactive UI**: A simple, user-friendly web interface built with **Gradio**.

---

## 📂 Project Structure

- `gradio_app.py`: The main application file. It launches the Gradio web interface and orchestrates the inputs/outputs.
- `brain_of_the_doctor.py`: Handles image encoding and sends the visual data and text query to the Multimodal LLM.
- `voice_of_the_patient.py`: Handles audio transcription using the Groq API.
- `voice_of_the_doctor.py`: Converts the AI's text response into an audio file using ElevenLabs.

---

## 🛠️ Prerequisites

Ensure you have **Python 3.8+** installed. You will also need **ffmpeg** installed on your system for audio processing.

### System Dependencies (ffmpeg)

- **Windows**: `winget install ffmpeg`
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### Python Libraries

Install the required packages using pip:

```bash
   pip install groq gradio speechrecognition pydub gTTS elevenlabs playsound python-dotenv
```

## 🔑 Configuration

You must set up your API keys for the application to function.

1.  **Create a `.env` file** in the root directory of your project.
2.  **Add the following keys** to the file:

```env
GROQ_API_KEY="your_groq_api_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"
```

# 🚀 First-Time Setup Guide

This guide explains how to run the project locally after cloning it from GitHub.

## 1. Clone the Repository

```bash
git clone https://github.com/username/AI-Doctor-with-Vision-and-Voice.git
cd AI-Doctor-with-Vision-and-Voice
```

---

## 2. Check Python Version

Ensure you have Python 3.13 installed:

```bash
python --version
```

---

## 3. Install Pipenv

If you don’t already have it:

```bash
pip install pipenv
```

---

## 4. Create and Activate Virtual Environment

Inside the project folder:

```bash
pipenv install
pipenv shell
```

- `pipenv install` installs all dependencies from `Pipfile`/`Pipfile.lock`.
- `pipenv shell` activates the environment.

---

## 5. Verify Dependencies

Check that packages like `gradio` are installed:

```bash
pip list
```

If something is missing:

```bash
pipenv install gradio
```

---

## 6. Configure VS Code (for Pylance)

- Open **Command Palette** (`Ctrl+Shift+P`).
- Select **Python: Choose Interpreter**.
- Pick the interpreter from your pipenv environment:
  ```
  C:\Users\<your-username>\.virtualenvs\AI-Doctor-with-Vision-and-Voice-<hash>\Scripts\python.exe
  ```

---

## 7. Run the Application

```bash
python gradio_app.py
```

or

```bash
pipenv run python gradio_app.py
```

---

## 8. (Optional) Export Requirements for Plain Pip

If you prefer not to use pipenv:

```bash
pipenv requirements > requirements.txt
pip install -r requirements.txt
```

---

## ⚡ Common Issues

- **`Import "gradio" could not be resolved`** → VS Code is pointing to the wrong interpreter. Fix by selecting the pipenv interpreter.
- **Installation errors (`OSError: No such file or directory`)** → Clear pipenv cache:
  ```bash
  pipenv --clear
  pipenv install
  ```
- **Environment mismatch** → Always run inside the pipenv shell or use `pipenv run`.
