import subprocess
import argparse

def generate_command(url:str) -> list:
    args = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format",
        "mp3",
        url,
    ]
    return args

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True)
    args = parser.parse_args()

    cmd = generate_command(args.url)

    subprocess.call(cmd)