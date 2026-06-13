from typing import TypedDict

class GraphState(TypedDict):

    query : str

    rewritten_queries:list

    video_results:list

    web_results:list

    retrieval_evaluation:dict

    evidence_evaluation:dict

    status:str
