import tkinter as tk
from tkinter import filedialog, messagebox
import ffmpeg

def convert_to_stereo(input_file, output_file):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, ac=2)
            .run(overwrite_output=True)
        )
        messagebox.showinfo("Success", "Conversion to stereo completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_file():
    filename = filedialog.askopenfilename(title="Select a mono mp3, wav, or mp4 file", filetypes=[("Audio files", "*.mp4 *.wav *.mp3")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, filename)

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4"), ("WAV files", "*.wav"), ("MP3 files", "*.mp3")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, filename)

def convert():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if not input_file or not output_file:
        messagebox.showwarning("Warning", "Please select both input and output files.")
        return
    convert_to_stereo(input_file, output_file)

# Set up the main window
root = tk.Tk()
root.title("Mono to Stereo Converter")

# Input file
tk.Label(root, text="Input Mono Mp3, Wav, or Mp4 File:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=10, pady=10)

# Output file
tk.Label(root, text="Output Stereo Mp3, Wav, or Mp4 File:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
save_button = tk.Button(root, text="Save As", command=save_file)
save_button.grid(row=1, column=2, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert to Stereo", command=convert)
convert_button.grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
