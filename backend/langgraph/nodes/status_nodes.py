def accepted_node(
    state
):

    state["status"] = (
        "accepted"
    )

    return state


def retrieved_again_node(
    state
):

    state["status"] = (
        "retrieved_again"
    )

    return state


def web_corrected_node(
    state
):

    state["status"] = (
        "web_corrected"
    )

    return state


def knowledge_gap_node(
    state
):

    state["status"] = (
        "knowledge_gap"
    )

    return state