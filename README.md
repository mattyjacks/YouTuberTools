# YouTuberTools
 A collection of tools to be used for Matt's YouTuber journey


# Current Tools

## Speech2Speech

Using 11Labs Speech2Speech Synthesis, this tool takes an input video (mp4 only), takes out the audio, sends it to 11Labs to turn it into a different voice using the power of artificial intelligence, and then puts the modified voice back into the video.

## Mono2Stereo

This tool takes input video (mp4 only) files that only have sound coming out of one output side, and copies the output audio over to the other track. Not tested very much.

# Future Tools

## ScreenShotter

This lets you go through a video and take a full-size screenshot of any frame; great for thumbnails!

## VidStacker

This tool takes up to 5 videos in order and combines them into 1 video, combining them together in order. This is particularly good for workflows where you have a super-short intro, the video itself, a sponsor segment, an outro, and an end-screen.


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
