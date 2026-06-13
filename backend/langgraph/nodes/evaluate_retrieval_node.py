from backend.services.retrieval_evaluator_service import (
    retrieval_evaluator_service
)


def evaluate_retrieval_node(
    state
):

    query = (
        state["query"]
    )

    results = (
        state["video_results"]
    )

    evaluation = (
        retrieval_evaluator_service.evaluate(
            query=query,
            results=results
        )
    )

    state[
        "retrieval_evaluation"
    ] = evaluation

    return state