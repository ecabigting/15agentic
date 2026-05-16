from pydantic import BaseModel


class IngestRequest(BaseModel):
    documents: list[str]
    metadata: dict = {}


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3


class RunRequest(BaseModel):
    task: str


class ToolCall(BaseModel):
    tool: str
    input: dict
    output: str


class RunResponse(BaseModel):
    result: str
    tool_calls: list[ToolCall]
