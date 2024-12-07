from PyPDF2 import PdfReader
from docx import Document

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        text = ''.join(page.extract_text() for page in reader.pages)
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = ''.join(paragraph.text for paragraph in doc.paragraphs)
    else:
        raise ValueError("Unsupported file type.")
    return text
