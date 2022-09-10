from datetime import datetime

class Contact:

    def __init__(self, name):
        self.name = name
        self.current_count = 1
        self.last_count = 1
        self.last_activated = datetime.now()
        self.frequency_limit = 0

    def serializable_data(self) -> dict:
        data = {
            "current_count" : self.current_count,
            "last_count" : self.last_count,
            "last_activated" : self.last_activated.timestamp(),
            "frequency_limit" : self.frequency_limit
        }
  
        return data