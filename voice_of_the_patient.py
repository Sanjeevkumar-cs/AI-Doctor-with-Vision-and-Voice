import os
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from groq import Groq
from pathlib import Path

# --- CONFIG ---
# Using Path ensures your file paths work on both Windows and Linux/Mac
audio_filepath = Path("patient_voice.mp3")
stt_model = "whisper-large-v3"

# --- FUNCTIONS ---
def record_audio(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🔴 [RECORDING] Please speak now...")
            # Calibrates the mic to your room's background noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.listen(source, timeout=10)
            
            # Convert the raw data to MP3
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            
            # Exporting to MP3 helps reduce API upload time
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            print(f"✅ Audio saved to {file_path}")
    except Exception as e:
        print(f"❌ Recording failed: {e}")

def transcribe_with_groq(model, file_path):
    # Ensure the API key is accessible (set it in your .env or environment)
    client = Groq(api_key=os.environ.get("GROQ_API_KEY")) 

    print("⚙️ AI is transcribing...")
    
    # Opening the file in binary mode is the standard way to send to Groq
    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=model,
            file=audio_file,
            language="en",
            response_format="text" # Returns string directly
        )
    return transcription

# --- EXECUTION ---
# uncomment the following lines to run the recording and transcription process in this file directly. This is useful for testing the voice of the patient component independently.

# # 1. Record the patient's voice
# record_audio(audio_filepath)

# # 2. Check if file was actually created before transcribing
# if audio_filepath.exists():
#     text_result = transcribe_with_groq(stt_model, audio_filepath)
#     print(f"\n📢 PATIENT SAID: {text_result}")
# else:
#     print("⚠️ No audio file found to transcribe.")