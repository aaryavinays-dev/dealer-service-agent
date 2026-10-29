# 1. Import os, and load_dotenv from dotenv
import os
from dotenv import load_dotenv

# 2. Import DefaultAzureCredential and AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# 3. Load the .env file
load_dotenv()

# 4. Read AZURE_AI_PROJECT_ENDPOINT and MODEL_DEPLOYMENT into two variables
endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
deployment = os.getenv("MODEL_DEPLOYMENT")

# 5. Print both, to check they loaded
print(endpoint)
print(deployment)

INSTRUCTIONS = """You help dealership service advisors find and track vehicle safety recalls.
Only answer questions about safety recalls and vehicle service.
Never make up recall numbers, dates, or repair steps.
If you don't know, say so, explain why, and say what information you need (for example, the VIN).
Keep answers to 6 lines or fewer."""

# 6. Create the project client (the front desk) with the endpoint and an ID card
project = AIProjectClient(endpoint=endpoint, credential=DefaultAzureCredential())

# 7. Get the OpenAI client (room service) from the project
openai = project.get_openai_client()

response = openai.responses.create(model=deployment, instructions=INSTRUCTIONS, input="What's a good pizza place near Northville?")
print(response.output_text)

