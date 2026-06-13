import time
from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from backend.langgraph.graph import (
    graph
)


router = APIRouter()


class SearchRequest(
    BaseModel
):

    query: str


@router.post(
    "/search"
)
def search(
    request: SearchRequest
):

    print()
    print("=" * 50)
    print("SEARCH REQUEST RECEIVED")
    print(request.query)
    print("=" * 50)
    print()

    state = {

        "query":
        request.query,

        "rewritten_queries":
        [],

        "video_results":
        [],

        "web_results":
        [],

        "retrieval_evaluation":
        {},

        "evidence_evaluation":
        {},

        "status":
        ""

    }

    start = time.time()

    result = graph.invoke(state)

    print(
        f"GRAPH TIME: "
        f"{time.time() - start:.2f}s"
    )

    return result