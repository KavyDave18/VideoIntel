from dataset.evaluation_queries import (
    EVALUATION_DATASET
)

from backend.services.hybrid_search_service import (
    hybrid_search_service
)

from backend.services.reranked_search_service import (
    reranked_search_service
)

from backend.evaluation.retrieval_metrics import (
    recall_at_k,
    precision_at_k
)

from backend.evaluation.mrr import (
    reciprocal_rank
)

from backend.evaluation.ndcg import (
    ndcg
)

# =====================================
# HYBRID
# =====================================

hybrid_recalls = []
hybrid_precisions = []
hybrid_mrrs = []
hybrid_ndcgs = []

# =====================================
# RERANKED
# =====================================

rerank_recalls = []
rerank_precisions = []
rerank_mrrs = []
rerank_ndcgs = []

for item in EVALUATION_DATASET:

    query = item["query"]

    relevant_ids = (
        item["relevant_video_ids"]
    )

    # ==========================
    # HYBRID
    # ==========================

    hybrid_results = (
        hybrid_search_service.search(
            query=query,
            limit=5,
            candidate_limit=50
        )
    )

    hybrid_ids = [

        result["result"]["video_id"]

        for result
        in hybrid_results
    ]

    hybrid_recalls.append(
        recall_at_k(
            hybrid_ids,
            relevant_ids
        )
    )

    hybrid_precisions.append(
        precision_at_k(
            hybrid_ids,
            relevant_ids
        )
    )

    hybrid_mrrs.append(
        reciprocal_rank(
            hybrid_ids,
            relevant_ids
        )
    )

    hybrid_ndcgs.append(
        ndcg(
            hybrid_ids,
            relevant_ids
        )
    )

    # ==========================
    # RERANKED
    # ==========================

    reranked_results = (
        reranked_search_service.search(
            query=query,
            final_limit=5
        )
    )

    reranked_ids = [

        result["result"]["video_id"]

        for result
        in reranked_results
    ]

    rerank_recalls.append(
        recall_at_k(
            reranked_ids,
            relevant_ids
        )
    )

    rerank_precisions.append(
        precision_at_k(
            reranked_ids,
            relevant_ids
        )
    )

    rerank_mrrs.append(
        reciprocal_rank(
            reranked_ids,
            relevant_ids
        )
    )

    rerank_ndcgs.append(
        ndcg(
            reranked_ids,
            relevant_ids
        )
    )

# =====================================
# AVERAGES
# =====================================

avg_hybrid_recall = (
    sum(hybrid_recalls)
    /
    len(hybrid_recalls)
)

avg_hybrid_precision = (
    sum(hybrid_precisions)
    /
    len(hybrid_precisions)
)

avg_hybrid_mrr = (
    sum(hybrid_mrrs)
    /
    len(hybrid_mrrs)
)

avg_hybrid_ndcg = (
    sum(hybrid_ndcgs)
    /
    len(hybrid_ndcgs)
)

avg_rerank_recall = (
    sum(rerank_recalls)
    /
    len(rerank_recalls)
)

avg_rerank_precision = (
    sum(rerank_precisions)
    /
    len(rerank_precisions)
)

avg_rerank_mrr = (
    sum(rerank_mrrs)
    /
    len(rerank_mrrs)
)

avg_rerank_ndcg = (
    sum(rerank_ndcgs)
    /
    len(rerank_ndcgs)
)

print()
print("=" * 60)
print("HYBRID SEARCH")
print("=" * 60)

print(
    f"Recall@5    : {avg_hybrid_recall:.3f}"
)

print(
    f"Precision@5 : {avg_hybrid_precision:.3f}"
)

print(
    f"MRR@5       : {avg_hybrid_mrr:.3f}"
)

print(
    f"nDCG@5      : {avg_hybrid_ndcg:.3f}"
)

print()
print("=" * 60)
print("HYBRID + RERANKER")
print("=" * 60)

print(
    f"Recall@5    : {avg_rerank_recall:.3f}"
)

print(
    f"Precision@5 : {avg_rerank_precision:.3f}"
)

print(
    f"MRR@5       : {avg_rerank_mrr:.3f}"
)

print(
    f"nDCG@5      : {avg_rerank_ndcg:.3f}"
)