from openai import OpenAI
import pyperclip
import os
import pyaudio
import wave
from tempfile import NamedTemporaryFile
from pynput import keyboard
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Set your OpenAI API key here
api_key = os.getenv("OPEN_AI_API")
client = OpenAI(api_key=api_key)

# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

# Global variables
is_recording = False
frames = []
listener = None  # Define listener in the global scope


def on_activate():
    global is_recording, frames, listener
    if not is_recording:
        is_recording = True
        frames = []
        print("Recording started...")
    else:
        is_recording = False
        print("Recording stopped.")
        listener.stop()  # Stop the listener when recording stops


def for_canonical(f):
    return lambda k: f(listener.canonical(k))


def record_audio():
    global frames, listener
    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    print("Press 'cmd+R' to start recording.")

    hotkey = keyboard.HotKey(keyboard.HotKey.parse("<cmd>+r"), on_activate)

    listener = keyboard.Listener(
        on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)
    )

    listener.start()
    print("Listener started...")

    while listener.running:
        if is_recording:
            try:
                data = stream.read(CHUNK, exception_on_overflow=False)
                frames.append(data)
            except OSError as e:
                print(f"Error reading audio stream: {e}")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames


def save_audio(frames, output_filename):
    wf = wave.open(output_filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()


def transcribe_audio(file_path):
    with open(file_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            prompt="Speaking American English",
        )
    return transcript.text


def main():
    temp_audio_path = "/Users/cvk/Downloads/[CODE] Local Projects/24SUMR_Whisper_on_opt-W_Mac/temp_audio.wav"

    # Record audio
    frames = record_audio()

    # Save the recorded audio to a temporary file
    save_audio(frames, temp_audio_path)

    # Transcribe the audio using OpenAI's Whisper API
    transcription = transcribe_audio(temp_audio_path)

    # Delete the temporary audio file
    os.unlink(temp_audio_path)

    # Copy transcription to clipboard
    pyperclip.copy(transcription)
    print("Transcription copied to clipboard:")
    print(transcription)


if __name__ == "__main__":
    main()
