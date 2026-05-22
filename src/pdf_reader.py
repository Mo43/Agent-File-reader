import os 
import fitz

def extract_pdf_text(file_path: str) -> str:
    """
    Extract text from a PDF file.
    """
    
    extracted_text = ""
    
    try:
        doc = fitz.open(file_path)
        for page in doc:
            extracted_text += page.get_text()
        doc.close()
    except Exception as e:
        return f"Error reading PDF: {e}"
    
    return extracted_text


    
    
