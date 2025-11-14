thonpython
import logging
from datetime import datetime, timedelta

class AvailabilityParser:
    """
    Returns mock reservation slots for each restaurant.
    """

    def parse(self, restaurants):
        logging.info("Parsing availability for restaurants.")

        results = []

        for restaurant in restaurants:
            now = datetime.now()
            slots = []

            for i in range(5):
                time = (now + timedelta(minutes=30 * i)).strftime("%H:%M")
                slots.append({
                    "isAvailable": True,
                    "availableAt": time,
                    "link": f"https://www.opentable.com/booking/{restaurant['restaurantId']}/{time}",
                    "pointsValue": 100,
                    "slotHash": f"HASH-{restaurant['restaurantId']}-{i}",
                })

            results.append({
                "name": restaurant["name"],
                "restaurantId": restaurant["restaurantId"],
                "slots": slots,
                "summary": [{"availableAt": slot["availableAt"], "link": slot["link"]} for slot in slots],
            })

        return results