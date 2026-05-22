from .ai_agent import agent

prompt = """
Read all files in the data folder.

Summarise the content clearly.

Include:
- Key points
-important insights
-conclusion

Save the output into outputs/final_summary.txt
"""

response = agent.run(prompt)

with open("outputs.final_summary.txt", "w", encoding="utf-8") as f:
    f.write(response)
    
if __name__ == "__main__":
    print("\n--- Triggering the AI Agent ---")
    prompt = (
        "Look inside the './data' folder, read all .txt and .pdf files in there, "
        "generate a clear summary and save that summary into a new file called 'final_summary.txt'."
    )
    response = agent.run(prompt)

    print("\nAgent Response:")
    print(response)

