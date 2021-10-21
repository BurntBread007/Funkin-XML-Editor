from io import FileIO
import lib.globalVars as globalVars

fileLines = list()
xml = "test.xml"

def run():
    scanXml()
    calculateFrames()
    #saveXml()

def scanXml():
    global fileLines, xml
    # Opens user-given XML, saves it to both a Contents and Lines
    file = open(globalVars.direct+globalVars.userFiles+xml, "r")
    fileContents = file.read()
    fileLines = fileContents.split("\n")
    file.close()

def calculateFrames():
    coordList = list()
    animList = list()
    frameCount = 0

    anim = ""
    up = "UP"
    down = "DOWN"
    left = "LEFT"
    right = "RIGHT"
    hey = "HEY"
    idle = "IDLE"
    miss = " MISS"

    for i in range(len(fileLines)):

        # Scan 1 - Searches for unique x and y coords, as well as total number of drawn frames.
        if(fileLines[i].find("SubT") != -1):
            nameBound1 = fileLines[i].find("x=\"")
            nameBound2 = fileLines[i].find("\" w")
            frameAdd = fileLines[i][nameBound1:fileLines[i].find("\"",nameBound2)]+"\""
            repeat = 'false'
            for x in range(len(coordList)):
                if(frameAdd == coordList[x]):
                    repeat = 'true'
            if(repeat != 'true'):
                coordList.append(frameAdd)
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
            animList.append(anim)

    for y in range(len(fileLines)):
        pass
    print(animList)
    print(coordList)
    print(str(frameCount) + " frames\n\n")
    print(globalVars.xRes)
    print(globalVars.yRes)
    print(globalVars.spaceRes)

def saveXml(fileLines):
    global xml

    newFile = open(dir+globalVars.output+xml, "r")
    newFileList = list()
    newFileList = fileLines
    newFile.close()