from backend.services.evidence_evaluator_service import (
    evidence_evaluator_service
)


def evaluate_evidence_node(
    state
):

    query = (
        state["query"]
    )

    web_results = (
        state[
            "web_results"
        ]
    )

    evaluation = (
        evidence_evaluator_service.evaluate(
            query=query,
            web_results=web_results
        )
    )

    state[
        "evidence_evaluation"
    ] = evaluation

    return state