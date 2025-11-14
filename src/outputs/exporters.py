thonpython
import json
import logging
from pathlib import Path

class JSONExporter:
    @staticmethod
    def export(data, path: Path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logging.info(f"JSON exported successfully to {path}")
        except Exception as e:
            logging.error(f"Failed to export JSON: {e}")