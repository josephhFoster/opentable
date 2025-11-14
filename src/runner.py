thonpython
import json
import logging
from pathlib import Path
from extractors.search_parser import SearchParser
from extractors.restaurant_parser import RestaurantParser
from extractors.availability_parser import AvailabilityParser
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    logging.info("Runner started.")

    data_dir = Path(__file__).resolve().parent.parent / "data"
    sample_input = data_dir / "sample_input.txt"

    if not sample_input.exists():
        logging.error("sample_input.txt not found.")
        return

    query = sample_input.read_text().strip()
    logging.info(f"Loaded query: {query}")

    search_parser = SearchParser()
    restaurant_parser = RestaurantParser()
    availability_parser = AvailabilityParser()

    search_results = search_parser.parse(query)
    logging.info("Search results parsed.")

    restaurants = restaurant_parser.parse(search_results)
    logging.info("Restaurant metadata collected.")

    availability = availability_parser.parse(restaurants)
    logging.info("Availability extracted.")

    output_path = data_dir / "sample_output.json"
    JSONExporter.export(availability, output_path)
    logging.info(f"Exported result to {output_path}")

if __name__ == "__main__":
    main()