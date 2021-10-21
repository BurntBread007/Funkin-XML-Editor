from PIL import ImageDraw, Image, ImageFont, features
import lib.globalVars as globalVars
import array

xFill = 0
yFill = 0
#xResolution = 0
#yResolution = 0

def run():
    global xFill, yFill
    xFill = globalVars.xRes+globalVars.spaceRes
    yFill = globalVars.yRes+globalVars.spaceRes
    calcResolution()
    #calcCoords()

def calcResolution():
    global xFill, yFill
    framesPerRow = int(globalVars.frameCount / 6)
    xResolution = xFill * framesPerRow
    yResolution = yFill * 7
    print(xFill)
    print(xResolution)
    print(yFill)
    print(yResolution)

def calcCoords():
    global xFill, yFill
    xCoords = list()
    yCoords = list()
    xCo = 0
    yCo = 0
    frameInRow = 0
    for x in range(globalVars.frameCount):
        xCoords[x] = xCo
        yCoords[x] = yCo
        xCo += xFill
        frameInRow += 1
        #if(frameInRow >= framesPerRow):
        #    yCo += yFill
        #    xCo = 0
        print(xCoords[x])
        print(yCoords[x])