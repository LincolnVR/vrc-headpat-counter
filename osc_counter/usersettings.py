import json
from datetime import datetime

class UserSettings:

    def __init__(self) -> None:
        self.config: dict = self.get_config()
        self.param_persistance: int = self.config['ParamPersistance']
        self.ListeningPort: int = self.config['ListeningPort']
        self.SendingPort: int = self.config['SendingPort']
        self.IP: str() = self.config['IP']
        self.log: bool() = self.config['Log']

    def is_past_delay(self, contact: dict) -> bool:
        current_time = datetime.now().timestamp()
        delta = current_time - contact['last_activated']
        return True if delta > contact['frequency_limit'] else False
         

    def get_config(self) -> dict:
        with open("config.json", "r") as jsonFile:
            config = json.load(jsonFile)
        return config