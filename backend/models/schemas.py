from pydantic import BaseModel

class ReceiptData(BaseModel):
    store: str
    date: str
    total: float
    product_id: str