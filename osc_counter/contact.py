from datetime import datetime

class Contact:

    def __init__(self, name):
        self.name = name
        self.current_count = 1
        self.last_count = 1
        self.last_activated = datetime.now()

    def serializable_data(self) -> dict:
        data = {
            "current_count" : self.current_count,
            "last_count" : self.last_count,
            "last_activated" : self.last_activated.timestamp()
        }
  
        return data