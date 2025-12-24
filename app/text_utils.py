from pypdf import PdfReader
from io import BytesIO

def read_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="ignore")

def read_pdf(file_bytes: bytes) -> str:
    pdf_stream = BytesIO(file_bytes)   # ✅ FIX
    reader = PdfReader(pdf_stream)

    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text

def chunk_text(text: str, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks
