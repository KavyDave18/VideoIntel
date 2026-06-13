import json

from backend.services.llm_service import (
    llm_service
)


class EvidenceEvaluatorService:

    def evaluate(
        self,
        query,
        web_results
    ):

        if not web_results:

            return {

                "sufficient": False,

                "confidence": 0,

                "reason":
                "No web evidence found."

            }

        evidence = []

        for result in web_results[:5]:

            evidence.append(

                f"""
Title:
{result.get('title', '')}

Content:
{result.get('content', '')}

URL:
{result.get('url', '')}
"""

            )

        context = "\n\n".join(
            evidence
        )

        prompt = f"""
You are an expert evidence evaluator.

Your task is to determine whether
the provided web evidence can answer
the user's query DIRECTLY and SPECIFICALLY.

IMPORTANT RULES:

1. Be strict.
2. Do not accept partially related information.
3. Do not accept generic information when
   the query asks for something specific.
4. If important entities, versions,
   names, dates, locations, products,
   or facts are missing,
   mark the evidence as insufficient.
5. Only mark sufficient when the
   web evidence directly answers
   the user's query.

User Query:
{query}

Web Evidence:
{context}

Return ONLY valid JSON.

Example:

{{
    "sufficient": true,
    "confidence": 95,
    "reason": "The web evidence directly answers the query."
}}

Example:

{{
    "sufficient": false,
    "confidence": 10,
    "reason": "The evidence is related but does not directly answer the query."
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


evidence_evaluator_service = (
    EvidenceEvaluatorService()
)