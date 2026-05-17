from fastapi import FastAPI
from agent_service.agents.tool_agent import agent
from agent_service.models.schemas import (
    IngestRequest,
    RunRequest,
    RunResponse,
    ToolCall,
)

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ingest")
async def ingest(request: IngestRequest):
    return {"recieved": len(request.documents)}


@app.post("/api/v1/run")
async def run_task(request: RunRequest) -> RunResponse:
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": request.task}]}
    )
    messages = result["messages"]
    final_answer = ""
    tool_calls = []
    pending = {}
    for msg in messages:
        if msg.type == "ai" and msg.content and not msg.tool_calls:
            final_answer = msg.content
        elif msg.type == "ai" and msg.tool_calls:
            for tc in msg.tool_calls:
                tc_obj = ToolCall(tool=tc["name"], input=tc["args"], output="")
                tool_calls.append(tc_obj)
                pending[tc["id"]] = tc_obj
        elif msg.type == "tool" and hasattr(msg, "tool_call_id"):
            call_id = msg.tool_call_id
            if call_id in pending:
                pending[call_id].output = str(msg.content)

    return RunResponse(result=final_answer, tool_calls=tool_calls)
