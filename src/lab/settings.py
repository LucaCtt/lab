from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings, loaded from environment variables or .env file in the project root."""

    # LiteLLM API settings. 
    litellm_base_url: str = "http://10.20.25.121:4000/v1"
    litellm_api_key: str | None = None # Remember to set this in your .env file or environment variables!

    # Model settings. These are the defaults recommended here: https://huggingface.co/Qwen/Qwen3.5-9B#best-practices
    model: str = "openai/qwen-3.5-instruct"
    max_tokens: int = 32768
    temperature: float = 0.7
    top_p: float = 0.8
    top_k: int = 20
    presence_penalty: float = 2.0
    repetition_penalty: float = 1.0