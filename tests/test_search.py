from backend.services.search_service import (
    search_service
)

results = search_service.search(
    "self attention"
)

for result in results:

    print()

    print(
        "Score:",
        result["score"]
    )

    print(
        "Video:",
        result["video_title"]
    )

    print(
        "Start:",
        result["start_time"]
    )

    print(
        "End:",
        result["end_time"]
    )

    print()

    print(
        result["chunk_text"]
    )

    print("-" * 80)