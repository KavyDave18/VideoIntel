from langgraph.graph import (
    StateGraph,
    END
)

from backend.langgraph.state import (
    GraphState
)

from backend.langgraph.nodes.retrieve_node import (
    retrieve_node
)

from backend.langgraph.nodes.evaluate_retrieval_node import (
    evaluate_retrieval_node
)

from backend.langgraph.nodes.rewrite_query_node import (
    rewrite_query_node
)

from backend.langgraph.nodes.retrieve_rewritten_node import (
    retrieve_rewritten_node
)

from backend.langgraph.nodes.web_search_node import (
    web_search_node
)

from backend.langgraph.nodes.evaluate_evidence_node import (
    evaluate_evidence_node
)

from backend.langgraph.nodes.status_nodes import (
    accepted_node,
    retrieved_again_node,
    web_corrected_node,
    knowledge_gap_node
)


def retrieval_router(
    state
):

    evaluation = (
        state[
            "retrieval_evaluation"
        ]
    )

    if evaluation.get(
        "sufficient",
        False
    ):

        return "accepted"

    return "rewrite_query"


def second_retrieval_router(
    state
):

    evaluation = (
        state[
            "retrieval_evaluation"
        ]
    )

    if evaluation.get(
        "sufficient",
        False
    ):

        return "retrieved_again"

    return "web_search"


def evidence_router(
    state
):

    evaluation = (
        state[
            "evidence_evaluation"
        ]
    )

    if evaluation.get(
        "sufficient",
        False
    ):

        return "web_corrected"

    return "knowledge_gap"


graph_builder = (
    StateGraph(
        GraphState
    )
)

# ==================================================
# MAIN NODES
# ==================================================

graph_builder.add_node(
    "retrieve",
    retrieve_node
)

graph_builder.add_node(
    "evaluate_retrieval",
    evaluate_retrieval_node
)

graph_builder.add_node(
    "rewrite_query",
    rewrite_query_node
)

graph_builder.add_node(
    "retrieve_rewritten",
    retrieve_rewritten_node
)

graph_builder.add_node(
    "evaluate_retrieval_again",
    evaluate_retrieval_node
)

graph_builder.add_node(
    "web_search",
    web_search_node
)

graph_builder.add_node(
    "evaluate_evidence",
    evaluate_evidence_node
)

# ==================================================
# STATUS NODES
# ==================================================

graph_builder.add_node(
    "accepted",
    accepted_node
)

graph_builder.add_node(
    "retrieved_again",
    retrieved_again_node
)

graph_builder.add_node(
    "web_corrected",
    web_corrected_node
)

graph_builder.add_node(
    "knowledge_gap",
    knowledge_gap_node
)

# ==================================================
# ENTRY POINT
# ==================================================

graph_builder.set_entry_point(
    "retrieve"
)

# ==================================================
# RETRIEVAL PATH
# ==================================================

graph_builder.add_edge(
    "retrieve",
    "evaluate_retrieval"
)

graph_builder.add_conditional_edges(
    "evaluate_retrieval",
    retrieval_router
)

# ==================================================
# REWRITE PATH
# ==================================================

graph_builder.add_edge(
    "rewrite_query",
    "retrieve_rewritten"
)

graph_builder.add_edge(
    "retrieve_rewritten",
    "evaluate_retrieval_again"
)

graph_builder.add_conditional_edges(
    "evaluate_retrieval_again",
    second_retrieval_router
)

# ==================================================
# WEB SEARCH PATH
# ==================================================

graph_builder.add_edge(
    "web_search",
    "evaluate_evidence"
)

graph_builder.add_conditional_edges(
    "evaluate_evidence",
    evidence_router
)

# ==================================================
# TERMINAL NODES
# ==================================================

graph_builder.add_edge(
    "accepted",
    END
)

graph_builder.add_edge(
    "retrieved_again",
    END
)

graph_builder.add_edge(
    "web_corrected",
    END
)

graph_builder.add_edge(
    "knowledge_gap",
    END
)

# ==================================================
# COMPILE
# ==================================================

graph = (
    graph_builder.compile()
)