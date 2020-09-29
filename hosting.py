import uvicorn
PORT="8080"
from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "serve/test.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(some_file_path)
if __name__ == "__main__":
    uvicorn.run("hosting:app", host="0.0.0.0", port=int(PORT), reload=True, debug=True, workers=2)
