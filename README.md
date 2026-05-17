# 15agentic — AI Agent Microservice
> A tool-using AI agent that *does work* via REST API — not a chatbot.
Built as a hands-on learning project to master agentic AI patterns: tool calling,
Retrieval-Augmented Generation (RAG), and multi-agent orchestration.
## What It Does
Send a task, the agent decides how to solve it:
```bash
curl -X POST /api/v1/run -d '{"task": "Who is the CEO of Tesla and what is 2+2?"}'
The agent reasons about the task, calls the right tools (web search, calculator),
and returns the answer along with a full trace of every tool it used.
Architecture
Client → FastAPI → LangGraph Agent → Gemini LLM
                         ↓
                   ┌──────┴──────┐
              Calculator      Web Search
              (sandboxed)    (DuckDuckGo)
- 
FastAPI async REST server with auto-generated OpenAPI docs
- 
LangChain + LangGraph agent orchestration (ReAct loop)
- 
Google Gemini (gemini-2.5-flash) as the reasoning engine
- 
Pydantic runtime validation for all API contracts
- 
Chroma vector store for Phase 2 document retrieval (planned)
Phase 1 — Complete ✅
Component	Status
API models (RunRequest, RunResponse, ToolCall)	✅
Calculator tool (sandboxed eval() with math whitelist)	✅
Web Search tool (DuckDuckGo instant answer API)	✅
Tool-using agent (create_agent with Gemini)	✅
POST /api/v1/run endpoint with tool trace	✅
Tech Stack
Layer	Choice
Framework	LangChain 1.x + LangGraph
LLM	Google Gemini 2.5 Flash (free tier)
API	FastAPI + Uvicorn
Validation	Pydantic v2 + Pydantic Settings
Package Mgmt	uv + pyproject.toml
Testing	pytest + pytest-async
Linting	ruff + mypy
Why This Project?
This is a learning project designed to build real understanding of agentic AI —
not framework lock-in. Every LangChain abstraction is paired with an explanation of
what the raw LLM SDK would do underneath. The goal: know how agents work, not just
how to use a library.
Quick Start
# Requirements: Python 3.11+, Google Gemini API key
git clone https://github.com/ericthomasc/15agentic.git
cd 15agentic
# Create venv and install
python -m venv .venv
source .venv/bin/activate
pip install uv
uv sync
# Add your API key
echo "GOOGLE_API_KEY=your-key-here" > .env
# Run
uv run uvicorn src.agent_service.main:app --reload
# Test
curl -X POST http://127.0.0.1:8000/api/v1/run \
  -H "Content-Type: application/json" \
  -d '{"task": "What is 2+2?"}'
Roadmap
- 
Phase 1: Single tool-using agent
- 
Phase 2: RAG — document retrieval with Chroma vector store
- 
Phase 3: Multi-agent — LangGraph supervisor + parallel specialists
