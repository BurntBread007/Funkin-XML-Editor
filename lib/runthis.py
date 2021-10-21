# Alpha Version, v0.4.0
# Takes user-given width and height of a sprite, and dynamically creates
# a spritesheet resolution, along with coordinates for each type of frame.
# 
# Developed by BurntBread007
# 4/14/2021
import io
import os
from PIL import ImageDraw, Image, ImageFont, features

direct = os.getcwd()

xResolution = 0
yResolution = 0

xFrame = 0
yFrame = 0
spaceFrame = 0

frameCount = 0
framesPerRow = 0
framefile = ""
xmlfile = ""

xFilled = list()
yFilled = list()
typeFilled = list()

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
    print(  "==      version 0.4.0-alpha                                   ==")
    print(  "================================================================")
    print(  "developed by BurntBread007, idea inspired from Phoxx\n")

def printAllCoords():
    global framefile
    bar = "================================================================"
    print("\n\nCoordinates for Frames:\n")
    if(framefile == "boyfriend_frames.txt"):
        print("Death Loop (Frames 1 - 6) :\n"+bar)
        printCoords(1, 6, "Death \nLoop")
        print("\n\nDeath Retry (Frames 7 - 30) :\n"+bar)
        printCoords(7, 30, "Death \nRetry")
        print("\n\nHey! (Frames 31 - 33) :\n"+bar)
        printCoords(31, 33, "Hey!")
        print("\n\nDown Hits (Frames 34 - 37) :\n"+bar)
        printCoords(34, 37, "Down")
        print("\n\nLeft Hits (Frames 38 - 42) :\n"+bar)
        printCoords(38, 42, "Left")
        print("\n\nRight Hits (Frames 43 - 46) :\n"+bar)
        printCoords(43, 46, "Right")
        print("\n\nUp Hits (Frames 47 - 50) :\n"+bar)
        printCoords(47, 50, "Up")
        print("\n\nDeath Start (Frames 51 - 85) :\n"+bar)
        printCoords(51, 85, "Death \nStart")
        print("\n\nIdle (Frames 86 - 90) :\n"+bar)
        printCoords(86, 90, "Idle")
        print("\n\nScared (Frames 91 - 94) :\n"+bar)
        printCoords(91, 94, "Scared")
    elif(framefile == "bfCar_frames.txt"):
        print("Down (Frames 1 - 8) :\n"+bar)
        printCoords(1, 8, "Down")
        print("\n\nLeft Hits (Frames 9 - 17) :\n"+bar)
        printCoords(9, 17, "Left")
        print("\n\nRight Hits (Frames 18 - 25) :\n"+bar)
        printCoords(18, 25, "Right")
        print("\n\nUp Hits (Frames 26 - 33) :\n"+bar)
        printCoords(26, 33, "Up")
        print("\n\n Idle Hits (Frames 34 - 23) :\n"+bar)
        printCoords(34, 45, "Idle")
    elif(framefile == "bfChristmas_frames.txt"):
        print("Hey! (Frames 1 - 3) :\n"+bar)
        printCoords(1, 3, "Hey!")
        print("\n\nDown Hits (Frames 4 - 8) :\n"+bar)
        printCoords(4, 8, "Down")
        print("\n\nLeft Hits (Frames 9 - 13) :\n"+bar)
        printCoords(9, 13, "Left")
        print("\n\nRight Hits (Frames 14 - 18) :\n"+bar)
        printCoords(14, 18, "Right")
        print("\n\nUp Hits (Frames 19 - 23) :\n"+bar)
        printCoords(19, 23, "Up")
        print("\n\nIdle (Frames 24 - 28) :\n"+bar)
        printCoords(24, 28, "Idle")

def printCoords(start, stop, animType):
    global xFilled, yFilled, typeFilled, framesPerRow
    framesMapped = 0
    y = start - 1
    while(y <= (stop-1)):
        print("[ "+str(xFilled[y])+", "+str(yFilled[y])+" ]", end="\t")
        framesMapped += 1
        typeFilled[y] = animType
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
    global xResolution, yResolution, framesPerRow
    xResolution = xFrame * framesPerRow
    yResolution = yFrame * 7

def checkType():
    inp = input()
    try:
        inpInt = int(inp)
        if(inpInt < 1):
            inpInt = inpInt * -1
        return inpInt
    except ValueError:
        print("Invalid response. Try again with a whole number.")
        return(checkType())

def askSettings():
    global xFrame, yFrame, spaceFrame, frameCount, framefile, xmlfile

    print("Settings\n================================================================")

    print("Choose a character you would like to customize:")
    print("\nCharacters:\n \tBoyfriend - Press 1\n \tBoyfriend Car - Press 2\n \tBoyfriend Christmas - Press 3")
    charInp = checkType()
    if(charInp == 1): #original
        frameCount = 94
        xmlfile = "BOYFRIEND.xml"
        framefile = "boyfriend_frames.txt"
    elif(charInp == 2): # car
        frameCount = 45
        xmlfile = "bfCar.xml"
        framefile = "bfCar_frames.txt"
    elif(charInp == 3): # christmas
        frameCount = 28
        xmlfile = "bfChristmas.xml"
        framefile = "bfChristmas_frames.txt"
    #elif(charInp == '4'): # pixel
    #   frameCount = "a lot"
    #   xmlfile = "bfPixels.xml"
    #   xmlfile2 = "bfPixelsDEAD.xml"
    #   framefile = "bfPixels_frames.txt"
    #   framefile2 = "bfPixelsDEAD_frames.txt"

    print("Enter the width (in pixels) of your custom sprite frame:  ")
    xFrame = checkType()
    print("\nEnter the height (in pixels) of your custom sprite frame:  ")
    yFrame = checkType()
    print("\nChoose the spacing (in pixels) between each frame:  ")
    spaceFrame = checkType()

    xFrame = xFrame + spaceFrame
    yFrame = yFrame + spaceFrame

