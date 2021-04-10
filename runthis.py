# Alpha Version, v0.0.2
# Takes user-given width and height of a sprite, and dynamically creates
# a spritesheet resolution, along with coordinates for each type of frame.
# 
# Developed by BurntBread007
# 4/10/2021
import io
import os

def printHeader():
    print("\n================================================================")
    print("==      Spritesheet Creator for Friday Night Funkin           ==")
    print("==      version 0.0.2, alpha                                  ==")
    print("================================================================")
    print("developed by BurntBread007, idea inspired from Phoxx\n")

def printAllCoords(bar, xFilled, yFilled, framesMapped, framesPerRow):
    print("\n\nCoordinates for Frames:\n")

    print("Death Loop (Frames 1 - 6) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 1, 6)
    print("\n\nDeath Retry (Frames 7 - 30) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 7, 30)
    print("\n\nHey! (Frames 31 - 33) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 31, 33)
    print("\n\nDown Hits (Frames 34 - 37) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 34, 37)
    print("\n\nLeft Hits (Frames 38 - 42) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 38, 42)
    print("\n\nRight Hits (Frames 43 - 46) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 43, 46)
    print("\n\nUp Hits (Frames 47 - 50) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 47, 50)
    print("\n\nDeath Start (Frames 51 - 85) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 51, 85)
    print("\n\nIdle (Frames 86 - 90) :")
    print(bar)
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 86, 90)
    print("\n\nScared (Frames 91 - 94) :")
    print(bar)
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

def writeAllCoords(xFilled, yFilled, framesMapped, framesPerRow, savefile):
    savefile.write("Coordinates for Frames:\n")

    savefile.write("\nDeath Loop (Frames 1 - 6) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 1, 6, savefile)
    savefile.write("\n\nDeath Retry (Frames 7 - 30) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 7, 30, savefile)
    savefile.write("\n\nHey! (Frames 31 - 33) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 31, 33, savefile)
    savefile.write("\n\nDown Hits (Frames 34 - 37) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 34, 37, savefile)
    savefile.write("\n\nLeft Hits (Frames 38 - 42) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 38, 42, savefile)
    savefile.write("\n\nRight Hits (Frames 43 - 46) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 43, 46, savefile)
    savefile.write("\n\nUp Hits (Frames 47 - 50) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 47, 50, savefile)
    savefile.write("\n\nDeath Start (Frames 51 - 85) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 51, 85, savefile)
    savefile.write("\n\nIdle (Frames 86 - 90) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 86, 90, savefile)
    savefile.write("\n\nScared (Frames 91 - 94) :\n")
    writeCoords(xFilled, yFilled, framesMapped, framesPerRow, 91, 94, savefile)

    print("\nResults were successfully written to spritesheet_coordinates.txt!")

def writeCoords(xFilled, yFilled, framesMapped, framesPerRow, start, stop, savefile):
    y = start
    while(y <= stop):
        savefile.write("[ "+str(xFilled[y])+", "+str(yFilled[y])+" ] \n")
        framesMapped += 1
        if(framesMapped > (framesPerRow/3)):
            savefile.write("")
            framesMapped = 0
        y += 1

def calcCoords(xFilled, yFilled, xCoord, yCoord, xFrame, yFrame, frameCount, framesPerRow):
    for x in range(frameCount):
        if(xFilled[x] < (framesPerRow*xFrame)):
            xCoord += xFrame
            xFilled.append(xCoord)
            yFilled.append(yCoord)
        elif(xFilled[x] >= (framesPerRow*xFrame)):
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
    return xFrame,yFrame

def editXML(direct):
    xml = open(direct+"\\source\\BOYFRIEND.xml", "r")
    xml_contents = xml.read()
    xml_lines = xml_contents.split("\n")

    # Line count of each type of animation
    dead_loop     =  xml_contents.count("Dead Loop0")
    dead_confirm  =  xml_contents.count("Dead confirm0")
    hey           =  xml_contents.count("HEY!!0")
    note_down     =  xml_contents.count("NOTE DOWN0")
    note_downmiss =  xml_contents.count("NOTE DOWN MISS0")
    note_left     =  xml_contents.count("NOTE LEFT0")
    note_leftmiss =  xml_contents.count("NOTE LEFT MISS0")
    note_right    =  xml_contents.count("NOTE RIGHT0")
    note_rightmis =  xml_contents.count("NOTE RIGHT MISS0")
    note_up       =  xml_contents.count("NOTE UP0")
    note_upmiss   =  xml_contents.count("NOTE UP MISS0")
    dies          =  xml_contents.count("dies0")
    hit           =  xml_contents.count("hit0")
    idle_dance    =  xml_contents.count("idle dance0")
    idle_shaking  =  xml_contents.count("idle shaking0")
    pre_attack    =  xml_contents.count("pre attack0")
    attack        =  xml_contents.count("attack0")
    dodge         =  xml_contents.count("dodge0")

def exitOnPress():
    exitPress = input("\n\nPress Enter to close program...")
    exit()

def main():
    direct = os.getcwd()
    # String Variables to save codespace.
    bar = "================================================================"

    # Variables for sprite data.
    xFrame = 0
    yFrame = 0
    spaceFrame = 5
    frameCount = 94
    framesPerRow = int(frameCount / 6)

    # Variables for mapping frames onto spritesheet.
    framesMapped = 0
    xFilled = list()
    yFilled = list()
    xFilled.append(0)
    yFilled.append(0)
    xCoord = 0
    yCoord = 0

    printHeader()
    xFrame,yFrame = askSettings()

    calcCoords(xFilled, yFilled, xCoord, yCoord, xFrame, yFrame, frameCount, framesPerRow)
    printAllCoords(bar, xFilled, yFilled, framesMapped, framesPerRow)
    calcResolution(xFrame, yFrame, framesPerRow)
    
    print("\nWould you like to save these results to a .txt file? (Y/N)")
    saveToFile = input().upper()
    if(saveToFile == "Y"):
        savefile = open(direct+"\\output\\spritesheet_coordinates.txt", "w")
        writeAllCoords(xFilled, yFilled, framesMapped, framesPerRow, savefile)
        savefile.close()
    elif(saveToFile == "N"):
        print("\nNo file has been created.")

    exitOnPress()
main()