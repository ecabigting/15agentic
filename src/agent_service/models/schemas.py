from pydantic import BaseModel


class IngestRequest(BaseModel):
    documents: list[str]
    metadata: dict = {}


class QueryRequest(BaseModel):
    question: str
    top_k: int = 3
