# 🧾 Visual Receipt Scanner for Returns

## 🎯 Project Objective

Automate and streamline the **product return process** by using OCR-powered visual recognition to extract data from customer receipts and determine return eligibility.

---

## ✅ Problem It Solves

Traditional return processes require manual verification of receipts, leading to:
- Long customer wait times
- Human errors
- Frustrating user experiences

This project eliminates manual checks by automating receipt parsing and validation using AI.

---

## 🤖 AI & Tech Stack

| Component            | Technology Used         |
|---------------------|-------------------------|
| OCR Engine           | Tesseract (Open Source) |
| Backend API          | FastAPI (Python)        |
| Frontend Interface   | Streamlit (Python)      |
| Database             | JSON (Sample Records)   |
| Optional Upgrade     | Google Vision AI        |

---

## 🔄 Workflow Overview

1. **Upload Receipt**: User uploads a scanned receipt (.jpg/.png).
2. **OCR Extraction**: Tesseract extracts text from the image.
3. **Data Parsing**: Regex & NLP extract store name, date, product ID, and total.
4. **Validation**: Data is compared with a purchase database (JSON).
5. **Return Decision**: System returns a message: `"Return Approved"` or `"Not Eligible"`.

---

## 🗂️ Project Structure

```
visual-receipt-scanner/
├── backend/
│ ├── main.py # FastAPI app
│ ├── ocr/tesseract_ocr.py # OCR logic
│ ├── utils/parser.py # Regex parsing + validation
│ ├── models/schemas.py # Pydantic models
│ └── data/purchases.json # Sample purchase DB
│
├── frontend/
│ └── app.py # Streamlit UI
│
├── sample_receipts/
│ └── receipt1.jpg # Sample receipts
│
├── requirements.txt
└── README.md 
```

---

## 🚀 How to Run

### 1. Clone & Install Requirements

```bash
git clone <repo-url>
cd visual-receipt-scanner
pip install -r requirements.txt
```

### 2. Run Backend

```bash
cd backend
uvicorn main:app --reload
```

### 3. Run Frontend

```bash
cd frontend
streamlit run app.py
```
<img width="720" height="390" alt="image" src="https://github.com/user-attachments/assets/e363c2e2-fb90-4875-9d02-b0ddb6bdc91e" />

<img width="720" height="354" alt="image" src="https://github.com/user-attachments/assets/c36a2324-70d8-464d-910a-dac49f7e9648" />

---

## ⚙️ Future Enhancements
📸 Integrate Google Vision AI for high-accuracy multilingual OCR

🧠 Use NLP to better extract and normalize fields

☁️ Store receipts & decisions in a cloud DB

🛡️ Add authentication for secure uploads

📊 Admin dashboard for return statistics
