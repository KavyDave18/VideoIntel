from backend.evaluation.retrieval_metrics import recall_at_k,precision_at_k
from dataset.evaluation_queries import EVALUATION_DATASET
from backend.services.reranked_search_service import reranked_search_service

all_recalls = []
all_precisions = []

for item in EVALUATION_DATASET:

    query = item["query"]
    relevant_ids = (item["relevant_video_ids"])

    results = (
        reranked_search_service.search(
            query=query,
            final_limit = 5,
        )
    )

    retrival_ids = [
        result["result"]["video_id"] for result in results
    ]

    recall=recall_at_k(retrival_ids,relevant_ids)
    precision = precision_at_k(retrival_ids,relevant_ids)

    all_recalls.append(recall)
    all_precisions.append(precision)

    print()

    print(
        f"Query: {query}"
    )

    print(
        f"Recall@5: {recall:.2f}"
    )

    print(
        f"Precision@5: {precision:.2f}"
    )

avg_recall = (
    sum(all_recalls)
    /
    len(all_recalls)
)

avg_precision = (
    sum(all_precisions)
    /
    len(all_precisions)
)

print()
print("=" * 60)

print(
    f"Average Recall@5: {avg_recall:.3f}"
)

print(
    f"Average Precision@5: {avg_precision:.3f}"
)


    