# Fetchify

A very simple GUI app to download YouTube videos in mp4,mp3,webm format with a
Dark-themed interface with selectable video quality with a progress bar.

<img width="521" height="460" alt="Capture" src="https://github.com/user-attachments/assets/75de0a9e-9c85-4833-a8fc-1442c94b5c70" />

## Requirements (linux)
- Python 3
- python3-venv
- python3-tk

## Installation (Ubuntu)
1. Install dependencies if not already:
```bash
sudo apt update
sudo apt install python3-venv python3-tk
```
2. Download Latest Ytdownloader.deb from releases.
3. install it
```bash
sudo dpkg -i YtDownloader.deb
sudo apt-get install -f
```
Thats it!
The installer automatically makes a .desktop so it will appear in you app launcher.

To run it from terminal:
```bash
ytdownloader
```
   
## Installation (Windows)
Make sure you have FFmpeg installed if not heres how:

1: install chocolatey if not already: 
open powershell and type:
```bash
Set-ExecutionPolicy Bypass -Scope Process -Force
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2: Install FFmpeg:
```bash
choco install ffmpeg
```
3: Download installer from releases
4: Run it (The installer will guide you from there)


