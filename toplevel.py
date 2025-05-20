import tkinter as tk
from tkinter import *
from tkinter import ttk


class Newlv():
    def __init__(self, window, reruns):
        self.toplv = window
        self.reruns = reruns # TODO: Remember that reruns is the number of alts we want to collect

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
        
        # Create notebook with top tab bar
        shopBook = ttk.Notebook(toplv)
        
        # Create frames with dark background
        regSeeds = Frame(shopBook, bg="#292928")
        gearShop = Frame(shopBook, bg="#292928")
        eggShop = Frame(shopBook, bg="#292928")
        bloodMoonShop = Frame(shopBook, bg="#292928")

        # Add tabs to notebook
        shopBook.add(regSeeds, text="Regular Seeds")
        shopBook.add(gearShop, text="Gear Shop")
        shopBook.add(eggShop, text="Egg Shop")
        shopBook.add(bloodMoonShop, text="Blood Moon Shop")
        
        # Pack notebook to fill window
        shopBook.pack(expand=True, fill="both", padx=5, pady=5)





