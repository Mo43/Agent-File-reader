import os
from smolagents import CodeAgent, InferenceClientModel
from dotenv import load_dotenv
from .tools import load_documents

load_dotenv()

model = InferenceClientModel(
    model_id = "Qwen/Qwen2.5-Coder-32B-Instruct",
)
agent = CodeAgent(
    tools=[load_documents], model=model
)
