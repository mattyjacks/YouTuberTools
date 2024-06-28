# YouTuberTools
 A collection of tools to be used for Matt's YouTuber journey



Instructions for Running the Audio Replacement Script
This script extracts audio from an MP4 video file, processes it using Eleven Labs API, and replaces the original audio in the video with the processed audio. Below are the steps to set up and run the script.

Prerequisites
Python 3.x - Ensure Python is installed on your machine.

FFmpeg - Ensure FFmpeg is installed and accessible via the command line.

Environment Variables:

ELEVENLABS_KEY     Your Eleven Labs API key.

Python Libraries
Install the following Python libraries using pip:

   pip install moviepy pydub requests tk


Running the Script
Open your terminal or command prompt.

Navigate to the directory where you saved the speech2speech.py script.

Run the script using the following command:

       python speech2speech.py

A file dialog will open. Select the MP4 file you want to process.

The script will extract the audio, process it with the Eleven Labs API, and generate a new MP4 file with the updated audio.

The output video will be saved in the final-mp4s folder with a prefix GIRLVOICE- added to the original filename.

To change the voice, run  get-11labs-voices.py to get a list of voice IDs and then replace the ID in line 93 in speech2speech.py with the voice ID you want.