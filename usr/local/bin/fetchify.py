import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import os
import yt_dlp

download_folder = os.getcwd()  # Default folder

# -------------------------
# Functions
# -------------------------
def choose_folder():
    global download_folder
    folder = filedialog.askdirectory()
    if folder:
        download_folder = folder
        folder_var.set(f"Save to: {download_folder}")

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    format_choice = format_var.get()
    quality_choice = quality_var.get()
    status_var.set(f"Downloading {format_choice} at {quality_choice}...")
    progress_var.set(0)
    progress_bar["value"] = 0
    percent_label.config(text="0%")

    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
            downloaded = d.get('downloaded_bytes', 0)
            if total > 0:
                percent = int(downloaded / total * 100)
                progress_var.set(percent)
                progress_bar["value"] = percent
                percent_label.config(text=f"{percent}%")
        elif d['status'] == 'finished':
            # Finished downloading, start conversion animation if needed
            status_var.set("Converting...")
            progress_bar.config(mode="indeterminate")
            progress_bar.start(10)  # pulsing animation

    def run_download():
        try:
            output_template = os.path.join(download_folder, "%(title)s.%(ext)s")

            if format_choice == "MP4":
                if quality_choice == "best":
                    ydl_opts = {
                        "format": "bestvideo+bestaudio/best",
                        "outtmpl": output_template,
                        "progress_hooks": [progress_hook],
                        "postprocessors": [
                            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
                        ],
                    }
                else:
                    height = int(quality_choice.replace("p",""))
                    ydl_opts = {
                        "format": f"bestvideo[height<={height}]+bestaudio/best",
                        "outtmpl": output_template,
                        "progress_hooks": [progress_hook],
                        "postprocessors": [
                            {"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}
                        ],
                    }

            elif format_choice == "WebM":
                if quality_choice == "best":
                    ydl_opts = {
                        "format": "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]",
                        "outtmpl": output_template,
                        "merge_output_format": "webm",
                        "progress_hooks": [progress_hook]
                    }
                else:
                    height = int(quality_choice.replace("p", ""))
                    ydl_opts = {
                        "format": f"bestvideo[ext=webm][height<={height}]+bestaudio[ext=webm]/best[ext=webm]",
                        "outtmpl": output_template,
                        "merge_output_format": "webm",
                        "progress_hooks": [progress_hook]
                    }

            elif format_choice == "MP3":
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": output_template,
                    "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3", "preferredquality": "192"}],
                    "progress_hooks": [progress_hook]
                }

            else:
                raise ValueError("Unknown format")

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            status_var.set("✅ Download complete!")

        except Exception as e:
            status_var.set("❌ Error: " + str(e))
        finally:
            progress_bar.stop()
            progress_bar.config(mode="determinate")
            progress_bar["value"] = 100
            percent_label.config(text="100%")

    threading.Thread(target=run_download).start()

# -------------------------
# GUI Setup
# -------------------------
root = tk.Tk()
root.title("Fetchify")
root.geometry("520x420")
root.configure(bg="#1e1e1e")

# Title
title_label = tk.Label(root, text="Fetchify", font=("Segoe UI", 26, "bold"), fg="#00c8ff", bg="#1e1e1e")
title_label.pack(pady=(20,15))

# URL Entry
url_entry = tk.Entry(root, width=55, font=("Segoe UI", 14), bg="#2a2a2a", fg="white", insertbackground="white")
url_entry.pack(pady=5)

# Format Selector
format_var = tk.StringVar(value="MP4")
tk.Label(root, text="Format:", fg="white", bg="#1e1e1e", font=("Segoe UI", 10)).pack()
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=["MP4","MP3","WebM"], state="readonly", font=("Segoe UI", 10))
format_dropdown.pack(pady=5)

# Quality Selector
quality_var = tk.StringVar(value="best")
tk.Label(root, text="Quality:", fg="white", bg="#1e1e1e", font=("Segoe UI", 10)).pack()
quality_dropdown = ttk.Combobox(root, textvariable=quality_var, values=["best","1080p","720p","480p","360p"], state="readonly", font=("Segoe UI", 10))
quality_dropdown.pack(pady=5)

# Folder Selection
folder_var = tk.StringVar(value=f"Save to: {download_folder}")
folder_label = tk.Label(root, textvariable=folder_var, fg="white", bg="#1e1e1e", font=("Segoe UI", 10))
folder_label.pack(pady=2)
choose_folder_btn = tk.Button(root, text="Choose Folder", command=choose_folder, bg="#00c8ff", fg="white", relief="flat", font=("Segoe UI", 10), bd=0)
choose_folder_btn.pack(pady=3)

# Download Button
download_btn = tk.Button(root, text="Download", command=download_video, bg="#ff5a5f", fg="white", font=("Segoe UI", 14, "bold"), relief="flat", bd=0)
download_btn.pack(pady=10, ipadx=10, ipady=5)

# Progress Bar + Percentage
progress_var = tk.IntVar()
style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", foreground="#00c8ff", background="#00c8ff", troughcolor="#2a2a2a", thickness=22)

progress_bar = ttk.Progressbar(root, mode="determinate", length=450, variable=progress_var, maximum=100, style="TProgressbar")
progress_bar.pack(pady=5)
percent_label = tk.Label(root, text="0%", fg="white", bg="#1e1e1e", font=("Segoe UI", 10))
percent_label.pack(pady=2)

# Status Label
status_var = tk.StringVar(value="Ready")
status_label = tk.Label(root, textvariable=status_var, fg="white", bg="#1e1e1e", font=("Segoe UI", 10))
status_label.pack(pady=5)

root.mainloop()
