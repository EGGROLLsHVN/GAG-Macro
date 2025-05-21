# import pyautogui
# import threading
# import time
# import keyboard
# from datetime import datetime, timedelta
# import pytz # For timezone handling
# import autoit   # Direct input automations

# waitTm = .1
# rblxDelay = 1

# class Macro():
#     def __init__(self, seed_data, runCount,):
#         self.seed_data = seed_data  # Store the seeds dictionary
#         self.runCount = runCount
#         self.is_running = False
#         self.thread = None
#         self.est = pytz.timezone("US/Eastern")

#     def start(self):
#         if not self.is_running:
#             self.is_running = True
#             self.thread = threading.Thread(target=self.mainLoop, daemon=True)
#             self.thread.start()

#     def stop(self):
#         self.is_running = False
#         if self.thread and self.thread.is_alive():
#             self.thread.join(timeout=1)
    
#     # Handles controling loop: starting, number of iterations, controlling the time
#     def mainLoop(self):
#         while self.is_running is not False:
#             self.runMacroCycle()
#             self.waitUntilNextInterval()

#     # needs to repeat number of runCount times each time it finishes it alt tabes once
#         # Could use alt + shift + tab to reverse through tabs in order which could work
#     def runMacroCycle(self):
#         for run in range(self.runCount):
#             if not self.is_running:
#                 break

#             print(f"Starting run {run + 1}/{self.runCount}")
#             self.executeMacro()

#             # if run < (self.runCount):
#             #     self.switchTabs()
                

#     # TODO: Actually create the macros according to each seed setting
#     def executeMacro(self):
#         time.sleep(.5)
#         autoit.win_activate("Roblox")
#         print(pyautogui.position()) # Needs to be at x=851, y=192
#         autoit.mouse_click(851,192, 3)
#         # pyautogui.click(851,192, clicks=3, interval=waitTm)
#         # time.sleep(5)

#         if self.seed_data.get("SeedShop") > 0:
#             self.regSeedMacro()

#         # if self.seed_data.get("GearShop") > 0:
#         #     self.gearShopMacro()

#         # if self.seed_data.get("BloodMoonShop") > 0:
#         #     self.eggShopMacro()
#         # if self.seed_data.get("EggShop") > 0:
#         #     self.bloodMoonShop()

#     def regSeedMacro(self):
#         print("RegularSeed")
#         pyautogui.press("e", presses=3, interval=rblxDelay)

#         if self.seed_data.get("Carrot", False):
#             pyautogui.click(573, 870, clicks=3, interval=waitTm)
#             pyautogui.click(1010, 935, clicks=3, interval=waitTm) # time.sleep(waitTm) # Carrot click (x=573, y=870), buy (x=1010, y=935)


#         # if self.seed_data.get("Strawberry", False):
#         #     pyautogui.click(1795, 522, clicks=3, interval=waitTm)
#         #     pyautogui.mouseDown(button="left") # Hold the scroll bar and scroll down the correct amount until it lines up with the image i took note off
#         #     pyautogui.move(0, 100, duration=1.0)



#     # def gearShopMacro(self):


#     # def eggShopMacro(self):


#     # def bloodMoonShop(self):

#     # def shopScroll(self):
#     #   x = 1795, y = 123
#         # Need to manually 
        



#     def switchTabs(self):
#             keyboard.press_and_release("alt + shift + tab")
#             time.sleep(0.5)
#             print("Switched to next tab")

#     # Calculates time based on local time, or time zone in intervals of 5
#     def waitUntilNextInterval(self):
#         if not self.is_running:
#             return

#         now = datetime.now() # now = datetime.now(self.est)
#         nextRun = now + timedelta(minutes=5)
#         nextRun = nextRun.replace(second=0, microsecond=0)

#         if now.minute % 5 == 0:
#             nextRun += timedelta(minutes=5)

#         wait_seconds = (nextRun - now).total_seconds()

#         while wait_seconds > 0 and self.is_running:
#             time.sleep(min(1, wait_seconds))
#             wait_seconds-=1




