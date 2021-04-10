# Alpha Version, v0.0.1
# Takes user-given width and height of a sprite, and dynamically creates
# a spritesheet resolution, along with coordinates for each type of frame.
# 
# Developed by BurntBread007
# 4/10/2021
import io

def printCoords(xFilled, yFilled, framesMapped, framesPerRow, start, stop):
    y = start
    while(y <= stop):
        print("[ "+str(xFilled[y])+", "+str(yFilled[y])+" ]", end="        ")
        framesMapped += 1
        if(framesMapped > (framesPerRow/3)):
            print("")
            framesMapped = 0
        y += 1

def main():
    xml = open('BOYFRIEND.xml', 'r')
    xml_contents = xml.read()
    xml_lines = xml_contents.split("\n")

# Line count of each type of animation
#    dead_loop     =  xml_contents.count("Dead Loop0")
#    dead_confirm  =  xml_contents.count("Dead confirm0")
#    hey           =  xml_contents.count("HEY!!0")

#    note_down     =  xml_contents.count("NOTE DOWN0")
#    note_downmiss =  xml_contents.count("NOTE DOWN MISS0")

#    note_left     =  xml_contents.count("NOTE LEFT0")
#    note_leftmiss =  xml_contents.count("NOTE LEFT MISS0")

#    note_right    =  xml_contents.count("NOTE RIGHT0")
#    note_rightmis =  xml_contents.count("NOTE RIGHT MISS0")

#    note_up       =  xml_contents.count("NOTE UP0")
#    note_upmiss   =  xml_contents.count("NOTE UP MISS0")

#    dies          =  xml_contents.count("dies0")
#    hit           =  xml_contents.count("hit0")

#    idle_dance    =  xml_contents.count("idle dance0")
#    idle_shaking  =  xml_contents.count("idle shaking0")

#    pre_attack    =  xml_contents.count("pre attack0")
#    attack        =  xml_contents.count("attack0")

#    dodge         =  xml_contents.count("dodge0")

# Initializes frame variables
    xFrame = 0
    yFrame = 0
    spaceFrame = 5

# Prints Header
    print("================================================================")
    print("==        XML Editor for Friday Night Funkin (KADE)           ==")
    print("==        version 0.0.1, alpha                                ==")
    print("================================================================")
    print("developed by BurntBread007, idea inspired from Phoxx\n")

# Asks user for frame settings
    print("Settings\n================================================================")
    print("Enter the width of your custom sprite frame:  ")
    xFrame = int(input())
    print("\nEnter the width of your custom sprite frame:  ")
    yFrame = int(input())
    print("\nChoose the spacing (in pixels) between each frame:  ")
    spaceFrame = int(input())

    xFrame = xFrame + spaceFrame
    yFrame = yFrame + spaceFrame

# Calculate file resolution, and coordinates for each frame.
    frameCount = 94
    framesPerRow = int(frameCount / 6)
    xResolution = xFrame * framesPerRow
    yResolution = yFrame * 7

# Finds coordinates for each frame.
    framesMapped = 0
    xFilled = list()
    yFilled = list()
    xFilled.append(0)
    yFilled.append(0)
    xCoord = 0
    yCoord = 0

    print("\nTotal Sheet Resolution: \n " + str(xResolution) + " x " + str(yResolution)+"\n")

    print("Coordinates for Frames:")
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
    print("Death Loop (Frames 1 - 6) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 1, 6)

    print("\n\nDeath Retry (Frames 7 - 30) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 7, 30)

    print("\n\nHey! (Frames 31 - 33) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 31, 33)

    print("\n\nDown Hits (Frames 34 - 37) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 34, 37)

    print("\n\nLeft Hits (Frames 38 - 42) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 38, 42)

    print("\n\nRight Hits (Frames 43 - 46) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 43, 46)

    print("\n\nUp Hits (Frames 47 - 50) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 47, 50)

    print("\n\nDeath Start (Frames 51 - 85) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 51, 85)

    print("\n\nIdle (Frames 86 - 90) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 86, 90)

    print("\n\nScared (Frames 91 - 94) :\n================================================================")
    printCoords(xFilled, yFilled, framesMapped, framesPerRow, 91, 94)
main()