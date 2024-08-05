# youtube-video-downloader

For further documentation: "https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation"

1. If you have not created a virtual environemnt, set up conda environment (python 3.12)
```console
conda create -n yt-app python=3.12
```
If you have previously set up the virtual environment, run 
```console
conda actvate yt-app
```

2. install dependencies:
```console
pip install yt-dlp 
```

3. If you don't have ffmpeg, use the website linked: "https://phoenixnap.com/kb/install-ffmpeg-ubuntu" 

4. Run the python script:
```console
python get_audio.py
```
5. Paste the Youtube URL

6. Write "mp3" to download as an audio mp3 file or write "mp4" to write as a video mp4 file