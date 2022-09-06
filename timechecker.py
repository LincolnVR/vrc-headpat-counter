from datetime import datetime

class TimeChecker:

    def __init__(self, interval = 3):
       self.interval_timer = interval
       self.last_change = datetime.now()

    def enough_time_passed(self) -> bool:
        current_time = datetime.now()
        delta = current_time.timestamp()- self.last_change.timestamp()
        return delta >= self.interval_timer

    def update_last_change(self) -> None:
        self.last_change = datetime.now()
