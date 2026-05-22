import os
import fitz
from dotenv import load_dotenv
from smolagents import CodeAgent, InferenceClientModel, tool

load_dotenv()

#free cloud model hugging face 
model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct") 

#smart agent
agent = CodeAgent(tools=[], model=model)

print("\n--- Triggering the AI Agent ---")
response = agent.run("x")
print("\nAgent Response:")
print(response)

def _extract_pdf_text(file_path: str) -> str:
    """
    pull plain text from a PDF, one page at a time.
    """
    text_package = ""
    try:
        doc = fitz.open(file_path)
        for page in doc:
            text_package += page.get_text()
        doc.close()
    except Exception as e:
        return f"[Error reading PDF {os.path.basename(file_path)}: {str(e)}]"
    
    return text_package

@tool
def read_my_folder(folder_name: str) -> str:
    """
    A tool that opens a specific folder and reads .txt and .pdf files inside it.

    Args:
        folder_name: The name of the folder you want to look inside.
    """
    if not os.path.exists(folder_name):
        return f"cannot find the folder named {folder_name}"

    text_data = ""

    for file in  os.listdir(folder_name):
        path = os.path.join(folder_name, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                text_data += f"\n--- {file} ---\n" + f.read()
        elif file.endswith(".pdf"):
             pdf_text = _extract_pdf_text(path)
             text_data += f"\n--- {file} (PDF) ---\n" + pdf_text

    return text_data

@tool
def write_summary_file(filename: str, content: str) -> str:
    """
    A tool that creates a new text file and writes content or a summary inside it.

    Args:
        filename: The name of the file to create (e.g., 'summary.txt').
        content: The text or summary that should be written inside the file.
    """
    try:
        with open (filename, 'w', encoding= 'utf-8') as f:
                   f.write(content)
        return f"Successfully created and saved the file: {filename}"
    except Exception as e:
        return f"Failed to write file due to error {str(e)}"

model = InferenceClientModel(model_id="Qwen/Qwen2.5-Coder-32B-Instruct") 


agent = CodeAgent(tools=[read_my_folder, write_summary_file], model=model)


if __name__ == "__main__":
    print("\n--- Triggering the AI Agent ---")
    prompt = (
        "Look inside the './data' folder, read all .txt and .pdf files in there, "
        "generate a clear summary and save that summary into a new file called 'final_summary.txt'."
    )
    response = agent.run(prompt)

    print("\nAgent Response:")
    print(response)