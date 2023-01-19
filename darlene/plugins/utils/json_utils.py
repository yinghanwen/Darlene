import ujson as json
from pathlib import Path

JSON_DEFAULT_PATH = Path(".") / "data"

class JsonUtils:
    
    def __init__(self) -> None:
        pass

    @staticmethod
    def open_json(json_path: str, mode: str):
        with open(json_path, mode) as f:
            yield json.load(f) if 'r' in mode else f

    @staticmethod
    def read_json(json_path: str) -> dict:
        with JsonUtils.open_json(json_path, 'r') as f:
            return f

    @staticmethod
    def write_json(json_path: str, data: dict):
        with JsonUtils.open_json(json_path, 'w') as f:
            json.dump(data, f)
