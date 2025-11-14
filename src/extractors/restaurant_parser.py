thonpython
import logging

class RestaurantParser:
    """
    Converts search results into structured restaurant metadata.
    """

    def parse(self, search_results: dict):
        logging.info("Parsing restaurant metadata.")

        restaurants = []
        for entry in search_results.get("restaurants", []):
            restaurants.append({
                "restaurantId": entry["id"],
                "name": entry["name"],
                "attributes": ["default"],
            })

        return restaurants