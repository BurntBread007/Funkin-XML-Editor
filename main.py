#
# Comments
#

import io
import os

#from lib import VanillaEngine
#from lib import KadeEngine
#from lib import PsychEngine

from lib import SpriteConverting
from lib import ImageWriting
from lib import XmlEditing
#from lib import GlobalVars

from PIL import ImageDraw, Image, ImageFont, features
direct = os.getcwd()

#class Main:
#    def __init__(self, var):
#        self.x = var
#
#    def getVar(self):
#        return self.x
#    def printMe(self):
#        print("[ "+str(self.x)+", "+str(self.y)+" ]")

def printHeader():
    print("\n================================================================")
    print(  "==      FunkyXML Editor (for Friday Night Funkin)             ==")
    print(  "==      version 0.5.0-alpha (rewrite of 0.4.0)                ==")
    print(  "================================================================")
    print(  "developed by BurntBread007\n")

def chooseEngine():
    print("Before we begin, please choose the corresponding game engine you wish to create, edit, or convert sprites for.")
    print("1 -- Vanilla Engine (default)")
    print("2 -- Kade Engine")
    print("3 -- Psych Engine\n")

    engine = checkType(3)
    return engine

def printMainMenu():
    print("\nChoose an action below to complete. (To-Add: Append \"help\" after the number to learn more about the action.)")
    print("\n==============================\n")
    print("1 -- Create spritesheet template(s)")
    print("2 -- Create or edit XML file(s)")
    print("3 -- Convert Frames -> Spritesheet")
    print("4 -- Convert Spritesheet -> Frames")
    print("n/a -- Convert to another engine")
    print("5 -- Quit Application")

    inp = checkType(5)
    if(inp == 1):
        ImageWriting.run()
    elif(inp == 2):
        XmlEditing.run()
    elif(inp == 3):
        SpriteConverting.run(0)
    elif(inp == 4):
        SpriteConverting.run(1)
    elif(inp == 5):
        exitOnPress()  

def checkType(inpMax):
    inp = input()
    try:
        inpInt = int(inp)
        if(inpInt < 1 & inpInt <= inpMax):
            inpInt = inpInt * -1
        return inpInt
    except ValueError:
        print("Invalid response. Try again with a whole number.")
        return(checkType(inpMax))

def exitOnPress():
    exitPress = input("\n\nPress Enter to close program...")
    exit()

def main():
    printHeader()
    userChoice = printMainMenu()
main()