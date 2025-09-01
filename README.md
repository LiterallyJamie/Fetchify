# Fetchify

A very simple GUI app to download YouTube videos in mp4,mp3,webm format with a
Dark-themed interface with selectable video quality with a progress bar.

<img width="521" height="460" alt="Capture" src="https://github.com/user-attachments/assets/75de0a9e-9c85-4833-a8fc-1442c94b5c70" />

## Requirements (linux) *Outdated Version but still works but only does webm*
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

1: install chocolatey if you dont have it already. 
Run Powershell As Admin and type:
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


<img width="592" height="460" alt=";Capture" src="https://github.com/user-attachments/assets/a69ee01a-79df-4e6f-bb2b-ca6fb1b44175" />




#You may need to drag the box a bit to beable to see the text
##Before:

<img width="518" height="421" alt="dddd" src="https://github.com/user-attachments/assets/20be7de6-70a0-483b-bfec-c0790052d7ff" />

##After:

<img width="522" height="458" alt="dsa" src="https://github.com/user-attachments/assets/2f130325-72ec-4173-8084-c999ddf17b01" />
