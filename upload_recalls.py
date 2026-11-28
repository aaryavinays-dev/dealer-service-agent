import os
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient

load_dotenv()
client = SearchClient(
    endpoint=os.getenv("SEARCH_ENDPOINT"),
    index_name="recalls",                      
    credential=DefaultAzureCredential(),
)

docs = []
with open("data/sample_recalls.txt") as f:
    for line in f:
        if line.startswith("#") or not line.strip():
            continue                         # skip the header and empty lines
        make, model, year, recall_id, problem = [p.strip() for p in line.split("|")]   
        docs.append({"id": recall_id, "make": make, "model": model,
                     "year": int(year), "problem": problem})                       
        
result = client.upload_documents(documents=docs)        
print(f"Uploaded {len(docs)} recalls")