#!/usr/bin/env python3
from spotdl import Spotdl
from spotdl.types.options import DownloaderOptions
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration from environment variables
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_URL = os.getenv('SPOTIFY_URL', 'https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M')
OUTPUT_DIR = os.getenv('OUTPUT_DIR', './Songs')

def download_spotify_content(url):
    """Download Spotify track, album, or playlist"""
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Initialize Spotdl with your credentials
    spotdl = Spotdl(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        downloader_settings=DownloaderOptions(
            output=OUTPUT_DIR,
            format='mp3',
            bitrate='320k',
        )
    )
    
    print(f"Searching for: {url}")
    
    # Search and get song objects
    songs = spotdl.search([url])
    
    print(f"Found {len(songs)} song(s)")
    
    # Download the songs
    for song in songs:
        print(f"Downloading: {song.name} - {song.artist}")
    
    results = spotdl.download_songs(songs)
    
    print(f"\nDownload complete! Files saved to: {OUTPUT_DIR}")
    return results

if __name__ == "__main__":
    # Check if credentials are set
    if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
        print("Error: Spotify credentials not found!")
        print("\nPlease:")
        print("1. Copy .env.example to .env")
        print("2. Add your Spotify API credentials to .env")
        print("3. Get credentials from https://developer.spotify.com/dashboard")
        exit(1)
    
    try:
        download_spotify_content(SPOTIFY_URL)
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have:")
        print("1. Installed dependencies: pip install -r requirements.txt")
        print("2. Installed ffmpeg: brew install ffmpeg")
        print("3. Set valid Spotify API credentials in .env")
        print("4. Provided a valid Spotify URL")
