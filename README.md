## Spotify Playlist/Track Downloader using spotdl
Downloads audio from YouTube based on Spotify metadata

**⚠️ Disclaimer:** 

This project is for educational and testing purposes only. Please respect artists' rights and do not use this tool for copyright infringement. Support artists by purchasing their music or using legitimate streaming services.

## How it works

spotdl uses Spotify's API to fetch metadata (song name, artist, album) and then searches YouTube for the matching audio to download.

Downloaded files will be saved to the `./Songs` directory. You can change this in Output directory.

## Prerequisites

- Python 3.8 or higher
- ffmpeg (required for audio conversion)

### Install ffmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
Download from https://ffmpeg.org/download.html or use:
```bash
choco install ffmpeg
```

## Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your credentials:
   - Go to https://developer.spotify.com/dashboard
   - Create an app
   - Copy your Client ID and Client Secret
   - Paste them into `.env` file

5. **Run the script:**
   ```bash
   python spotify_downloader.py
   ```

## Deactivating

When you're done, deactivate the virtual environment:
```bash
deactivate
```

## Usage

Edit `.env` file and update:
- `SPOTIFY_CLIENT_ID` - Your Spotify Client ID
- `SPOTIFY_CLIENT_SECRET` - Your Spotify Client Secret
- `SPOTIFY_URL` - The Spotify URL you want to download
- `OUTPUT_DIR` - Where to save downloaded files (default: `./Songs`)

Supported URLs:
- Single track: `https://open.spotify.com/track/...`
- Album: `https://open.spotify.com/album/...`
- Playlist: `https://open.spotify.com/playlist/...`
