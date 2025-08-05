# import re
# import json

# def parse_receipt_data(text: str) -> dict:
#     store = re.search(r"(Walmart|Target|Costco|Tesco)", text, re.IGNORECASE)
#     date = re.search(r"\d{2}/\d{2}/\d{4}", text)
#     total = re.search(r"Total\s+\$?([\d.]+)", text, re.IGNORECASE)
#     product_id = re.search(r"Product\s+ID[:\-]?\s*(\w+)", text, re.IGNORECASE)

#     return {
#         "store": store.group(1) if store else None,
#         "date": date.group(0) if date else None,
#         "total": float(total.group(1)) if total else None,
#         "product_id": product_id.group(1) if product_id else None
#     }

# def validate_receipt(data: dict) -> dict:
#     with open("backend/data/purchases.json") as f:   #
#         purchase_db = json.load(f)

#     for purchase in purchase_db:
#         if (
#             purchase["product_id"] == data["product_id"]
#             and purchase["store"].lower() == data["store"].lower()
#         ):
#             return {"status": "Return Approved", "match": purchase}

#     return {"status": "Not Eligible", "details": data}

import re
import json
import os

def parse_receipt_data(text: str) -> dict:
    store = re.search(r"(Walmart|Target|Costco|Tesco)", text, re.IGNORECASE)
    date = re.search(r"\d{2}/\d{2}/\d{4}", text)
    total = re.search(r"Total\s+\$?([\d.]+)", text, re.IGNORECASE)
    product_id = re.search(r"Product\s+ID[:\-]?\s*(\w+)", text, re.IGNORECASE)

    return {
        "store": store.group(1) if store else None,
        "date": date.group(0) if date else None,
        "total": float(total.group(1)) if total else None,
        "product_id": product_id.group(1) if product_id else None
    }

def validate_receipt(data: dict) -> dict:
    # 🔧 FIX: Use absolute path
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "../data/purchases.json")

    with open(data_path) as f:
        purchase_db = json.load(f)

    for purchase in purchase_db:
        if (
            purchase["product_id"] == data["product_id"]
            and purchase["store"].lower() == data["store"].lower()
        ):
            return {"status": "Return Approved", "match": purchase}

    return {"status": "Not Eligible", "details": data}
