from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from agent_service.config import settings
from agent_service.tools.calculator import calculator
from agent_service.tools.web_search import web_search

model = ChatGoogleGenerativeAI(
    model=settings.llm_model, api_key=settings.google_api_key
)

agent = create_agent(model, tools=[calculator, web_search])
