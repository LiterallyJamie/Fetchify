#!/usr/bin/env python3


import tkinter as tk
from tkinter import filedialog, ttk
import threading
import yt_dlp
import re
import os

# ---------------- Functions ----------------
def download_video():
    url = url_entry.get().strip()
    if not url:
        add_status("❌ Please enter a YouTube link.", "red")
        return

    folder = filedialog.askdirectory()
    if not folder:
        add_status("❌ No folder selected.", "red")
        return

    quality = quality_var.get()
    if quality == "1080p":
        format_code = "bestvideo[height<=1080]+bestaudio/best"
    elif quality == "720p":
        format_code = "bestvideo[height<=720]+bestaudio/best"
    elif quality == "Audio Only":
        format_code = "bestaudio"
    else:
        format_code = "best"

    add_status(f"⬇️ Downloading ({quality})...", "blue")
    download_button.config(state="disabled")
    progress_bar['value'] = 0

    def run_download():
        try:
            ydl_opts = {
                'format': format_code,
                'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
                'progress_hooks': [progress_hook]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            add_status("✅ Download complete!", "green")
        except Exception as e:
            add_status(f"❌ Download failed: {e}", "red")
        finally:
            download_button.config(state="normal")
            progress_bar['value'] = 0

    threading.Thread(target=run_download, daemon=True).start()

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0.0%')
        percent_num = float(percent.replace('%','').strip())
        progress_bar['value'] = percent_num

def add_status(message, color="white"):
    status_box.config(state="normal")
    status_box.insert(tk.END, message + "\n")
    status_box.tag_add(message, f"{status_box.index('end')}-2l", "end-1l")
    status_box.tag_config(message, foreground=color)
    status_box.see(tk.END)
    status_box.config(state="disabled")

def open_folder():
    folder = filedialog.askdirectory()
    if folder:
        if os.name == "nt":
            os.startfile(folder)
        else:
            subprocess.Popen(["xdg-open", folder])

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#1e1e1e")  # dark background

label_font = ("Arial", 12)
entry_font = ("Arial", 11)
button_font = ("Arial", 12, "bold")

fg_color = "#ffffff"
button_bg = "#0078D7"
button_fg = "#ffffff"

# Title
title_label = tk.Label(root, text="📥 YouTube Video Downloader", font=("Arial", 16, "bold"),
                       fg=fg_color, bg="#1e1e1e")
title_label.pack(pady=10)

# URL Entry
tk.Label(root, text="YouTube Link:", font=label_font, fg=fg_color, bg="#1e1e1e").pack()
url_entry = tk.Entry(root, width=55, font=entry_font)
url_entry.pack(pady=5)

# Quality Selector
tk.Label(root, text="Select Quality:", font=label_font, fg=fg_color, bg="#1e1e1e").pack()
quality_var = tk.StringVar(value="Best Available")
quality_options = ["Best Available", "1080p", "720p", "Audio Only"]
quality_menu = tk.OptionMenu(root, quality_var, *quality_options)
quality_menu.config(font=entry_font, bg="#2e2e2e", fg=fg_color)
quality_menu.pack(pady=5)

# Download Button
download_button = tk.Button(root, text="⬇ Download", font=button_font,
                            bg=button_bg, fg=button_fg, command=download_video)
download_button.pack(pady=10)

# Progress Bar
progress_frame = tk.Frame(root, bg="#1e1e1e")
progress_frame.pack(pady=5)
progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(side="left")

# Open Folder Button
open_folder_button = tk.Button(root, text="📂 Open Folder", font=("Arial", 11, "bold"),
                               bg="#2e2e2e", fg=fg_color, command=open_folder)
open_folder_button.pack(pady=5)

# Status Box (log)
status_box = tk.Text(root, width=60, height=8, font=("Arial", 10), bg="#2e2e2e", fg=fg_color, state="disabled")
status_box.pack(pady=10)

root.mainloop()
