import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def extract_text_tesseract(image_path: str) -> str:
    return pytesseract.image_to_string(Image.open(image_path))


