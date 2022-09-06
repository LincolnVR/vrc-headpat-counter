from datetime import datetime
import json

class FileManager:

    # Increases the current count of a given contact locally in the JSON file
    def add_contact(self, contact_name: str) -> None:
        tracker = self.get_tracker()
        tracker[contact_name]['current_count'] = tracker[contact_name]['current_count']+1

        with open("tracker.json", "w") as jsonFile:
            json.dump(tracker, jsonFile)

    # Sets the last count to the current count so that it can be updated in the OSC Server
    # The value in last_count is sent as a message to the OSC Server in messenger.py:format_message()
    def update_tracker(self) -> None:
        tracker = self.get_tracker()
        
        for contact_name in tracker.keys():
            current_count =  tracker[contact_name]['current_count']
            last_count = tracker[contact_name]['last_count']
            if (current_count > last_count):
                print(f"Gained {current_count - last_count} {contact_name.capitalize()}!")
                tracker[contact_name]['last_count'] = current_count

        with open("tracker.json", "w") as jsonFile:
            json.dump(tracker, jsonFile)

    # The list of keys in the tracker.json file has to be updated while running 
    # because we can't know beforehand what parameters exist for the avatar
    def does_key_exist(self, contact_name: str) -> bool:
        return contact_name in self.get_tracker().keys()

    def inject_new_contact(self, contact_name: str) -> None:
        tracker = self.get_tracker()

        tracker[contact_name] = {'current_count' : 1,'last_count' : 1}
        with open("tracker.json", "w") as jsonFile:
            json.dump(tracker, jsonFile)

    def get_tracker(self) -> dict:
        with open("tracker.json", "r") as jsonFile:
            tracker = json.load(jsonFile)

        return tracker



        
        
        

        

