import os
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, ReceiptFile
import crud, utils

UPLOAD_DIR = "receipts"
os.makedirs(UPLOAD_DIR, exist_ok=True)

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return crud.create_receipt_file(db, file.filename, file_path)

@app.post("/validate")
def validate_file(file_id: int, db: Session = Depends(get_db)):
    db_file = db.query(ReceiptFile).get(file_id)
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")

    valid = utils.is_valid_pdf(db_file.file_path)
    reason = None if valid else "Invalid file type"
    crud.validate_receipt_file(db, db_file, valid, reason)
    return {"file_id": file_id, "is_valid": valid, "reason": reason}

@app.post("/process")
def process_file(file_id: int, db: Session = Depends(get_db)):
    db_file = db.query(ReceiptFile).get(file_id)
    if not db_file or not db_file.is_valid:
        raise HTTPException(status_code=400, detail="Invalid or missing file")

    text = utils.extract_text_from_pdf(db_file.file_path)
    data = utils.parse_receipt_text(text)
    data["file_path"] = db_file.file_path
    crud.save_receipt(db, data)
    crud.mark_as_processed(db, db_file)
    return {"message": "Processed"}

@app.get("/receipts")
def get_all_receipts(db: Session = Depends(get_db)):
    return db.query(ReceiptFile).all()

@app.get("/receipts/{id}")
def get_receipt_by_id(id: int, db: Session = Depends(get_db)):
    receipt = db.query(ReceiptFile).get(id)
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt
