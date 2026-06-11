from backend.services.reranker_service import (
    reranker_service
)

query = (
    "How does self attention work in transformers?"
)

chunks = [

    "What is self attention in transformers?",

    "Cricket world cup final highlights",

    "Multi head attention improves contextual understanding",

    "How to cook pasta"
]

results = (
    reranker_service.rerank(
        query=query,
        chunks=chunks
    )
)

for text, score in results:

    print()
    print(score)
    print(text)
    print("-" * 80)