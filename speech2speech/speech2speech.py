import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip, AudioFileClip
from pydub import AudioSegment
import requests
import json
import shlex
import logging

# Setup basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Folders to store intermediate and output files
ORIG_MP3_FOLDER = "speech2speech/orig-mp3s/"
ELEVENLABS_MP3_FOLDER = "speech2speech/11labs-mp3s/"
FINAL_MP4_FOLDER = "speech2speech/final-mp4s/"

# Ensure directories exist
os.makedirs(ORIG_MP3_FOLDER, exist_ok=True)
os.makedirs(ELEVENLABS_MP3_FOLDER, exist_ok=True)
os.makedirs(FINAL_MP4_FOLDER, exist_ok=True)

# Fetch Eleven Labs API key from environment variables
api_key = os.getenv('ELEVENLABS_KEY')

# Initialize Tkinter
root = tk.Tk()
root.withdraw()

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    logging.info(f"File selected: {file_path}")
    return file_path

def extract_audio(mp4_path, mp3_path):
    try:
        clip = VideoFileClip(mp4_path)
        clip.audio.write_audiofile(mp3_path, codec='mp3')
        clip.close()
        logging.info("Audio extracted successfully.")
    except Exception as e:
        logging.error(f"Failed to extract audio: {e}")
        raise

def send_to_11labs(mp3_path, voice_id):
    CHUNK_SIZE = 1024
    XI_API_KEY = os.getenv('ELEVENLABS_KEY')
    original_filename_base = os.path.splitext(os.path.basename(mp3_path))[0]
    output_filename = f"11LABS-{original_filename_base}.mp3"
    OUTPUT_PATH = os.path.join(ELEVENLABS_MP3_FOLDER, output_filename)
    sts_url = f"https://api.elevenlabs.io/v1/speech-to-speech/{voice_id}/stream"
    headers = {"Accept": "application/json", "xi-api-key": XI_API_KEY}
    data = {"model_id": "eleven_english_sts_v2", "voice_settings": json.dumps({"stability": 0.5, "similarity_boost": 0.8})}
    files = {"audio": open(mp3_path, "rb")}

    try:
        response = requests.post(sts_url, headers=headers, data=data, files=files, stream=True)
        response.raise_for_status()
        with open(OUTPUT_PATH, "wb") as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                f.write(chunk)
        logging.info("Audio stream saved successfully.")
        return OUTPUT_PATH
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API call: {e}\n{response.text}")
        return None
    finally:
        files['audio'].close()

def replace_audio_in_video_ffmpeg(mp4_path, new_audio_path, output_path):
    cmd = f'ffmpeg -y -i "{mp4_path}" -i "{new_audio_path}" -c:v copy -map 0:v:0 -map 1:a:0 -c:a aac -strict experimental "{output_path}"'
    process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        logging.error(f"ffmpeg failed: {stderr}")
    else:
        logging.info("Audio replacement and video file generation successful.")

def main():
    mp4_path = select_file()
    if not mp4_path:
        logging.info("No file selected")
        return
    filename = os.path.basename(mp4_path)
    file_prefix = "GIRLVOICE-"
    audio_filename = os.path.splitext(filename)[0] + ".mp3"
    video_output_filename = file_prefix + filename
    orig_mp3_path = os.path.join(ORIG_MP3_FOLDER, audio_filename)
    final_mp3_path = os.path.join(ELEVENLABS_MP3_FOLDER, "fixed_output.mp3")
    output_mp4_path = os.path.join(FINAL_MP4_FOLDER, video_output_filename)
    
    extract_audio(mp4_path, orig_mp3_path)
    new_mp3_path = send_to_11labs(orig_mp3_path, "EXAVITQu4vr4xnSDxMaL")
    if not new_mp3_path:
        logging.info("Failed to obtain the new audio file from 11labs API.")
        return
    
    replace_audio_in_video_ffmpeg(mp4_path, new_mp3_path, output_mp4_path)
    logging.info(f"New video saved to {output_mp4_path}")

if __name__ == "__main__":
    main()