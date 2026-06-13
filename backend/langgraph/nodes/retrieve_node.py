from backend.services.reranked_search_service import reranked_search_service

def retrieve_node(state):

    query = (state["query"])

    category = (state.get("category"))

    results = (reranked_search_service.search(query=query,category=category))

    state["video_results"]=results

    return state