from backend.services.llm_service import (
    llm_service
)

response = (
    llm_service.generate(
        "What is a transformer architecture?"
    )
)

print(response)