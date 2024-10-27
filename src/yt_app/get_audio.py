from pathlib import Path
import shutil
import subprocess
import argparse
from yt_app.constants import VIDEO_DIR, REPO_ROOT


def _generate_command(url:str, file_type:str) -> list:
    if(file_type == "mp3"):
        args = [
        "yt-dlp",
        "-o",
        "%(title)s.%(ext)s",
        "--extract-audio",
        "--audio-format",
        "mp3",
        "-P",
        VIDEO_DIR,
        url,
    ]
    else:
        args = [
            "yt-dlp",
            "-o",
            "%(title)s.%(ext)s",
            "-f",
            "mp4+bestaudio",
            "-P",
            VIDEO_DIR,
            url,
        ]
    return args

def _get_video(url:str, file_type:str) -> None:
    cmd = _generate_command(url, file_type)
    subprocess.run(cmd, cwd=REPO_ROOT)


def _clean_vid_dir(dir_name:Path):
    for file in dir_name.iterdir():
        if file.is_file() and file.name != "README.md":
            file.unlink()
        if file.is_dir():
            shutil.rmtree(file)

def _format_video_name(dir_name:Path) -> Path:
    for file in dir_name.iterdir():
        if file.name == "README.md":
            pass
        else:
            name = file.stem
            new_name = name.lower().replace(" ", "-")
            file_ext = file.suffix
            new_name = new_name + file_ext
            new_file = file.parent.joinpath(new_name)
            shutil.move(file, new_file)
    return new_file.resolve()

def download_youtube(url:str, file_type:str):
    _clean_vid_dir(dir_name=VIDEO_DIR)
    _get_video(url, file_type)
    file_path = _format_video_name(dir_name=VIDEO_DIR)
    return file_path

if __name__ == '__main__':
    url = 'https://youtu.be/jNQXAC9IVRw?si=z48CdD1MC_YwyQpp'
    download_youtube(url, 'mp4')