import os

def read_text_file(file_path: str) -> str:
    """
    Read a .txt file and return its contents as a string
    """
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

    except Exception as e:
        return f"Error reading text file {os.path.basename(file_path)}: {e}"
    