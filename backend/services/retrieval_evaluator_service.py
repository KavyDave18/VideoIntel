import json

from backend.services.llm_service import (llm_service)


class RetrievalEvaluatorService:

    def evaluate(
        self,
        query,
        results
    ):

        if not results:

            return {
                "sufficient": False,

                "confidence": 0,

                "reason":
                "No retrieval results found."

            }

        chunks = []

        for result in results[:3]:

            chunks.append(

                result["result"][
                    "chunk_text"
                ]

            )

        context = "\n\n".join(
            chunks
        )

        prompt = f"""
You are an expert retrieval evaluator.

Your task is to determine whether the retrieved
chunks can answer the user's query DIRECTLY
and SPECIFICALLY.

IMPORTANT RULES:

1. Do NOT accept partially related information.
2. Do NOT accept general information when the
   query asks for something specific.
3. If important entities, versions, dates,
   names, locations, products, events,
   or facts are missing, mark insufficient.
4. Be strict.
5. Only mark sufficient when the retrieved
   chunks directly answer the query.

User Query:
{query}

Retrieved Chunks:
{context}

Return ONLY valid JSON.

Example:

{{
    "sufficient": true,
    "confidence": 95,
    "reason": "The retrieved chunks directly answer the query."
}}

Example:

{{
    "sufficient": false,
    "confidence": 10,
    "reason": "The chunks discuss GPT generally but do not contain information about GPT 5 specifically."
}}
"""

        response = (
            llm_service.generate(
                prompt
            )
        )

        if response is None:

            return {

                "sufficient": False,

                "confidence": 0,

                "reason":
                "LLM unavailable."

            }

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

            return json.loads(
                cleaned_response
            )

        except Exception:

            return {

                "sufficient": False,

                "confidence": 0,

                "reason":
                "Failed to parse LLM response."

            }


retrieval_evaluator_service = (RetrievalEvaluatorService())