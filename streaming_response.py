import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
some_file_path = "serve/test.mp4"



PORT="8080"
app = FastAPI()

# headers = {
    # "Accept-Ranges": "bytes",
    # "Content-Length": str(sz),
    # "Content-Range": F"bytes {asked}-{sz-1}/{sz}",
# }
# response =  StreamingResponse(streaming_file(file_path, CS, asked), headers=headers,


@app.get("/")
async def main():
    headers = {
        "Accept-Ranges": "bytes",
        "Content-Length": str(sz),
        "Content-Range": F"bytes {asked}-{sz-1}/{sz}",
    }
    file_like = open(some_file_path, mode="rb")
    # response =  StreamingResponse(streaming_file(file_path, CS, asked), headers=headers,
    return StreamingResponse(file_like, media_type="video/mp4")
if __name__ == "__main__":
    uvicorn.run("streaming_response:app", host="0.0.0.0", port=int(PORT), reload=True, debug=True, workers=2)
