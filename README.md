# AI Doctor with Vision and Voice. 

**AI Doctor** is a multimodal application that acts as a virtual medical assistant. It combines **computer vision**, **speech recognition**, and **generative AI** to simulate a doctor's consultation. Users can upload medical images (e.g., skin conditions) and ask questions via voice. The AI analyzes the visuals and the audio query to provide a spoken response.

> **⚠️ DISCLAIMER:** This project is for **educational and learning purposes only**. It is not a replacement for professional medical advice, diagnosis, or treatment. Always consult a real medical professional for health concerns.

---

## 🌟 Features

- **Multimodal Analysis**: Analyzes both **Images** (X-rays, skin issues, etc.) and **Audio** (patient's verbal description) simultaneously.
- **Speech-to-Text (STT)**: Converts patient voice input into text using Groq's implementation of **Whisper-large-v3**.
- **Vision AI**: Uses Llama-based vision models (via Groq) to inspect images for medical anomalies.
- **Text-to-Speech (TTS)**: The AI "Doctor" responds with a realistic voice using **ElevenLabs** (primary) or **gTTS** (backup).
- **Interactive UI**: A simple, user-friendly web interface built with **Gradio**.

---

## 📂 Project Structure

- `gradio_app.py`: The main application file. It launches the Gradio web interface and orchestrates the inputs/outputs.
- `brain_of_the_doctor.py`: Handles image encoding and sends the visual data and text query to the Multimodal LLM.
- `voice_of_the_patient.py`: Handles audio transcription using the Groq API.
- `voice_of_the_doctor.py`: Converts the AI's text response into an audio file using ElevenLabs or gTTS.

---

## 🛠️ Prerequisites

Ensure you have **Python 3.8+** installed. You will also need **ffmpeg** installed on your system for audio processing.

### System Dependencies (ffmpeg)

- **Windows**: `winget install ffmpeg`
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### Python Libraries

Install the required packages using pip:

````bash
   pip install groq gradio speechrecognition pydub gTTS elevenlabs playsound python-dotenv
````
## 🔑 Configuration

You must set up your API keys for the application to function.

1.  **Create a `.env` file** in the root directory of your project.
2.  **Add the following keys** to the file:

```env
GROQ_API_KEY="your_groq_api_key_here"
ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"

