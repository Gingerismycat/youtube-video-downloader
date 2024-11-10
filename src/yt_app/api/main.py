from fastapi import FastAPI
from fastapi.responses import FileResponse
from yt_app.get_audio import download_youtube

app = FastAPI()



@app.get("/get-my-vid/{url}", response_class=FileResponse)
async def get_my_vid(url:str):
    
    file_path = download_youtube(url, file_type="mp3")
    print(file_path)
    return FileResponse(str(file_path), media_type="mp3")