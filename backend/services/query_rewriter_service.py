import json

from backend.services.llm_service import (
    llm_service
)


class QueryRewriterService:

    def rewrite(
        self,
        query
    ):

        prompt = f"""
You are an expert search query rewriting system.

User Query:
{query}

Generate 5 alternative search queries that
could improve retrieval quality.

Rules:

1. Keep queries short.
2. Expand abbreviations.
3. Include related concepts.
4. Preserve original intent.
5. Do not explain.
6. Return JSON only.

Example:

{{
    "queries": [
        "transformer architecture",
        "self attention mechanism",
        "multi head attention",
        "positional encoding",
        "encoder decoder architecture"
    ]
}}
"""

        response = (
            llm_service.generate(
                prompt
            )
        )

        if response is None:

            return [
                query
            ]

        try:

            cleaned_response = (

                response

                .replace(
                    "```json",
                    ""
                )

                .replace(
                    "```",
                    ""
                )

                .strip()

            )

            data = json.loads(
                cleaned_response
            )

            rewritten_queries = (
                data.get(
                    "queries",
                    []
                )
            )

            final_queries = [
                query
            ]

            for rewritten_query in rewritten_queries:

                if (
                    rewritten_query
                    and
                    rewritten_query
                    not in final_queries
                ):

                    final_queries.append(
                        rewritten_query
                    )

            return final_queries

        except Exception:

            return [
                query
            ]


query_rewriter_service = (
    QueryRewriterService()
)