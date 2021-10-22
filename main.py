#
# Comments
#

import io
import os

#from lib import VanillaEngine, KadeEngine, PsychEngine

from lib import globalVars, SpriteConverting, ImageWriting, XmlEditing

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
    print("1 -- Create spritesheet from scratch")
    print("2 -- Create spritesheet and/or XML from existing XML")
    print("3 -- Convert Frames to Spritesheet")
    print("4 -- Convert to another engine")
    print("5 -- Quit Application")

    inp = checkType(5)
    if(inp == 1):
        askFrameSettings()
        globalVars.usingXml = 'false'
        ImageWriting.run()
    elif(inp == 2):
        askFrameSettings()
        globalVars.usingXml = 'true'
        XmlEditing.run()
        ImageWriting.run()
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
        if(inpInt < 1):
            inpInt = inpInt * -1
        if(inpInt > inpMax):
            print("\nNumber is too high. Try a smaller number.")
            return(checkType(inpMax))
        return inpInt
    except ValueError:
        print("\nInvalid response. Try again with a whole number.")
        return(checkType(inpMax))

def askFrameSettings():
    print("\n\nChoose settings from a file or create manually?")
    print("1 -- Create manually")
    print("2 -- Create by file\n")
    frameMakeMethod = checkType(2)
    
    if(frameMakeMethod == 1):
        print("\nFrame X-resolution? (Max is 2048 pixels)")
        globalVars.xRes = checkType(2048)
        print("\nFrame Y-resolution? (Max is 2048 pixels)")
        globalVars.yRes = checkType(2048)
        globalVars.spaceRes = int(((globalVars.xRes+globalVars.yRes) * 0.025)+1)
        print("\nHow many frames will the spritesheet have? (Max is 256 frames")
        globalVars.frameCount = checkType(256)
    elif(frameMakeMethod == 2):
        print("not done yet")
        exitOnPress()
    
def exitOnPress():
    exitPress = input("\n\nPress Enter to close program...")
    exit()

def main():
    printHeader()
    userChoice = printMainMenu()
main()