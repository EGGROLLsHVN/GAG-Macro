import tkinter as tk
from tkinter import *
from menu import Menu 

# Windows = Container to hold widgets
# Widgets = GUI elements: buttons, textboxes, labels, images
    # Labels: Holds text or images
    # Buttons: Self explanatory 
    # Entry Widget: Textbox that accepts user input
    # Nodebook: Widget that manages a collection of windows/displays

class Main ():
    def __init__(self):
        self.root = Tk() #Instatiates a window
        self.menuBuild = Menu(self.root)  # Pass the window to Menu
        self.menuBuild.guiBuilder()
        self.root.mainloop() # Opens window and listens for events
        
        # reruns = self.menuBuild.reruns
        
        # self.toplv = Toplevel()
        # toplv = self.toplv
        # self.protocol("WM_DELETE_WINDOW", lambda: settingWindow(toplv))


        # self.root.mainloop() # Opens window and listens for events







if __name__ == "__main__":
    app = Main()  # This only runs when gui.py is executed directly

# def settingWindow():


# def runMacro():
#     # if the time is a multiple of 5 then run the loop again for the number of reruns executed 
#     # if the time is not a multiple of 5 and less than the next multiple of 5 then keep executing the loop for the number of reruns left

