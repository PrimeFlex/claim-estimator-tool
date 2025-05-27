import PyPDF2
import pandas as pd
import re

def extract_amount_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        match = re.search(r'Net Claim[:\s]*\$?([\d,]+\.\d{2})', text)
        if match:
            return float(match.group(1).replace(",", ""))
    return None

def extract_amount_from_excel(excel_path):
    df = pd.read_excel(excel_path)
    for col in df.columns:
        if 'total' in col.lower() or 'estimate' in col.lower():
            try:
                value = float(df[col].iloc[0])
                return value
            except:
                continue
    return None
