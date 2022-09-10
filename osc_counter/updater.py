from contact import Contact
from os.path import exists
from filemanager  import FileManager

class Updater():

    def __init__(self) -> None:
        self.file_manager = FileManager()

    def check_for_updates(self) -> None:
        if not exists('tracker.json'):
            self.create_tracker()

        tracker = self.file_manager.get_tracker()
        if(len(tracker) > 0):
            self.update_tracker(tracker)
        print("tracker.json is up to date.")

    # Checks for each property in the first key from tracker.json
    # adds any missing properties to all contacts 
    # with the default values those properties would instantiate with
    def update_tracker(self, tracker: dict) -> None:
        contact = Contact('UPDATER')
        serialized_contact = contact.serializable_data()

        for prop in serialized_contact:
            if not prop in tracker[next(iter(tracker))].keys():
                print(f"Adding {prop} to each contact.")

                for contact_name in tracker:
                    tracker[contact_name][prop] = serialized_contact[prop] 
            self.file_manager.dump_tracker(tracker)

    def  create_tracker(self) -> None:
        with open('tracker.json', 'w') as f:
            tracker = {}
            self.file_manager.dump_tracker(tracker)
            print("Tracker is created")
