import os
import sys
from yt_dlp import YoutubeDL


class MusicDownloader:

    def __init__(self):
        self.save_dir = "./music/"
        self.filename = "%(title)s.%(ext)s"
        self.ydl_opts = {
            "outtmpl": self.save_dir + self.filename,
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        os.makedirs(self.save_dir, exist_ok=True)

    def download(self, url):
        try:
            print("Downloading...")
            with YoutubeDL(self.ydl_opts) as ydl:
                ydl.download(url)
                print("Download Complete")
        except Exception as e:
            raise e


def main():
    downloader = MusicDownloader()
    try:
        downloader.download(url=sys.argv[1])
    except IndexError:
        print("Enter the url")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
