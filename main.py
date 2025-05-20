import tkinter as tk
from tkinter import *
from menu import Menu 

# Windows = Container to hold widgets
# Widgets = GUI elements: buttons, textboxes, labels, images
    # Labels: Holds text or images
    # Buttons: Self explanatory 
    # Entry Widget: Textbox that accepts user input

class Main ():
    def __init__(self):
        self.root = Tk() #Instatiates a window
        self.menuBuild = Menu(self.root)  # Pass the window to Menu
        self.menuBuild.guiBuilder()
        self.root.mainloop() # Opens window and listens for events
        
        reruns = self.menuBuild.reruns
        print(f"{reruns} number") 
        






if __name__ == "__main__":
    app = Main()  # This only runs when gui.py is executed directly
