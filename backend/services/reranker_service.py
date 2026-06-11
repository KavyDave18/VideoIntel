from sentence_transformers import CrossEncoder

class RankerServices:

    def __init__(self):
        self.model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

    def rerank(self,query,chunks):

        pairs = [(query,chunk) for chunk in chunks]

        score = self.model.predict(pairs)

        result = list(zip(chunks,score))

        result.sort(key = lambda x:x[1],
                    reverse=True)

        return result

reranker_service = (RankerServices())
