import json
from datetime import datetime

class UserSettings:

    def __init__(self) -> None:
        self.config: dict = self.get_config()
        self.param_persistance: int = self.force_minimum(self.config['ParamPersistance'], 1)

    def force_minimum(self, num_val: int, minimum: int) -> int:
        return minimum if num_val < minimum else num_val

    def is_past_delay(self, contact: dict) -> bool:
        current_time = datetime.now().timestamp()
        delta = current_time - contact['last_activated']
        return True if delta > contact['frequency_limit'] else False
         

    def get_config(self) -> dict:
        with open("config.json", "r") as jsonFile:
            config = json.load(jsonFile)
        return config