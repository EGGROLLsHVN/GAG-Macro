import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
from macro import Macro
import keyboard

class Newlv():
    def __init__(self, window, reruns):
        self.toplv = window
        self.reruns = reruns # TODO: Remember that reruns is the number of alts we want to collect
        self.seed_vars = {}
        self.macro = None
        self.setup_global_hotkeys()

        self.shopCategories = {
            # Seed Shop
            "Carrot": "SeedShop",
            "Strawberry": "SeedShop",
            "Blueberry": "SeedShop",
            "OrangeTulip": "SeedShop",
            "TomatoSeed": "SeedShop",
            "CornSeed": "SeedShop",
            "WatermelonSeed": "SeedShop",
            "PumpkinSeed": "SeedShop",
            "AppleSeed": "SeedShop",
            "BambooSeed": "SeedShop",
            "CoconutSeed": "SeedShop",
            "CactusSeed": "SeedShop",
            "DragonFruitSeed": "SeedShop",
            "MangoSeed": "SeedShop",
            "GrapeSeed": "SeedShop",
            "MushroomSeed": "SeedShop",
            "PepperSeedCacaoSeed": "SeedShop",
            "BeanstalkSeed": "SeedShop",

            # Bloodmoon Shop
            "MysteriousCrate": "BloodMoonShop",
            "NightEgg": "BloodMoonShop",
            "NightSeedPack": "BloodMoonShop",
            "BloodBananaSeed": "BloodMoonShop",
            "MoonMelonSeed": "BloodMoonShop",
            "StarCaller": "BloodMoonShop",
            "BloodKiwi": "BloodMoonShop",
            "BloodHedgehog": "BloodMoonShop",
            "BloodOwl": "BloodMoonShop",

            # Gear Shop
            "WateringCan": "GearShop",
            "Trowel": "GearShop",
            "RecallWrench": "GearShop",
            "BasicSprinkler": "GearShop",
            "AdvancedSprinkler": "GearShop",
            "GodlySprinkler": "GearShop",
            "LightningRod": "GearShop",
            "MasterSprinkler": "GearShop",
            "FavoriteTool": "GearShop",

            # Egg Shop
            "All": "EggShop",
        }

        self.seeds = {
            # Seed Shop:
            "SeedShop": 0,
            "Carrot": False,
            "Strawberry": False,
            "Blueberry": False,
            "OrangeTulip": False,
            "TomatoSeed": False,
            "CornSeed": False,
            "WatermelonSeed": False,
            "PumpkinSeed": False,
            "AppleSeed": False,
            "BambooSeed": False,
            "CoconutSeed": False,
            "CactusSeed": False,
            "DragonFruitSeed": False,
            "MangoSeed": False,
            "GrapeSeed": False,
            "MushroomSeed": False,
            "PepperSeedCacaoSeed": False,
            "BeanstalkSeed": False,

            # Bloodmoon Shop:
            "BloodMoonShop": 0,
            "MysteriousCrate": False,
            "NightEgg": False,
            "NightSeedPack": False,
            "BloodBananaSeed": False,
            "MoonMelonSeed": False,
            "StarCaller": False,
            "BloodKiwi": False,
            "BloodHedgehog": False,
            "BloodOwl": False,

            # Gear:
            "GearShop": 0,
            "WateringCan": False,
            "Trowel": False,
            "RecallWrench": False,
            "BasicSprinkler": False,
            "AdvancedSprinkler": False,
            "GodlySprinkler": False,
            "LightningRod": False,
            "MasterSprinkler": False,
            "FavoriteTool": False,

            # Eggshop:
            "EggShop": 0,
            "All": False
        }

        for seed in self.seeds:
            self.seed_vars[seed] = tk.BooleanVar(value=self.seeds[seed])


    def setup_global_hotkeys(self):
        # Bind Ctrl+1 to start_macro (works even if window is not focused)
        keyboard.add_hotkey('ctrl+1', self.start_macro)
        # Bind Ctrl+2 to stop_macro
        keyboard.add_hotkey('ctrl+2', self.stop_macro)

    def newlvBuilder(self):
        toplv = self.toplv
        xGeo, yGeo = 600, 800

        toplv.geometry(f"{xGeo}x{yGeo}")
        toplv.title("Grow A Garden Multi Alt Macro")
        toplv.config(background="#292928")
        toplv.resizable(False, False)

        # Create style for notebook
        style = ttk.Style()
        style.theme_create("custom", parent="default", settings={
            "TNotebook": {      # Notebook styles
                "configure": {
                    "background": "#1e1e1e",  # Dark background for tab bar
                    "tabmargins": [5, 5, 0, 0],  # Margins around tabs
                }
            },
            "TNotebook.Tab": {      # Individual Tab Styles
                "configure": {
                    "background": "#3d3d3d",  # Inactive tab color
                    "foreground": "white",
                    "padding": [15, 5],  # Horizontal, vertical padding
                    "font": ('Comic Sans MS', 10)
                },
                "map": {        # State dependant tab styles
                    "background": [("selected", "#4d4d4d")],  # Active tab color
                    "expand": [("selected", [1, 1, 1, 0])]  # Stretch selected tab
                }
            }
        })
        style.theme_use("custom")

        # Pack notebook to fill window
        containFrame = Frame(toplv, bg="#292928")
        containFrame.pack(expand=True, fill="both", padx=20, pady=20)

        # Create notebook with top tab bar
        shopBook = ttk.Notebook(containFrame)
        shopBook.pack(expand=True, fill="both")
        
        # Create frames with dark background
        regSeeds = Frame(shopBook, bg="#292928")
        gearShop = Frame(shopBook, bg="#292928")
        eggShop = Frame(shopBook, bg="#292928")
        bloodMoonShop = Frame(shopBook, bg="#292928")
        startTab = Frame(shopBook, bg="#292928")

        # Add tabs to notebook
        shopBook.add(regSeeds, text="Regular")
        shopBook.add(gearShop, text="Gear")
        shopBook.add(eggShop, text="Eggs")
        shopBook.add(bloodMoonShop, text="Event")
        shopBook.add(startTab, text="Start Macro")
        
    


        # Reg Seeds
        for seed in ["Carrot", "Strawberry", "Blueberry", "OrangeTulip", "TomatoSeed", "CornSeed", "WatermelonSeed", "PumpkinSeed", "AppleSeed", "BambooSeed", "CoconutSeed", "CactusSeed", "DragonFruitSeed", "MangoSeed", "GrapeSeed", "MushroomSeed", "PepperSeedCacaoSeed", "BeanstalkSeed", 
]:
            Checkbutton(regSeeds, 
                        text=seed, 
                        variable=self.seed_vars[seed], 
                        onvalue=True, 
                        offvalue=False, 
                        command=lambda s=seed: self.update_seed(s),
                        bg="#292928",
                        fg="white",
                        selectcolor="#1e1e1e",
                        activebackground="#292928",
                        activeforeground="white"
                        ).pack()
            
        # Gear Shop    
        for gear in ["WateringCan", "Trowel", "RecallWrench", "BasicSprinkler", "AdvancedSprinkler", "GodlySprinkler", "LightningRod", "MasterSprinkler", "FavoriteTool"]:

            Checkbutton(gearShop, 
                        text=gear, 
                        variable=self.seed_vars[gear], 
                        onvalue=True, 
                        offvalue=False, 
                        command=lambda g=gear: self.update_seed(g),
                        bg="#292928",
                        fg="white",
                        selectcolor="#1e1e1e",
                        activebackground="#292928",
                        activeforeground="white"
                        ).pack()
        # Egg Shop
        for egg in ["All"]:
            Checkbutton(eggShop, 
                        text=egg, 
                        variable=self.seed_vars[egg], 
                        onvalue=True, 
                        offvalue=False, 
                        command=lambda e=egg: self.update_seed(e),
                        bg="#292928",
                        fg="white",
                        selectcolor="#1e1e1e",
                        activebackground="#292928",
                        activeforeground="white"
                        ).pack()
            
        # Blood Moon Shop
        for bloodSeed in ["MysteriousCrate", "NightEgg", "NightSeedPack", "BloodBananaSeed", "MoonMelonSeed", "StarCaller", "BloodKiwi", "BloodHedgehog", "BloodOwl"]:
            Checkbutton(bloodMoonShop, 
                        text=bloodSeed, 
                        variable=self.seed_vars[bloodSeed], 
                        onvalue=True, 
                        offvalue=False, 
                        command=lambda b=bloodSeed: self.update_seed(b),
                        bg="#292928",
                        fg="white",
                        selectcolor="#1e1e1e",
                        activebackground="#292928",
                        activeforeground="white"
                        ).pack()

        Button(startTab, 
            text="Start: Ctrl + 1",
            font=("Comic Sans MS", 12, 'bold'),  # Increased from 10 to 12
            width=14,  # Increased from 4 to 14 (proportional to font increase)
            height=2,  # Kept at 2 for taller button
            bd=0,
            highlightthickness=0,
            highlightbackground="#4d4d4d",
            highlightcolor="#4d4d4d",
            fg="White",
            bg="#4d4d4d",  # Matching your theme
            activebackground="#3d3d3d",
            padx=10,  # Horizontal padding
            pady=5,    # Vertical padding
            takefocus=0,
            command=self.start_macro # lambda: self.runMacro(self.seeds, self.reruns, True)
            ).pack(pady=(20,0), expand=True)
        
        Button(startTab, 
            text="Stop: Ctrl + 2",
            font=("Comic Sans MS", 12, 'bold'),  # Increased from 10 to 12
            width=14,  # Increased from 4 to 14 (proportional to font increase)
            height=2,  # Kept at 2 for taller button
            bd=0,
            highlightthickness=0,
            highlightbackground="#4d4d4d",
            highlightcolor="#4d4d4d",
            fg="White",
            bg="#4d4d4d",  # Matching your theme
            activebackground="#3d3d3d",
            padx=10,  # Horizontal padding
            pady=5,    # Vertical padding
            takefocus=0,
            command=self.stop_macro    # lambda: self.runMacro(self.seeds, self.reruns, False)
            ).pack(pady=(0,20), expand=True)

    def update_seed(self, seedName):
        self.seeds[seedName] = self.seed_vars[seedName].get()
        category = self.shopCategories.get(seedName)

        if self.seed_vars[seedName].get() is True:
            self.seeds[category] +=1
        else:
            self.seeds[category] -=1

        print(f"{seedName} state: {self.seeds[seedName]}") 
        print(f"{category} Buying: {self.seeds[category]}")

    def start_macro(self):
        if self.macro is None or not self.macro.is_running:
            self.macro = Macro(self.seeds, self.reruns)
            self.macro.start()
            print("Starting Macro")

    def stop_macro(self):
        if self.macro is not None and self.macro.is_running:
            self.macro.stop()
            print("Stopping Macro")

    def start_macro(self, event=None):
        if self.macro is None or not self.macro.is_running:
            self.macro = Macro(self.seeds, self.reruns)
            self.macro.start()
            print("Starting Macro")

    def stop_macro(self, event=None):
        if self.macro is not None and self.macro.is_running:
            self.macro.stop()
            print("Stopping Macro")

