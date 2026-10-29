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

# 6. Create the project client (the front desk) with the endpoint and an ID card
project = AIProjectClient(endpoint=endpoint, credential=DefaultAzureCredential())

# 7. Get the OpenAI client (room service) from the project
openai = project.get_openai_client()

# 8. Send one question to the model and print the answer
response = openai.responses.create(model=deployment, input="What is a vehicle safety recall?")
print(response.output_text)