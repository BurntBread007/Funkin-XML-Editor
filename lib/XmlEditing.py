from io import FileIO
import lib.globalVars as globalVars

fileLines = list()
xml = "test.xml"
allCoords = list()

def run():
    scanXml()
    calculateFrames()
    saveXml()

def scanXml():
    global fileLines, xml
    # Opens user-given XML, saves it to both a Contents and Lines
    file = open(globalVars.direct+globalVars.userFiles+xml, "r")
    fileContents = file.read()
    fileLines = fileContents.split("\n")
    file.close()

def calculateFrames():
    global fileLines, allCoords
    globalVars.coordList = list()
    frameCount = 0

    anim = ""
    up = "UP"
    down = "DOWN"
    left = "LEFT"
    right = "RIGHT"
    hey = "HEY"
    idle = "IDLE"
    miss = "\nMISS"

    for i in range(len(fileLines)):

        # Scan 1 - Searches for unique x and y coords, as well as total number of drawn frames.
        if(fileLines[i].find("SubT") != -1):
            nameBound1 = fileLines[i].find("x=\"")
            nameBound2 = fileLines[i].find("\" w")
            frameAdd = fileLines[i][nameBound1:fileLines[i].find("\"",nameBound2)]+"\""
            allCoords.append(frameAdd)
            repeat = 'false'
            for x in range(len(globalVars.coordList)):
                if(frameAdd == globalVars.coordList[x]):
                    repeat = 'true'
            if(repeat != 'true'):
                globalVars.coordList.append(frameAdd)
                frameCount += 1

                if(up in fileLines[i].upper()):
                    anim = up
                elif(down in fileLines[i].upper()):
                    anim = down
                elif(left in fileLines[i].upper()):
                    anim = left
                elif(right in fileLines[i].upper()):
                    anim = right
                elif(hey in fileLines[i].upper()):
                    anim = hey
                elif(idle in fileLines[i].upper()):
                    anim = idle
                if(miss in fileLines[i].upper()):
                    anim = anim + miss
                globalVars.animList.append(anim)

    print(globalVars.animList)
    print(globalVars.coordList)
    print(str(frameCount) + " frames\n")
    print(globalVars.xRes)
    print(globalVars.yRes)
    print(globalVars.spaceRes)   

def saveXml():
    global xml, fileLines, allCoords

    newFile = open(globalVars.direct+globalVars.output+xml, "r")
    newFileList = list()

    firstLine = fileLines[1]
    secondLine = fileLines[2]
    name = ""
    width = int(globalVars.xRes)
    height = globalVars.yRes
    frameWidth = width+globalVars.spaceRes
    frameHeight = height+globalVars.spaceRes
    frameWidth = 0
    frameHeight = 0
    end = "/>"
    newFileList.append(firstLine)
    newFileList.append(secondLine)
    for x in range(len(fileLines)-2):
        nameBound1 = x.find("x=\"")
        nameBound2 = x.find("\" w")
        name = fileLines[nameBound1:x.find("\"",nameBound2)]+"\""
        coord = allCoords[x]
        
        currentLine = name + coord + 
        
    
    counter = 0
    newLineList = list()
    for x in fileLines:

        frameAdd = x[nameBound1:x.find("\"",nameBound2)]+"\""
        newLineList.append(x[0:nameBound1] + allCoords[counter] + " width=\""+str(globalVars.xRes)+"\" height=\""+str(globalVars.yRes)+"\" frameX=\""+str(0)+"\" frameY=\""+str(0)+"\" frameWidth=\""+str(globalVars.spaceRes+globalVars.xRes)+"\" frameHeight=\""+str(globalVars.spaceRes+globalVars.yRes)+"\"/>")
        print(newLineList[counter])
        counter += 1
    for y in newLineList:
        newFile.writelines(y)
        print(y)
    newFile.close()

def waitforFile():
    print("\nNow place the XML file you want to edit into this program's \"input\" folder.\nPress enter to continue...")
    wait = input()