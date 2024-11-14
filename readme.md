# Spotify to MP3 Converter

A Python script that allows you to download songs and playlists from Spotify and convert them to MP3 format at 192kbps.

## Features

- Download entire Spotify playlists or individual songs.
- Convert downloaded tracks to MP3 format at 192kbps.
- Automatically embeds metadata from Spotify into MP3 files.

## Requirements

- **spotDL**: A command-line tool that downloads music from Spotify using YouTube as the audio source.
- **FFmpeg**: Required for audio processing and conversion.

## Installation

### Step 1: Install Python Packages

Run the following command to install `spotDL`:
- open up `cmd.exe` or `powershell`

```
pip install spotdl
```



## Installation

### 2. Install ffmpeg

#### Option A: Install with `winget` (Recommended for Windows Users)

Run this command in **Command Prompt** or **PowerShell** as Administrator:

```
winget install --id Gyan.FFmpeg -e --source winget
```

### Option B: Download and Manually Install

1. Download the latest `ffmpeg` build from [ffmpeg.org](https://ffmpeg.org/download.html) or [gyan.dev](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the files and add the `bin` directory (e.g., `C:\ffmpeg\bin`) to your system PATH.

- Verify `ffmpeg` installation by running:

```
ffmpeg -version
```

## Usage

1. Run the script in a terminal:
```
python main.py
```
or 
- Run the `launcher.bat` to run the `main.py` script to run the program.

Enter the Spotify track or playlist URL when prompted.
- copy and paste the entire `URL`

# Example 
```
https://open.spotify.com/track/7Ie9W94M7OjPoZVV216Xus?flow_ctx=f6ca8cb4-011f-4577-aa68-11e6ee014b32%3A1731636904#login?flow_ctx=f6ca8cb4-011f-4577-aa68-11e6ee014b32%3A1731636904
```
- The downloaded and converted MP3 files will be saved in the current directory.

## Prompt:

```
Enter the Spotify track or playlist URL: [paste Spotify URL here]
```

## LICENSE

## ***This project is proprietary and all rights are reserved by the author.***
## ***Unauthorized copying, distribution, or modification of this project is strictly prohibited.***
## ***Unless You have written permission from the Developer or the FNBUBBLES420 ORG.***


## Disclaimer

### Downloading and converting Spotify content may violate Spotify's Terms of Service. Use this tool responsibly and only for content you have the right to download.
