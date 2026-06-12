from dataset.evaluation_queries import (
    EVALUATION_DATASET
)

from backend.services.reranked_search_service import (
    reranked_search_service
)

from backend.evaluation.ndcg import (
    ndcg
)

scores = []

for item in EVALUATION_DATASET:

    query = item["query"]

    relevant_ids = (
        item["relevant_video_ids"]
    )

    results = (
        reranked_search_service.search(
            query=query,
            final_limit=5
        )
    )

    retrieved_ids = [

        result["result"]["video_id"]

        for result
        in results
    ]

    score = ndcg(
        retrieved_ids,
        relevant_ids
    )

    scores.append(score)

    print()

    print(
        f"Query: {query}"
    )

    print(
        f"nDCG@5: {score:.3f}"
    )

average_ndcg = (
    sum(scores)
    /
    len(scores)
)

print()
print("=" * 60)

print(
    f"Average nDCG@5: {average_ndcg:.3f}"
)