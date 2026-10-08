"""
CareerIQ - Resume Parser
------------------------
Extracts clean text from an uploaded PDF resume
using PyMuPDF (fitz).
"""

import fitz


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF resume.

    Args:
        uploaded_file: Streamlit UploadedFile object (PDF).

    Returns:
        str: Extracted and cleaned resume text.
    """
    pdf_bytes = uploaded_file.read()
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

    try:
        text = ""
        for page in pdf_document:
            text += page.get_text() + "\n"
        return text.strip()
    finally:
        pdf_document.close()