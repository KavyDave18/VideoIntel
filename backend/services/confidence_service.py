class ConfidenceService:

    def is_confident(self,results):

        if len(results)==0:
            return False

        top_score = (results[0]["rerank_score"])

        if top_score>2:
            return True

        return False

confidence_services = (ConfidenceService())