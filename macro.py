import pyautogui
import threading
import time
import keyboard
from datetime import datetime, timedelta
import pytz # For timezone handling
import autoit   # Direct input automations

buyPadding = 0

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
            autoit.win_activate("Roblox")
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

            # if run < (self.runCount):
            #     self.switchTabs()

    # TODO: Actually create the macros according to each seed setting
    def executeMacro(self):
        autoit.mouse_click("left", 851,192, 2)


        if self.seed_data.get("SeedShop") > 0:
            self.regSeedMacro()

        # if self.seed_data.get("GearShop") > 0:
        #     self.gearShopMacro()

        # if self.seed_data.get("BloodMoonShop") > 0:
        #     self.eggShopMacro()
        # if self.seed_data.get("EggShop") > 0:
        #     self.bloodMoonShop()

    def regSeedMacro(self): # waitTm = .5, clickWait = 1, moveSpeed = 0.5
        print("RegularSeeds")
        autoit.send("e")
        time.sleep(3)

        # Click for the seed (1010, 935) 
        # To close the buy (1770, 400)
        if self.seed_data.get("Carrot", False):
            autoit.mouse_click("left", 919, 677, 1)
            time.sleep(1.5)
            autoit.mouse_click("left", 1002, 939, 20) 
            time.sleep(1.5)
            autoit.mouse_click("left", 919, 677, 1)

        # Scrolls y + 40
        if self.seed_data.get("Strawberry", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 565)
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 565)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("Blueberry", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 605) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 605) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("OrangeTulip", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 645) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 645) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("TomatoSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 685) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 685) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("CornSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 725) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 725) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("WatermelonSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 765) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 765) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")
        
        # Scrolls y + 40
        if self.seed_data.get("PumpkinSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 805) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 805) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("AppleSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 845) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 845) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")
            
         # Scrolls y + 40
        if self.seed_data.get("BambooSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 885) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 885) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")
            
            # Scrolls y + 40
        if self.seed_data.get("CoconutSeed", False):
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 925) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 925) # Update to new fruit
            time.sleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            time.sleep(1.2)
            autoit.mouse_up("left")
            

    # def gearShopMacro(self):


    # def eggShopMacro(self):


    # def bloodMoonShop(self):

    def shopBuy(self):
        global buyPadding
        autoit.mouse_click("left", 920, 675 + buyPadding, 1)
        time.sleep(1.5)
        autoit.mouse_click("left", 1000, 950 + buyPadding, 20) 
        time.sleep(1.5)
        autoit.mouse_click("left", 920, 675 + buyPadding, 1)
        buyPadding += 5



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




