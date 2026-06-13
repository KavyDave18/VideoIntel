class QueryExpansionService:

    def __init__(self):

        self.expansions = {

            "transformers": [
                "transformer architecture",
                "self attention",
                "multi head attention",
                "positional encoding"
            ],

            "attention": [
                "attention mechanism",
                "self attention",
                "multi head attention"
            ],

            "llm": [
                "large language model",
                "gpt",
                "transformer architecture"
            ],

            "kohli batting": [
                "virat kohli batting",
                "virat kohli century",
                "virat kohli sixes"
            ]
        }

    def expand(self, query):

        return self.expansions.get(
            query.lower(),
            [query]
        )


query_expansion_service = (
    QueryExpansionService()
)