import subprocess
import argparse

def generate_command(url:str, file_type:str) -> list:
    if(file_type == "mp3"):
        args = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format",
        "mp3",
        url,
    ]
    else:
        args = [
            "yt-dlp",
            "-f",
            "mp4+bestaudio",
            url,
        ]
    return args

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-u', '--url', required=True)
    # args = parser.parse_args()

    # cmd = generate_command(args.url)

    # subprocess.call(cmd)
    print("Copy and Paste the URL from YouTube")
    input_url = input()
    print("mp3 or mp4 (default is mp4)")
    file_input = input()
    cmd = generate_command(input_url, file_input)
    subprocess.call(cmd)
