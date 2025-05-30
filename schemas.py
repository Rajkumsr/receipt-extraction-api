from pydantic import BaseModel
from typing import Optional

class ReceiptFileBase(BaseModel):
    file_name: str
    file_path: str

class ReceiptBase(BaseModel):
    purchased_at: Optional[str]
    merchant_name: Optional[str]
    total_amount: Optional[float]
    file_path: str
