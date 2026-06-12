import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

class WebSearchService:

    def __init__(self):

        self.client=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    def search(self,query,max_result=5):

        response = self.client.search(query=query,max_results=max_result)

        return response["results"]

web_search_service = (WebSearchService())
