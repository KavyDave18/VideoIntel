import os

from dotenv import load_dotenv
from google import genai
from openai import OpenAI

load_dotenv()


class LLMService:

    def __init__(self):

        self.provider = os.getenv(
            "LLM_PROVIDER",
            "gemini"
        )

        if self.provider == "gemini":

            self.gemini_client = (
                genai.Client(
                    api_key=os.getenv(
                        "GEMINI_API_KEY"
                    )
                )
            )

        elif self.provider == "openrouter":

            self.openrouter_client = (
                OpenAI(
                    api_key=os.getenv(
                        "OPENROUTER_API_KEY"
                    ),
                    base_url=
                    "https://openrouter.ai/api/v1"
                )
            )

        else:

            raise ValueError(
                f"Unsupported provider: "
                f"{self.provider}"
            )

    def generate(
        self,
        prompt,
        model=None
    ):

        try:

            if self.provider == "gemini":

                if model is None:

                    model = (
                        "gemini-2.5-flash"
                    )

                response = (
                    self.gemini_client
                    .models
                    .generate_content(
                        model=model,
                        contents=prompt
                    )
                )

                return (
                    response.text
                    .strip()
                )

            elif self.provider == "openrouter":

                if model is None:

                    model = os.getenv(
                        "OPENROUTER_MODEL",
                        "deepseek/deepseek-r1-0528:free"
                    )

                response = (
                    self.openrouter_client
                    .chat
                    .completions
                    .create(

                        model=model,

                        max_tokens=512,

                        temperature=0,

                        messages=[

                            {
                                "role":
                                "user",

                                "content":
                                prompt
                            }

                        ]

                    )
                )

                return (
                    response
                    .choices[0]
                    .message
                    .content
                    .strip()
                )

        except Exception as e:

            print()

            print(
                f"LLM Error: {e}"
            )

            print()

            return None


llm_service = (
    LLMService()
)