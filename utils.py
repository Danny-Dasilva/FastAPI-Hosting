from fastapi import UploadFile


def save_upload_file(upload_file: UploadFile, destination: Path) -> None:
    try:
        with destination.open("wb") as buffer:
            shutil.copyfileobj(upload_file.file, buffer)
    finally:
        upload_file.file.close()


def save_upload_file_tmp(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp_path


def handle_upload_file(
    upload_file: UploadFile, handler: Callable[[Path], None]
) -> None:
    tmp_path = save_upload_file_tmp(upload_file)
    try:
        handler(tmp_path)  # Do something with the saved temp file
    finally:
        tmp_path.unlink()  # Delete the temp file



with destination.open("wb") as buffer:
    shutil.copyfileobj(upload_file.file, buffer)


uploaded_file.file.seek(0)  # <-- This.
with destination.open("wb") as buffer:
    shutil.copyfileobj(upload_file.file, buffer)


## Dont use / starlette streaming response
from starlette.responses import StreamingResponse
import asyncio

async def slow_numbers(minimum, maximum):
    yield('<html><body><ul>')
    for number in range(minimum + maximum +1):
        yield f"<li>%{number}</li>"
        await asyncio.sleep(0.5)
    yield('</ul></body></html>')

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    generatpr = slow_numbers(1, 10)
    response = StreamingResponse(generator, media_type='test/html')
    await responce(scope, receive, send)
