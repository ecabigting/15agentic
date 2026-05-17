from urllib.parse import quote
import httpx
from langchain_core.tools import tool
from pydantic import BaseModel


class WebSearchInput(BaseModel):
    """Search query string"""

    query: str


@tool(args_schema=WebSearchInput)
async def web_search(query: str) -> str:
    url = f"https://api.duckduckgo.com/?q={quote(query)}&format=json&no_html=1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        abstract = data.get("AbstractText", "")
        topics = data.get("RelatedTopics", [])[:3]
        output = f"Summary: {abstract}\n\n"
        for i, topic in enumerate(topics, start=1):
            text = topic.get("Text", "")
            url = topic.get("FirstURL", "")
            output += f"{i}. {text}\n   {url}\n"
    return output
