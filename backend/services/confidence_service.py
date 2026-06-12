class ConfidenceService:

    def analyze(
        self,
        results
    ):

        if len(results) == 0:

            return {
                "top_score": 0,
                "second_score": 0,
                "score_gap": 0,
                "is_confident": False
            }

        top_score = (
            results[0]["rerank_score"]
        )

        second_score = (
            results[1]["rerank_score"]
            if len(results) > 1
            else 0
        )

        score_gap = (
            top_score -
            second_score
        )

        is_confident = False

        # ---------------------------------
        # TEMPORARY PHASE 10 LOGIC
        # ---------------------------------

        if top_score > 1:

            is_confident = True

        elif score_gap > 1:

            is_confident = True

        return {
            "top_score": top_score,
            "second_score": second_score,
            "score_gap": score_gap,
            "is_confident": is_confident
        }

    def is_confident(
        self,
        results
    ):

        analysis = (
            self.analyze(results)
        )

        return analysis[
            "is_confident"
        ]


confidence_service = (
    ConfidenceService()
)