import pyautogui
import time

class Macro():
    def __init__(self, seed_data, runCount, bool = False):
        self.seed_data = seed_data  # Store the seeds dictionary
        self.macroCounter = runCount
        self.counter = bool

    def run(self):
        self.start()

        # if self.seed_data.get("Carrot", False):
        #     self.carrotCollect()

        # if self.seed_data.get("Strawberry", False):
        #     self.strawberryCollect()

    def start(self):
        time.sleep(3)
        print(pyautogui.position())

    # def carrotCollect():
    #     print()
    
    # def strawberryCollect():
    #     print()



