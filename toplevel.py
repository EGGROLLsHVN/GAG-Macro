import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
from macro import Macro
import keyboard
import autoit

class Newlv():
    def __init__(self, window, reruns):
        self.toplv = window
        self.reruns = reruns
        self.seed_vars = {}
        self.macro = None
        self.setup_global_hotkeys()
        self.seedMaxC = 2
        self.gearMaxC = 1
        self.eggMaxC=1
        self.bloodMC=1
       

        self.shopCategories = {
            # Seed Shop
            "Carrot": "SeedShop",
            "Strawberry": "SeedShop",
            "Blueberry": "SeedShop",
            "OrangeTulip": "SeedShop",
            "TomatoSeed": "SeedShop",
            "CornSeed": "SeedShop",
            "DaffodilSeed": "SeedShop",
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
            "PepperSeed": "SeedShop",
            "CacaoSeed": "SeedShop",
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
            "DaffodilSeed": False,
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
            "PepperSeed": False,
            "CacaoSeed": False,
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
        # Bind Ctrl+1 to startMacro (works even if window is not focused)
        keyboard.add_hotkey('ctrl+1', self.startMacroKeybind, suppress=True, timeout=0.01)
        # Bind Ctrl+2 to stopMacro
        keyboard.add_hotkey('ctrl+2', self.stopMacroKeybind, suppress=True, timeout=0.001)

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
        
        # Create a container frame for the different tabs
        seedGrid = Frame(regSeeds, bg="#292928")
        seedGrid.pack(fill="both", expand=True, padx=10, pady=10)

        gearGrid = Frame(gearShop, bg="#292928")
        gearGrid.pack(fill="both", expand=True, padx=10, pady=10)

        bloodMoonGrid = Frame(bloodMoonShop, bg="#292928")
        bloodMoonGrid.pack(fill="both", expand=True, padx=10, pady=10)

        eggGrid = Frame(eggShop, bg="#292928")
        eggGrid.pack(fill="both", expand=True, padx=10, pady=10)

        # Reg Seeds

        for col in range(self.seedMaxC):
            seedGrid.grid_columnconfigure(col, weight=1)

        regularSeeds = ["Carrot", "Strawberry", "Blueberry", "OrangeTulip", "TomatoSeed", "CornSeed", 
                        "DaffodilSeed", "WatermelonSeed", "PumpkinSeed", "AppleSeed", "BambooSeed", 
                        "CoconutSeed", "CactusSeed", "DragonFruitSeed", "MangoSeed", "GrapeSeed", "MushroomSeed", 
                        "PepperSeed", "CacaoSeed", "BeanstalkSeed"]
                        
        # Add checkbuttons in grid layout
        for i, seed in enumerate(regularSeeds):
            row = i // self.seedMaxC
            column = i % self.seedMaxC

            Checkbutton(
                seedGrid,
                text=seed,
                variable=self.seed_vars[seed],
                onvalue=True,
                offvalue=False,
                command=lambda s=seed: self.updateSeed(s),
                bg="#292928",
                fg="white",
                selectcolor="#1e1e1e",
                activebackground="#292928",
                activeforeground="white",
                anchor="w",
                width=18  # Fixed width for consistent alignment
                ).grid(
                row=row,
                column=column,
                sticky="nsew",  # Expand to fill cell
                padx=5,
                pady=2
            )

        # Expanding Rows
        total_rows = (len(regularSeeds) // self.seedMaxC) + 1
        for row in range(total_rows):
            seedGrid.grid_rowconfigure(row, weight=1)

        # Gear Shop
        for col in range(self.gearMaxC):
            gearGrid.grid_columnconfigure(col, weight=1)

        gearItems = ["WateringCan", "Trowel", "RecallWrench", "BasicSprinkler", "AdvancedSprinkler", 
                     "GodlySprinkler", "LightningRod", "MasterSprinkler", "FavoriteTool"]

        for i, gear in enumerate(gearItems):
            row = i // self.gearMaxC
            column = i % self.gearMaxC

            Checkbutton(
                gearGrid,
                text=gear,
                variable=self.seed_vars[gear],
                onvalue=True,
                offvalue=False,
                command=lambda g=gear: self.updateSeed(g),
                bg="#292928",
                fg="white",
                selectcolor="#1e1e1e",
                activebackground="#292928",
                activeforeground="white",
                anchor="w",
                width=18  # Fixed width for consistent alignment
                ).grid(
                row=row,
                column=column,
                sticky="nsew",  # Expand to fill cell
                padx=5,
                pady=2
            )

        # Expanding Rows
        total_rows = (len(gearItems) // self.gearMaxC) + 1
        for row in range(total_rows):
            gearGrid.grid_rowconfigure(row, weight=1)

        # Egg Shop
        for col in range(self.eggMaxC):
            eggGrid.grid_columnconfigure(col, weight=1)

        eggShopList = ["All"]

        for i, egg in enumerate(eggShopList):
            row = i // self.eggMaxC
            column = i % self.eggMaxC

            Checkbutton(
                eggGrid,
                text=egg,
                variable=self.seed_vars[egg],
                onvalue=True,
                offvalue=False,
                command=lambda e=egg: self.updateSeed(e),
                bg="#292928",
                fg="white",
                selectcolor="#1e1e1e",
                activebackground="#292928",
                activeforeground="white",
                anchor="w",
                width=18  # Fixed width for consistent alignment
                ).grid(
                row=row,
                column=column,
                sticky="nsew",  # Expand to fill cell
                padx=5,
                pady=2
            )

        # Expanding Rows
        total_rows = (len(eggShopList) // self.eggMaxC) + 1
        for row in range(total_rows):
            eggGrid.grid_rowconfigure(row, weight=1)
        
        # Blood Moon Shop
        for col in range(self.bloodMC):
            bloodMoonGrid.grid_columnconfigure(col, weight=1)

        
        bloodItems = ["MysteriousCrate", "NightEgg", "NightSeedPack", "BloodBananaSeed", "MoonMelonSeed", 
                      "StarCaller", "BloodKiwi", "BloodHedgehog", "BloodOwl"]

        for i, bItems in enumerate(bloodItems):
            row = i // self.eggMaxC
            column = i % self.eggMaxC

            Checkbutton(
                bloodMoonGrid,
                text=bItems,
                variable=self.seed_vars[bItems],
                onvalue=True,
                offvalue=False,
                command=lambda b=bItems: self.updateSeed(b),
                bg="#292928",
                fg="white",
                selectcolor="#1e1e1e",
                activebackground="#292928",
                activeforeground="white",
                anchor="w",
                width=18  # Fixed width for consistent alignment
                ).grid(
                row=row,
                column=column,
                sticky="nsew",  # Expand to fill cell
                padx=5,
                pady=2
            )

        # Expanding Rows
        total_rows = (len(bloodItems) // self.bloodMC) + 1
        for row in range(total_rows):
            bloodMoonGrid.grid_rowconfigure(row, weight=1)

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
            command=self.startMacro # lambda: self.runMacro(self.seeds, self.reruns, True)
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
            command=self.stopMacro    # lambda: self.runMacro(self.seeds, self.reruns, False)
            ).pack(pady=(0,20), expand=True)

    def updateSeed(self, seedName):
        self.seeds[seedName] = self.seed_vars[seedName].get()
        category = self.shopCategories.get(seedName)

        if self.seed_vars[seedName].get() is True:
            self.seeds[category] +=1
        else:
            self.seeds[category] -=1

        print(f"{seedName} state: {self.seeds[seedName]}") 
        print(f"{category} Buying: {self.seeds[category]}")

    def startMacroKeybind(self, event=None):  
        self.startMacro()

    def startMacro(self):  
        if self.macro is None or not self.macro.is_running:
            self.macro = Macro(self.seeds, self.reruns)
            self.macro.start()
            print("Macro started")


    def stopMacroKeybind(self, event=None):  
        self.stopMacro()

    def stopMacro(self):  
        if  self.macro is not None and self.macro.is_running:
            self.macro.stop()
            self.macro = None
            # self.macro.thread.join(timeout=0.5)
            print("Macro stopped")
        else:
            print("No active macro to stop")

    

