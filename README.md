# Receipt Extraction API

## Overview
A FastAPI-based web application that extracts text and data from uploaded PDF receipts using OCR (Tesseract) and stores the information in an SQLite database.

---

## Setup Instructions

### 1. Install Dependencies

Install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases) and [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki) (add both to PATH).

Then, set up Python environment:

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
pip install -r requirements.txt
