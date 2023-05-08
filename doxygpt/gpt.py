"""
GPT API Bridge to simplify calls.
"""

from chatgpt_wrapper import OpenAIAPI
from chatgpt_wrapper.core.config import Config
from dotenv import load_dotenv
import os


class GPT:
    def __init__(self, dotenv_abs_path: str):
        load_dotenv(dotenv_abs_path)  # Get API Key from DotEnv
        self._chat = OpenAIAPI()
        self._chat.llm_class.request_timeout = 600

    def ask(self, prompt: str) -> str:
        success, response, message = self._chat.ask(prompt)
        if success:
            return response
        else:
            raise RuntimeError(message)
