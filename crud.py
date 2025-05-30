from sqlalchemy.orm import Session
from models import ReceiptFile, Receipt

def create_receipt_file(db: Session, file_name: str, file_path: str):
    db_file = ReceiptFile(file_name=file_name, file_path=file_path)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def validate_receipt_file(db: Session, receipt_file: ReceiptFile, is_valid: bool, reason: str = None):
    receipt_file.is_valid = is_valid
    receipt_file.invalid_reason = reason
    db.commit()

def mark_as_processed(db: Session, receipt_file: ReceiptFile):
    receipt_file.is_processed = True
    db.commit()

def save_receipt(db: Session, receipt_data: dict):
    db_receipt = Receipt(**receipt_data)
    db.add(db_receipt)
    db.commit()
    db.refresh(db_receipt)
    return db_receipt