def editXML():
    global direct, xFilled, yFilled, xFrame, yFrame, spaceFrame, framefile
    frameNumbers = open(direct+"\\source\\"+framefile, "r")
    frameNumbers_contents = frameNumbers.read()
    frameNumbers_lines = frameNumbers_contents.split("\n")
    frameNumbers.close()

    try:
        xml = open(direct+"\\source\\"+xmlfile, "r")
        xml_contents = xml.read()
        xml_lines = xml_contents.split("\n")
        xml.close()

        newXml = open(direct+"\\output\\CUSTOM_SPRITE.xml", "w")
        newXml_list = list()
        for i in range(len(frameNumbers_lines)):
            currentFrame = int(float(frameNumbers_lines[i]))-1
            writeOver = "x=\""+str(xFilled[currentFrame])+"\" y=\""+str(yFilled[currentFrame])+"\" width=\""+str((xFrame-spaceFrame))+"\" height=\""+str((yFrame-spaceFrame))+"\" frameX=\""+str(spaceFrame*-1)+"\" frameY=\""+str(spaceFrame*-1)+"\" frameWidth=\""+str(xFrame)+"\" frameHeight=\""+str(yFrame)+"\"/>"
            if(int(float(frameNumbers_lines[i])) < 1):
                newXml_list.append(xml_lines[i]+"\n")
            else:
                startingIndex = xml_lines[i].find("x=")
                newXml_list.append(xml_lines[i][:startingIndex]+writeOver+"\n")

        for x in newXml_list:
            newXml.writelines(x)
        newXml.close()
    except FileNotFoundError:
        print("\nHmm, we couldn't find \""+xmlfile+"\" in the source folder. If it isn't there, add it in and restart the program.\nIf it is already there, check the spelling of the file name, as well as the contents of the file (should be about 502 lines of text).\n\nCurrently this project is designed to only use the vanilla 'BOYFRIEND'.xml, so make sure you aren't using a modified version.")
        exitOnPress()

def askToSaveXML():
    saveToXML = input().upper()
    if(saveToXML[0:1] == "Y"):
        print("\nSaving CUSTOM_SPRITE.xml...")
        editXML()
        print("Saved! \nCheck your output folder for results!")
    elif(saveToXML[0:1] == "N"):
        print("XML edit is discarded.")
    else:
        print("\nInvalid response. Type Y or N (or Yes/No)")
        askToSaveXML()

def drawImage():
    global xResolution, yResolution, xFrame, yFrame, xFilled, yFilled, typeFilled, frameCount, spaceFrame, direct

    img = Image.new('RGBA', (xResolution, yResolution), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    font_numbers_size = int(yFrame / 3)
    font_numbers = ImageFont.truetype('arial.ttf', font_numbers_size)

    if(xFrame >= yFrame):
        font_names_size = int(yFrame / 4)
    else:
        font_names_size = int(xFrame / 3.5)
    font_names = ImageFont.truetype('arial.ttf', font_names_size)

    for x in range(frameCount):
        coords = [xFilled[x], yFilled[x], xFilled[x]+xFrame-spaceFrame, yFilled[x]+yFrame-spaceFrame]
        draw.rectangle(coords, fill ='#2B9100', outline ='red')
        draw.text((xFilled[x], yFilled[x]), str(x+1), fill='#003E6B', font=font_numbers)
        draw.text((xFilled[x], yFilled[x]+(yFrame/3)), typeFilled[x], fill='black', font=font_names)

    img.show()
    img.save(direct+"\\output\\CUSTOM_SPRITE_OUTLINE.png")

def askToSaveImage():
    saveToImage = input().upper()
    if(saveToImage[0:1] == "Y"):
        print("\nSaving CUSTOM_SPRITE_OUTLINE.png...")
        drawImage()
        print("Saved! \nCheck your output folder for results!")
    elif(saveToImage[0:1] == "N"):
        print("\nImage file is discarded.")
    else:
        print("\nInvalid response. Type Y or N (or Yes/No)")
        askToSaveImage()

def exitOnPress():
    exitPress = input("\n\nPress Enter to close program...")
    exit()

def main():
    printHeader()

    global xFilled, yFilled, typeFilled, xFrame, yFrame, spaceFrame, xResolution, yResolution, frameCount, framesPerRow
    xFilled.append(0)
    yFilled.append(0)

    askSettings()

    framesPerRow = int(frameCount/6)
    for x in range(frameCount+1):
        typeFilled.append("")

    calcCoords()
    calcResolution()
    printAllCoords()

    print("\n\nTotal Spritesheet Resolution:\n " + str(xResolution) + " x " + str(yResolution))

    print("\n\nWould you like save a copy of the custom spritesheet outline guide? (CUSTOM_SPRITE_OUTLINE.png) (Y/N)")
    askToSaveImage()

    print("\nWould you like to save a copy of the custom .xml file? (CUSTOM_SPRITE.xml) (Y/N)")
    askToSaveXML()

    exitOnPress()
main()