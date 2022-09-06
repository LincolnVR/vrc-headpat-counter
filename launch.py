#!/usr/bin/env python3
from oscserver import OSCServer
from timechecker import TimeChecker
from filemanager import FileManager
from messenger import Messenger
from datetime import datetime
import json
import math

def main():
    filemanager_timer = TimeChecker(600)
    messenger_timer = TimeChecker(1.5)
    filemanager = FileManager(filemanager_timer)
    messenger = Messenger(messenger_timer)
    osc = OSCServer(filemanager, messenger)
    osc.launch()

if __name__ == "__main__":
    main()


