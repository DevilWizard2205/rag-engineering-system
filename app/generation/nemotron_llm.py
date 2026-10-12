import os

from dotenv import load_dotenv
from openai import OpenAI

from app.generation.llm import LLM


class NemotronLLM(LLM):
    def __init__(
        self,
        model_name: str = "nvidia/nemotron-3.5-lightning-30b-a3b",
        temperature: float = 0.2,
        max_tokens: int = 2048,
    ):
        load_dotenv()

        api_key = os.getenv("NVIDIA_API_KEY")

        if not api_key:
            raise ValueError("NVIDIA_API_KEY is not set in the environment.")

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key,
        )

        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        return response.choices[0].message.content