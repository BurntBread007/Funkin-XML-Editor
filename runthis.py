# Alpha Version, v0.2.0
# Takes user-given width and height of a sprite, and dynamically creates
# a spritesheet resolution, along with coordinates for each type of frame.
# 
# Developed by BurntBread007
# 4/10/2021
import io
import os

class Runthis:
    def __init__(self, xFilled, yFilled, spaceFrame):
        self.x = xFilled
        self.y = yFilled
        self.spacing = spaceFrame

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getSpace(self):
        return self.spacing
    def printMe(self):
        print("[ "+str(self.x)+", "+str(self.y)+" ]")

def printHeader():
    print("\n================================================================")
    print(  "==      Spritesheet Creator for Friday Night Funkin           ==")
    print(  "==      version 0.2.0-alpha                                   ==")
    print(  "================================================================")
    print(  "developed by BurntBread007, idea inspired from Phoxx\n")

def printAllCoords(xFilled, yFilled, framesMapped, framesPerRow):
    bar = "================================================================"

    print("\n\nCoordinates for Frames:\n")
    print("Death Loop (Frames 1 - 6) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 1, 6)
    print("\n\nDeath Retry (Frames 7 - 30) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 7, 30)
    print("\n\nHey! (Frames 31 - 33) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 31, 33)
    print("\n\nDown Hits (Frames 34 - 37) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 34, 37)
    print("\n\nLeft Hits (Frames 38 - 42) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 38, 42)
    print("\n\nRight Hits (Frames 43 - 46) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 43, 46)
    print("\n\nUp Hits (Frames 47 - 50) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 47, 50)
    print("\n\nDeath Start (Frames 51 - 85) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 51, 85)
    print("\n\nIdle (Frames 86 - 90) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 86, 90)
    print("\n\nScared (Frames 91 - 94) :\n"+bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 91, 94)

def printCoords(xFilled, yFilled, framesMapped, framesPerRow, start, stop):
    y = start
    while(y <= stop):
        print("[ "+str(xFilled[y])+", "+str(yFilled[y])+" ]", end="\t")
        framesMapped += 1
        if(framesMapped > (framesPerRow/3)):
            print("")
            framesMapped = 0
        y += 1

def calcCoords(xFilled, yFilled, xFrame, yFrame, frameCount, framesPerRow):
    xCoord = 0
    yCoord = 0
    for x in range(frameCount):
        if((xFilled[x]+xFrame) < (framesPerRow*xFrame)):
            xCoord += xFrame
            xFilled.append(xCoord)
            yFilled.append(yCoord)
        elif((xFilled[x]+xFrame) >= (framesPerRow*xFrame)):
            yCoord += yFrame
            xCoord = 0
            xFilled.append(xCoord)
            yFilled.append(yCoord)

def calcResolution(xFrame, yFrame, framesPerRow):
    xResolution = xFrame * framesPerRow
    yResolution = yFrame * 7
    print("\n\nTotal Sheet Resolution: \n" + str(xResolution) + " x " + str(yResolution))

def askSettings():
    print("Settings\n================================================================")
    print("Enter the width of your custom sprite frame:  ")
    xFrame = int(input())
    print("\nEnter the width of your custom sprite frame:  ")
    yFrame = int(input())
    print("\nChoose the spacing (in pixels) between each frame:  ")
    spaceFrame = int(input())

    xFrame = xFrame + spaceFrame
    yFrame = yFrame + spaceFrame
    return xFrame,yFrame,spaceFrame

def editXML(spaceFrame, xFrame, yFrame, xFilled, yFilled):
    direct = os.getcwd()

    frameNumbers = open(direct+"\\source\\frameNumbers.txt", "r")
    frameNumbers_contents = frameNumbers.read()
    frameNumbers_lines = frameNumbers_contents.split("\n")
    frameNumbers.close()
    
    xml = open(direct+"\\source\\BOYFRIEND.xml", "r")
    xml_contents = xml.read()
    xml_lines = xml_contents.split("\n")
    xml.close()
    
    newXml = open(direct+"\\output\\CUSTOM.xml", "w")
    newXml_list = list()
    for i in range(502):
        currentFrame = int(float(frameNumbers_lines[i]))
        writeOver = "x=\""+str(xFilled[currentFrame])+"\" y=\""+str(yFilled[currentFrame])+"\" width=\""+str((xFrame-spaceFrame))+"\" height=\""+str((yFrame-spaceFrame))+"\" frameX=\""+str(spaceFrame*-1)+"\" frameY=\""+str(spaceFrame*-1)+"\" frameWidth=\""+str(xFrame)+"\" frameHeight=\""+str(yFrame)+"\"/>"

        if(int(float(frameNumbers_lines[i])) == 0):
            newXml_list.append(xml_lines[i]+"\n")
        else:
            startingIndex = xml_lines[i].find("x=")
            newXml_list.append(xml_lines[i][:startingIndex]+writeOver+"\n")

    for x in newXml_list:
        newXml.writelines(x)
    newXml.close()

#def askToSaveFile():
#    print("\nWould you like to save these results to a .txt file? (Y/N)")
#    saveToFile = input().upper()
#    if(saveToFile == "Y"):
#        savefile = open(direct+"\\spritesheet_coordinates.txt", "w")
#        writeAllCoords(xFilled, yFilled, framesMapped, framesPerRow, savefile)
#        savefile.close()
#    elif(saveToFile == "N"):
#        print("\nNo file has been created.")

def askToSaveXML(spaceFrame, xFrame, yFrame, xFilled, yFilled):
    print("\nWould you like to save a copy of a custom xml file? (CUSTOM.xml) (Y/N)")
    saveToXML = input().upper()
    if(saveToXML == "Y"):
        print("Saving CUSTOM.xml...")
        editXML(spaceFrame, xFrame, yFrame, xFilled, yFilled)
        print("Saved!")
    elif(saveToXML == "N"):
        print("\nXML edit is discarded.")

def exitOnPress():
    exitPress = input("\n\nPress Enter to close program...")
    exit()

def main():
    # Variables for sprite data.
    xFrame = 0
    yFrame = 0
    spaceFrame = 0
    frameCount = 94
    framesPerRow = int(frameCount / 6)

    # Variables for mapping frames onto spritesheet.
    framesMapped = 0
    xFilled = list()
    yFilled = list()
    xFilled.append(0)
    yFilled.append(0)

    printHeader()
    xFrame,yFrame,spaceFrame = askSettings()

    calcCoords(xFilled, yFilled, xFrame, yFrame, frameCount, framesPerRow)
    printAllCoords(xFilled, yFilled, framesMapped, framesPerRow)
    calcResolution(xFrame, yFrame, framesPerRow)

    askToSaveXML(spaceFrame, xFrame, yFrame, xFilled, yFilled)
    exitOnPress()
main()