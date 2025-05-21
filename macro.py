import pyautogui
import threading
import time
import keyboard
from datetime import datetime, timedelta
import pytz # For timezone handling

class Macro():
    def __init__(self, seed_data, runCount,):
        self.seed_data = seed_data  # Store the seeds dictionary
        self.runCount = runCount
        self.is_running = False
        self.thread = None
        self.est = pytz.timezone("US/Eastern")

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.mainLoop, daemon=True)
            self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1)
    
    # Handles controling loop: starting, number of iterations, controlling the time
    def mainLoop(self):
        while self.is_running is not False:
            self.runMacroCycle()
            self.waitUntilNextInterval()

    # needs to repeat number of runCount times each time it finishes it alt tabes once
        # Could use alt + shift + tab to reverse through tabs in order which could work
    def runMacroCycle(self):
        for run in range(self.runCount):
            if not self.is_running:
                break

            print(f"Starting run {run + 1}/{self.runCount}")
            self.executeMacro()

            if run < (self.runCount):
                self.switchTabs()
                
    # TODO: Actually create the macros according to each seed setting
    def executeMacro(self):
        time.sleep(3)
        print(pyautogui.position()) # Needs to be at x=851, y=192

        if self.seed_data.get("Carrot", False):
            print("Collecting Carrot Seeds")

        if self.seed_data.get("Strawberry", False):
            print("Collecting Strawberry Seeds")

    def switchTabs(self):
            keyboard.press_and_release("alt + shift + tab")
            time.sleep(0.5)
            print("Switched to next tab")

    # Calculates time based on local time, or time zone in intervals of 5
    def waitUntilNextInterval(self):
        if not self.is_running:
            return

        now = datetime.now() # now = datetime.now(self.est)
        nextRun = now + timedelta(minutes=5)
        nextRun = nextRun.replace(second=0, microsecond=0)

        if now.minute % 5 == 0:
            nextRun += timedelta(minutes=5)

        wait_seconds = (nextRun - now).total_seconds()

        while wait_seconds > 0 and self.is_running:
            time.sleep(min(1, wait_seconds))
            wait_seconds-=1




