from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    google_api_key: str = ""
    model_config = {"env_file": ".env"}
    llm_model: str = "gemini-2.5-flash"
    host: str = "0.0.0.0"
    port: int = 8989


settings = Settings()
