from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from ocr.tesseract_ocr import extract_text_tesseract
from utils.parser import parse_receipt_data, validate_receipt
import shutil
import os
import uuid

app = FastAPI()

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_receipt(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.jpg")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        raw_text = extract_text_tesseract(file_path)
        parsed_data = parse_receipt_data(raw_text)
        result = validate_receipt(parsed_data)
        return JSONResponse(content=result)
    finally:
        os.remove(file_path)




# from fastapi.responses import JSONResponse

# @app.post("/upload")
# async def upload(file: UploadFile = File(...)):
#     # Do OCR logic
#     extracted_text = "some text"
#     return JSONResponse(content={"text": extracted_text})
