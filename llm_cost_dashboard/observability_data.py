import json
import csv
from pathlib import Path

MOCK_DIR = Path(__file__).parent / "mock_data"

def get_llm_usage_summary(start_date: str = None, end_date: str = None) -> dict:
    with open(MOCK_DIR / "mock_llm_usage_summary.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_llm_usage_raw(start_date: str = None, end_date: str = None) -> list:
    rows = []
    with open(MOCK_DIR / "llm_usage_raw.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            if start_date and r["created_at"][:10] < start_date:
                continue
            if end_date and r["created_at"][:10] > end_date:
                continue
            rows.append(r)
    return rows