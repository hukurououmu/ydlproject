import os
import sys
import subprocess


class Downloader:

    def __init__(self):
        self.save_dir = "./videos/"
        self.output = "%(title)s.%(ext)s"
        os.makedirs(self.save_dir, exist_ok=True)

    def download(self, url):
        command = (
            "yt-dlp",
            "--format",
            "137+140",
            "--merge-output-format",
            "mp4",
            "--output",
            self.save_dir + self.output,
            url
        )
        with subprocess.Popen(command) as process:
            process.wait()
            print("yt-dlp return code:", process.returncode)
            if process.returncode == 0:
                print("complete")
            else:
                print("yt-dlp error exit program")


def main():
    downlaoder = Downloader()
    try:
        downlaoder.download(url=sys.argv[1])
    except IndexError:
        print("Enter the URL of the Youtube video you want to download in the argument")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        raise e
