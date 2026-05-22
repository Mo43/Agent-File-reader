import os
from smolagents import tool
from .pdf_reader import extract_pdf_text
from .text_reader import read_text_file
@tool
def load_documents(folder_path: str) -> str:
    """
    Reads all PDFs and TXT files in a folder and returns combined text.
    
    Args:
    folder_path(str): Path to the folder containing documents
    """

    if not os.path.exists(folder_path):
        return "Folder does not exist."

    all_text = ""

    for file_name in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file_name)

        # PDF FILE
        if file_name.endswith(".pdf"):
            text = extract_pdf_text(full_path)
            all_text += f"\n\n--- {file_name} ---\n\n"
            all_text += text

        # TEXT FILE
        elif file_name.endswith(".txt"):
            text = read_text_file(full_path)
            all_text += f"\n\n--- {file_name} ---\n\n"
            all_text += text

    return all_text[:15000]


