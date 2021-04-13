# Alpha Version, v0.3.0
# Takes user-given width and height of a sprite, and dynamically creates
# a spritesheet resolution, along with coordinates for each type of frame.
# 
# Developed by BurntBread007
# 4/12/2021
import io
import os
from PIL import ImageDraw, Image, ImageFont

direct = os.getcwd()

xResolution = 0
yResolution = 0

xFrame = 0
yFrame = 0
spaceFrame = 0

frameCount = 94
framesPerRow = int(frameCount / 6)

xFilled = list()
yFilled = list()

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
    print(  "==      FunkyXML Editor for Friday Night Funkin               ==")
    print(  "==      version 0.3.0-alpha                                   ==")
    print(  "================================================================")
    print(  "developed by BurntBread007, idea inspired from Phoxx\n")

def printAllCoords():
    bar = "================================================================"

    print("\n\nCoordinates for Frames:\n")
    print("Death Loop (Frames 1 - 6) :\n"+bar)
    printCoords(1, 6)
    print("\n\nDeath Retry (Frames 7 - 30) :\n"+bar)
    printCoords(7, 30)
    print("\n\nHey! (Frames 31 - 33) :\n"+bar)
    printCoords(31, 33)
    print("\n\nDown Hits (Frames 34 - 37) :\n"+bar)
    printCoords(34, 37)
    print("\n\nLeft Hits (Frames 38 - 42) :\n"+bar)
    printCoords(38, 42)
    print("\n\nRight Hits (Frames 43 - 46) :\n"+bar)
    printCoords(43, 46)
    print("\n\nUp Hits (Frames 47 - 50) :\n"+bar)
    printCoords(47, 50)
    print("\n\nDeath Start (Frames 51 - 85) :\n"+bar)
    printCoords(51, 85)
    print("\n\nIdle (Frames 86 - 90) :\n"+bar)
    printCoords(86, 90)
    print("\n\nScared (Frames 91 - 94) :\n"+bar)
    printCoords(91, 94)

def printCoords(start, stop):
    global xFilled, yFilled, framesPerRow
    framesMapped = 0
    y = start
    while(y <= stop):
        print("[ "+str(xFilled[y])+", "+str(yFilled[y])+" ]", end="\t")
        framesMapped += 1
        if(framesMapped > (framesPerRow/3)):
            print("")
            framesMapped = 0
        y += 1

def calcCoords():
    global xFilled, yFilled, xFrame, yFrame, frameCount
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

def calcResolution():
    global xResolution, yResolution
    xResolution = xFrame * framesPerRow
    yResolution = yFrame * 7

# checkType() is currently not being used, might use for error-checking later on.
def checkType(inp):
    inp = int(input())
    while(type(inp) != 'int'):
        print("Oops")
        temp = int(input())
    inp = temp
    return inp

def askSettings():
    global xFrame, yFrame, spaceFrame

    print("Settings\n================================================================")
    print("Enter the width of your custom sprite frame:  ")
    xFrame = int(input())
    print("\nEnter the width of your custom sprite frame:  ")
    yFrame = int(input())
    print("\nChoose the spacing (in pixels) between each frame:  ")
    spaceFrame = int(input())

    xFrame = xFrame + spaceFrame
    yFrame = yFrame + spaceFrame

def editXML():
    global direct, xFilled, yFilled, xFrame, yFrame, spaceFrame
    frameNumbers = open(direct+"\\source\\frameNumbers.txt", "r")
    frameNumbers_contents = frameNumbers.read()
    frameNumbers_lines = frameNumbers_contents.split("\n")
    frameNumbers.close()
    
    xml = open(direct+"\\source\\BOYFRIEND.xml", "r")
    xml_contents = xml.read()
    xml_lines = xml_contents.split("\n")
    xml.close()
    
    newXml = open(direct+"\\output\\CUSTOM_SPRITE.xml", "w")
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

def askToSaveXML():
    print("\nWould you like to save a copy of the custom .xml file? (CUSTOM_SPRITE.xml) (Y/N)")
    saveToXML = input().upper()
    if(saveToXML == "Y"):
        print("\nSaving CUSTOM_SPRITE.xml...")
        editXML()
        print("Saved!")
    elif(saveToXML == "N"):
        print("XML edit is discarded.")

def drawImage():
    global xResolution, yResolution, xFrame, yFrame, xFilled, yFilled, frameCount, spaceFrame, direct

    img = Image.new('RGBA', (xResolution, yResolution), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    for x in range(frameCount):
        coords = [xFilled[x], yFilled[x], xFilled[x]+xFrame-spaceFrame, yFilled[x]+yFrame-spaceFrame]
        draw.rectangle(coords, fill ='green', outline ='red')

    img.save(direct+"\\output\\CUSTOM_SPRITE_OUTLINE.png")
    img.show()

def askToSaveImage():
    print("\n\nWould you like save a copy of the custom spritesheet outline guide? (CUSTOM_SPRITE_OUTLINE.png) (Y/N)")
    saveToImage = input().upper()
    if(saveToImage == "Y"):
        print("\nSaving CUSTOM_SPRITE_OUTLINE.png...")
        drawImage()
        print("Saved!")
    elif(saveToImage == "N"):
        print("\nImage file is discarded.")

def exitOnPress():
    exitPress = input("\n\nPress Enter to close program...")
    exit()

def main():
    printHeader()

    global xFilled, yFilled, xFrame, yFrame, spaceFrame, xResolution, yResolution
    xFilled.append(0)
    yFilled.append(0)

    askSettings()

    calcCoords()
    calcResolution()
    printAllCoords()

    print("\n\nTotal Spritesheet Resolution:\n " + str(xResolution) + " x " + str(yResolution))
    askToSaveXML()
    askToSaveImage()

    exitOnPress()
main()