from backend.services.query_rewriter_service import query_rewriter_service

def rewrite_query_node(state):

    query = (state["query"])

    rewritten_query = (query_rewriter_service.rewrite(query=query))

    state["rewritten_queries"] = rewritten_query

    return state
