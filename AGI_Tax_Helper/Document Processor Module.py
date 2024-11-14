import pytesseract
from pdfplumber import PDF
from pathlib import Path
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()
    return text

def process_text(text):
    doc = nlp(text)
    transactions = []
    for ent in doc.ents:
        if ent.label_ in ["DATE", "MONEY", "ORG"]:
            transactions.append(ent.text)
    return transactions