from langchain_openai import ChatOpenAI

from jupyter_ai_magics import BaseProvider
from jupyter_ai_magics.providers import EnvAuthStrategy, TextField


class CBorgProvider(BaseProvider, ChatOpenAI):
    id = "cborg"
    name = "CBorg"
    # https://cborg.lbl.gov/models/
    models = [
        "lbl/cborg-chat:latest",  # LBL-hosted Llama 405B with custom system prompt
        "lbl/cborg-coder:latest",  # LBL-hosted Llama 405B with custom system prompt
        "lbl/cborg-vision:latest",  # LBL-hosted Llama 405B with custom system prompt
        "lbl/llama",  # LBL-hosted Llama 405B Chat model
        "lbl/llama-vision",  # LBL-hosted Llama 90B Vision model
        "openai/gpt-4o",
        "openai/gpt-4o-mini",
        "openai/o1",
        "openai/o1-mini",
        "anthropic/claude-haiku",
        "anthropic/claude-sonnet",
        "anthropic/claude-opus",
        "google/gemini-pro",
        "google/gemini-flash",
        "aws/llama-3.1-405b",
        "aws/llama-3.1-70b",
        "aws/llama-3.1-8b",
        "aws/command-r-plus-v1",
        "aws/command-r-v1"
    ]

    model_id_key = "model_name"
    pypi_package_deps = ["langchain_openai"]
    auth_strategy = EnvAuthStrategy(name="CBORG_API_KEY")

    fields = [
        TextField(
            key="openai_api_base", label="CBorg Base API URL (optional)", format="text",
        ),
    ]

    def __init__(self, **kwargs):
        cborg_api_key = kwargs.pop("cborg_api_key", None)
        cborg_api_base = kwargs.pop(
            "openai_api_base", "https://api.cborg.lbl.gov"
        )

        super().__init__(
            openai_api_key=cborg_api_key,
            openai_api_base=cborg_api_base,
            **kwargs,
        )

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an CBorg API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


