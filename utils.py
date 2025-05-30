from pdf2image import convert_from_path
from pytesseract import image_to_string
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

def is_valid_pdf(file_path):
    return file_path.endswith(".pdf")

def extract_text_from_pdf(file_path):
    images = convert_from_path(file_path, poppler_path=r"C:\poppler-24.08.0\Library\bin")
    text = ""
    for img in images:
        text += image_to_string(img)
    return text

def parse_receipt_text(text):
    merchant_name = text.split('\n')[0][:50]
    date_match = re.search(r'\d{2,4}[-/]\d{2}[-/]\d{2,4}', text)
    total_match = re.search(r'Total\s+\$?(\d+[\.\d+]*)', text, re.IGNORECASE)

    return {
        "purchased_at": date_match.group(0) if date_match else None,
        "merchant_name": merchant_name,
        "total_amount": float(total_match.group(1)) if total_match else None
    }
