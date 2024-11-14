import subprocess
import sys

def install_spotdl():
    """
    Installs the spotDL package if not already installed.
    """
    try:
        import spotdl
    except ImportError:
        print("Installing spotDL...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "spotdl"])

def download_spotify_content(url, bitrate='192k'):
    """
    Downloads Spotify playlists or individual tracks and converts them to MP3.
    
    Parameters:
    - url: str : Spotify URL (playlist or song).
    - bitrate: str : Desired MP3 bitrate (default is '192k').
    """
    try:
        # Run spotDL with specified URL and bitrate
        command = ["spotdl", "--bitrate", bitrate, url]
        subprocess.run(command, check=True)
        print("Download and conversion completed successfully.")
    except subprocess.CalledProcessError:
        print("There was an error with the download or conversion process.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    install_spotdl()
    # Replace with your desired Spotify URL (track or playlist)
    spotify_url = input("Enter the Spotify track or playlist URL: ")
    download_spotify_content(spotify_url)
