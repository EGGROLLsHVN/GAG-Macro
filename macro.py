import pyautogui
import threading
import time
import keyboard
from datetime import datetime, timedelta
import pytz # For timezone handling
import autoit   # Direct input automations

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

    def safeSleep(self, delay):
        """Sleep that can be interrupted by stop()"""
        for _ in range(int(delay * 10)):
            if not self.is_running:
                return
            time.sleep(0.1)    
    
    # Handles controling loop: starting, number of iterations, controlling the time
    def mainLoop(self):
        while self.is_running:
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
        if not self.is_running:
            return
        
        autoit.mouse_click("left", 851,192, 2)

        if self.seed_data.get("SeedShop") > 0 and self.is_running:
            self.regSeedMacro()

        # if self.seed_data.get("GearShop") > 0 and self.is_running:
        #     self.gearShopMacro()

        # if self.seed_data.get("BloodMoonShop") > 0 and self.is_running:
        #     self.eggShopMacro()

        # if self.seed_data.get("EggShop") > 0 and self.is_running:
        #     self.bloodMoonShop()

    def regSeedMacro(self): # waitTm = .5, clickWait = 1, moveSpeed = 0.5
        if not self.is_running:
            return
        
        print("RegularSeeds")
        autoit.send("e")
        self.safeSleep(3)

        # Click for the seed (1010, 935) 
        # To close the buy (1770, 400)
        if self.seed_data.get("Carrot", False) and self.is_running:
            autoit.mouse_click("left", 919, 677, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1002, 939, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 919, 677, 1)

        # Scrolls y + 40
        if self.seed_data.get("Strawberry", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 565)
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 565)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("Blueberry", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 605) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            self.shopBuy()
            autoit.mouse_move(1800, 605) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("OrangeTulip", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 645) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 980, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 930, 685, 1)
            # 
            autoit.mouse_move(1800, 645) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("TomatoSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 685) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1000, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 685) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Scrolls y + 40
        if self.seed_data.get("CornSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 725) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1020, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 725) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")
        
        if self.seed_data.get("DaffodilSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 765) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1020, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 765) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            
        if self.seed_data.get("WatermelonSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 805) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1020, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 805) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Pumpkin
        if self.seed_data.get("PumpkinSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 845) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1040, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 845) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        if self.seed_data.get("AppleSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 885) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1040, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 885) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        if self.seed_data.get("BambooSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 925) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 685, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1080, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 685, 1)
            # 
            autoit.mouse_move(1800, 925) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        if self.seed_data.get("CoconutSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 965) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1120, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 720, 1)
            # 
            autoit.mouse_move(1800, 965) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Cactus Seeds
        if self.seed_data.get("CactusSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1005) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1120, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 720, 1)
            # 
            autoit.mouse_move(1800, 1005) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")
        
        if self.seed_data.get("DragonFruitSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1045) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1120, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 720, 1)
            # 
            autoit.mouse_move(1800, 1045) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        if self.seed_data.get("MangoSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1085) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1160, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 800, 1)
            # 
            autoit.mouse_move(1800, 1085) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        # Grape Seeds
        if self.seed_data.get("GrapeSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1125) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1160, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 800, 1)
            # 
            autoit.mouse_move(1800, 1125) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        if self.seed_data.get("MushroomSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1165) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1160, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 800, 1)
            # 
            autoit.mouse_move(1800, 1165) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left")

        #Pepper Seeds
        if self.seed_data.get("PepperSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1205) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1200, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 860, 1)
            # 
            autoit.mouse_move(1800, 1205) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left") 

        if self.seed_data.get("CacaoSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1245) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 720, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1240, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 900, 1)
            # 
            autoit.mouse_move(1800, 1245) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left") 

        # Beanstalk Seed TODO: Might need to edit (update to new fruit line) when new fruits come out and the whole buy section # #
        if self.seed_data.get("BeanstalkSeed", False) and self.is_running:
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 1245) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_up("left")
            #
            autoit.mouse_click("left", 920, 1100, 1)
            self.safeSleep(1.5)
            autoit.mouse_click("left", 1000, 1240, 20) 
            self.safeSleep(1.5)
            autoit.mouse_click("left", 920, 1000, 1)
            # 
            autoit.mouse_move(1800, 1245) # Update to new fruit
            self.safeSleep(1.2)
            autoit.mouse_down("left")
            autoit.mouse_move(1800, 525)
            self.safeSleep(1.2)
            autoit.mouse_up("left") 
    
    # def gearShopMacro(self):


    # def eggShopMacro(self):


    # def bloodMoonShop(self):

    def shopBuy(self):
        if not self.is_running:
            return
        
        autoit.mouse_click("left", 920, 675, 1)
        self.safeSleep(1.5)
        autoit.mouse_click("left", 1000, 950, 20) 
        self.safeSleep(1.5)
        autoit.mouse_click("left", 920, 675, 1)

    def switchTabs(self):
            keyboard.press_and_release("alt + shift + tab")
            self.safeSleep(0.5)
            print("Switched to next tab")

    # Calculates time based on local time, or time zone in intervals of 5
    def waitUntilNextInterval(self):
        if not self.is_running:
            return

        now = datetime.now(self.est) # now = datetime.now(self.est)

        minutesPast = now.minute % 5
        secondsPast = now.second + now.microsecond/1_000_000

        if minutesPast == 0 or (minutesPast == 1 and now.second < 60):
            return
        
        minutesToWait = (5 - minutesPast) % 5
        nextRun = now.replace(second=0, microsecond=0) + timedelta(minutes=minutesToWait)
        wait_seconds = (nextRun - now).total_seconds()

        print(f"Current ET: {now.strftime('%H:%M:%S')}")
        print(f"Next run at: {nextRun.strftime('%H:%M:%S')}")
        print(f"Waiting {wait_seconds:.1f} seconds")

        while wait_seconds > 0 and self.is_running:
            time.sleep(min(1, wait_seconds))
            wait_seconds -= 1




