from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from yt_app.get_audio import download_youtube
from pydantic import BaseModel

class URLdata(BaseModel):
    url: str

app = FastAPI()

@app.get("/ping")
async def ping():
    return JSONResponse(
        content={"ping": "all good!"},
        status_code=200,
    )

@app.post("/add2")
async def add2(input:dict):
    value = input["value"]
    return {"result": value+2}

@app.get("/get-my-vid/")
async def get_my_vid(data:URLdata):
    
    file_path = download_youtube(data.url, file_type="mp3")
    return FileResponse(str(file_path), media_type="audio/mpeg")