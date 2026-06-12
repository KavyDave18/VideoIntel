from backend.services.web_search_service import (web_seach_service)

results = web_seach_service.search("latest gpt version release")

for result in results:
    print()
    print("=" * 80)

    print(
        result["title"]
    )

    print()

    print(
        result["url"]
    )

    print()

    print(
        result["content"][:300]
    )

    