from langchain_core.tools import tool
from pydantic import BaseModel


class CalculatorInput(BaseModel):
    """MATH Expression to evaluate, e.g. '2 + 2' or '37000000 / 1000'"""

    expression: str


@tool(args_schema=CalculatorInput)
async def calculator(expression: str) -> str:
    """Evaluate a mathematical expression. Supports +, -, *, /, **, and parentheses."""
    import math

    safe_dict = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    result = eval(expression, {"__builtins__": {}}, safe_dict)
    return str(result)
