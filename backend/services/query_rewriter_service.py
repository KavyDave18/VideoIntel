class QueryRewriterService:

    def __init__(self):

        self.rewrites = {

            "transformers":
            "transformer architecture",

            "attention":
            "attention mechanism",

            "kohli batting":
            "virat kohli batting",

            "neural nets":
            "neural networks",

            "llm":
            "large language model",

            "gpt":
            "gpt transformer architecture"

        }

    def rewrite(
        self,
        query
    ):

        return (
            self.rewrites.get(
                query.lower(),
                query
            )
        )


query_rewriter_service = (
    QueryRewriterService()
)