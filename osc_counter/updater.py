from contact import Contact
from filemanager  import FileManager

class Updater():

    def __init__(self) -> None:
        self.file_manager = FileManager()

    def auto_update_tracker(self) -> None:
        tracker = self.file_manager.get_tracker()
        if(len(tracker) > 0):
            self.execute_checker(tracker)
        print("tracker.json is up to date.")

    # checks for each property in the first key from tracker.json
    # adds any missing properties with the default values those properties would instantiate with
    def execute_checker(self, tracker: dict) -> None:
        contact = Contact('UPDATER')
        serialized_contact = contact.serializable_data()
        for prop in serialized_contact:
            if not prop in tracker[next(iter(tracker))].keys():
                print(f"Adding {prop} to each contact.")
                for contact_name in tracker:
                    tracker[contact_name][prop] = serialized_contact[prop] 
            self.file_manager.dump_tracker(tracker)