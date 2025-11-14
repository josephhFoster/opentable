thonpython
import logging

class SearchParser:
    """
    Simulates parsing OpenTable search results.
    """

    def parse(self, query: str):
        logging.info(f"Parsing search for: {query}")

        return {
            "query": query,
            "matchedLocation": f"Location match for {query}",
            "restaurants": [
                {"id": 1001, "name": "Sample Restaurant A"},
                {"id": 1002, "name": "Sample Restaurant B"},
            ],
        }