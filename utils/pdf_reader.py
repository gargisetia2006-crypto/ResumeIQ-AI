from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file.

    Args:
        pdf_path (str): Path to the uploaded PDF.

    Returns:
        str: Complete extracted text from the PDF.
    """

    reader = PdfReader(pdf_path)

    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            resume_text += text + "\n"

    return resume_text