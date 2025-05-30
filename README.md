## Receipt Extraction API

A FastAPI-based application that extracts text from scanned PDF receipts using Tesseract OCR and stores the data in an SQLite database.

Why FastAPI?

We chose FastAPI because it makes building APIs in Python quick and efficient. It automatically handles request validation, error responses, and interactive documentation, which saves a lot of development time. With its support for modern Python features like type hints, it's easier to write clean and reliable code. FastAPI is also really fast in terms of performance, making it a great choice for production ready APIs.

----------------------------------------------------------------------

## Setup and Run Instructions

# Prerequisites

- Python 3.8+
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases)

----------------------------------------------------------------------

# Steps

1. Clone the repo:

   git clone https://github.com/your-username/receipt-extraction-api.git
   cd receipt-extraction-api

2. Create and activate a virtual environment:

    python -m venv venv
    venv\Scripts\activate  # On Windows

3. Install dependencies:

    pip install -r requirements.txt

4. Install Tesseract OCR

    Download and install from:
    https://github.com/UB-Mannheim/tesseract/wiki

    Add Tesseract path to system environment variables.

5. Install Poppler for Windows (for PDF to image conversion)

    Download from:
    https://github.com/oschwartz10612/poppler-windows/releases

    Add the bin folder to your system PATH.

6   . Start the API:

    uvicorn app.main:app --reload

----------------------------------------------------------------------

# API Usage
1. Upload PDF Receipt
    POST /upload

    Form field: file (PDF)

    Response:

    json
    {
    "message": "File uploaded and processed successfully"
    }

2. View Extracted Receipts
    GET /receipts

    Response:

    json
    [
    {
        "id": 1,
        "file_name": "venetian_434280912998.pdf",
        "text": "11/25/18, THE VENETIAN? | THE PALAZZO”",
        "upload_time": "2025-05-30 05:54:34.215578"
    }
    ]

# Execution Instructions
    1. Ensure Tesseract and Poppler are installed and configured.
    2. Activate virtual environment.
    3. Run the FastAPI server.
    4. Use Swagger UI at http://127.0.0.1:8000/docs to test the endpoints.
    5. Check the SQLite database file receipts.db for saved records.
