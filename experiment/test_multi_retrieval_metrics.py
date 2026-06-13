from backend.services.reranked_search_service import (
    reranked_search_service
)

from experiment.reranked_multi_retrieval_service import (
    reranked_multi_retrieval_service
)

queries = [

    "world cup final highlights",
    "india australia world cup final",
    "rohit sharma batting",
    "travis head catch",
    "australia wins world cup",

    "virat kohli sixes",
    "kohli biggest six",
    "virat aggressive batting",
    "virat kohli century",
    "india sri lanka 2017",
    "match winning hundred",

    "build neural network from scratch",
    "numpy neural network",
    "forward propagation",
    "backpropagation implementation",

    "relu activation function",
    "sigmoid vs tanh",
    "activation functions deep learning",

    "self attention",
    "multi head attention",
    "transformer architecture",
    "positional encoding",
    "why transformers replaced rnn",

    "encoder decoder architecture",
    "attention mechanism",
    "machine translation",
    "seq2seq model",

    "digital electronics encoder decoder",
    "2 to 4 decoder",
    "computer organization decoder",

    "addiction is wrong",
    "sleep superpower",
    "brain scans",

    "jack ma advice",
    "joe rogan motivation",
    "oprah life lessons",
    "david goggins motivation",

    "spend time alone",
    "let go of the past"

]

print()
print("=" * 100)
print("HYBRID VS MULTI RETRIEVAL")
print("=" * 100)

for query in queries:

    hybrid_results = (
        reranked_search_service.search(
            query=query
        )
    )

    multi_results = (
        reranked_multi_retrieval_service.search(
            query=query
        )
    )

    print()
    print("-" * 100)

    print(
        f"Query: {query}"
    )

    print()

    print(
        "HYBRID + RERANKER"
    )

    if len(hybrid_results) > 0:

        top = hybrid_results[0]

        print(
            f"Score: "
            f"{top['rerank_score']:.4f}"
        )

        print(
            f"Video: "
            f"{top['result']['video_id']}"
        )

    else:

        print(
            "No Results"
        )

    print()

    print(
        "MULTI RETRIEVAL + RERANKER"
    )

    if len(multi_results) > 0:

        top = multi_results[0]

        print(
            f"Score: "
            f"{top['rerank_score']:.4f}"
        )

        print(
            f"Video: "
            f"{top['result']['result']['video_id']}"
        )

        print(
            f"Retrieved From: "
            f"{top['result']['retrieved_from']}"
        )

    else:

        print(
            "No Results"
        )

    print()
    print("-" * 100)

print()
print("=" * 100)
print("TEST COMPLETE")
print("=" * 100)
