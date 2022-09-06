#!/usr/bin/env python3
from oscserver import OSCServer
from timechecker import TimeChecker
from filemanager import FileManager
from messenger import Messenger

def main():
    messenger_timer = TimeChecker(1.5)
    filemanager = FileManager()
    messenger = Messenger(messenger_timer)
    osc = OSCServer(filemanager, messenger)
    osc.launch()

if __name__ == "__main__":
    main()


