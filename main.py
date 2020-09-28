import uvicorn
import os
import shutil
PORT="8080"
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

upload_folder = "uploads"
@app.get("/")
def read_root():
    return {"Hello": "World"}





@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    global upload_folder
    print(file)
    file_object = file.file
    #create empty file to copy the file_object to
    upload_folder = open(os.path.join(upload_folder, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(PORT), reload=True, debug=True, workers=2)
