from fastapi import FastAPI

from agent_service.models.schemas import IngestRequest

app = FastAPI()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/ingest")
async def ingest(request: IngestRequest):
    return {"recieved": len(request.documents)}
