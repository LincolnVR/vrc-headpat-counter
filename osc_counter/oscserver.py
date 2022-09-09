from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc import udp_client
from filemanager import FileManager
from timechecker import TimeChecker
from messenger import Messenger
import threading

class OSCServer():
    def __init__(self, filemanager, messenger):
        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self._def_osc_dispatch)
        self.server = BlockingOSCUDPServer(("127.0.0.1", 9001), self.dispatcher)
        self.server_thread = threading.Thread(target=self._process_osc)
        self.client =  udp_client.SimpleUDPClient("127.0.0.1", 9000)
        self.filemanager: FileManager = filemanager
        self.messenger: Messenger = messenger

    def launch(self) -> None:
        self.server_thread.start()

    def shutdown(self) -> None:
        self.server.shutdown()
        self.server_thread.join()

    # Entry point from OSC Unity receiver for any contact point
    # Remember from the README that args is derived from your avatars OSC JSON file
    # Per the README these address can only be boolean
    def _def_osc_dispatch(self, address: str, *args) -> None:
        if (self.messenger.timer.enough_time_passed() and \
                self.messenger.has_new_content(tracker := self.filemanager.get_tracker())):
            self.filemanager.update_tracker()
            self.message(tracker)
            self.messenger.timer.update_last_change()

        if (args[0] == True and 'Track_' in address):
            contact_name = address.split('Track_')[-1]
            if (self.filemanager.does_key_exist(contact_name)):
                self.filemanager.add_contact(contact_name)
            else:
                self.filemanager.inject_new_contact(contact_name)

    def _process_osc(self) -> None:
        print("[OSCThread] Launching OSC server thread!")
        self.server.serve_forever()

    def message(self, tracker: dict) -> None:
        self.client.send_message("/chatbox/input", [self.messenger.format_message(tracker), True])









