from dataset.evaluation_queries import (
    EVALUATION_DATASET
)

from backend.services.reranked_search_service import (
    reranked_search_service
)

from backend.evaluation.mrr import (
    reciprocal_rank
)

all_rr = []

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

    rr = reciprocal_rank(
        retrieved_ids,
        relevant_ids
    )

    all_rr.append(rr)

    print()

    print(
        f"Query: {query}"
    )

    print(
        f"Reciprocal Rank: {rr:.3f}"
    )

mrr = (
    sum(all_rr)
    /
    len(all_rr)
)

print()
print("=" * 60)

print(
    f"MRR@5: {mrr:.3f}"
)