# dealer service recall agent

## The problem
Dealership service teams often miss open safety recalls on their customers'
vehicles. Tracking which vehicles are affected, notifying owners, and booking
the repair is largely manual and hard to keep up with, so many recalls go
unrepaired. That leaves a safety risk on the road, and it leaves recall repair
work, which the manufacturer pays the dealer for, undone. This project draws on
my experience at FordDirect and my own research.

## What this agent will do
1. Find customer vehicles with open safety recalls
2. Explain each recall to service advisors, with sources
3. Draft outreach to owners and book service, with human approval

## Design choices
| Job | Service / model | Why |
|---|---|---|
| Chat | gpt-5.4-mini | Cheap and fast |
| Recall lookup (planned, Lab 2-3) | Model calls a tool; Azure AI Search over recall documents | Grounds answers in the actual recall documents |
| VIN format check (planned, Lab 3) | Plain Python, no model | Free, instant, exact |
| Read recall PDFs (planned, Lab 4) | Azure AI Document Intelligence | Pulls text and tables reliably |
| Voice (planned, Lab 5) | Azure AI Speech | Speech-to-text in, text-to-speech out |
| Read a photo (planned, Lab 6) | Multimodal GPT with vision, or Azure AI Vision | GPT with vision understands the whole photo (damage, labels); Azure AI Vision is cheaper when you only need the text |

## Status
v1: chat loop with history, guardrail and env check