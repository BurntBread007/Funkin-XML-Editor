from PIL import ImageDraw, Image, ImageFont, features
import lib.globalVars as globalVars

xFill = 0
yFill = 0

xResolution = 0
yResolution = 0

xCoords = list()
yCoords = list()

framesPerRow = 0

def run():
    global xFill, yFill
    xFill = globalVars.xRes+globalVars.spaceRes
    yFill = globalVars.yRes+globalVars.spaceRes
    calcResolution()
    calcCoords()
    drawCoords()

def calcResolution():
    global xFill, yFill, xResolution, yResolution, framesPerRow
    framesPerRow = int((globalVars.frameCount / 6)+1)
    xResolution = xFill * framesPerRow
    yResolution = (yFill * 7)
    print("Xresolution" + str(xResolution))
    print("Yresolution" + str(yResolution))
    
def calcCoords():
    global xFill, yFill, xCoords, yCoords, framesPerRow
    xCo = 0
    yCo = 0
    frameInRow = 0
    for x in range(globalVars.frameCount):
        xCoords.append(xCo)
        yCoords.append(yCo)
        xCo += xFill
        frameInRow += 1
        if(frameInRow >= framesPerRow):
            yCo += yFill
            xCo = 0
            frameInRow = 0

def drawCoords():
    global xResolution, yResolution, xFill, xFill, xCoords, yCoords
    spaceRes = globalVars.spaceRes

    img = Image.new('RGBA', (xResolution, yResolution), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    numberSize = int(yFill / 3)
    numberFont = ImageFont.truetype('arial.ttf', numberSize)

    if(xFill >= yFill):
        nameSize = int(yFill / 4)
    else:
        nameSize = int(xFill / 3.5)
    nameFont = ImageFont.truetype('arial.ttf', nameSize)

    for x in range((globalVars.frameCount)):
        coords = [xCoords[x], yCoords[x], xCoords[x]+xFill-spaceRes, yCoords[x]+yFill-spaceRes]
        draw.rectangle(coords, fill ='#2B9100', outline ='red')
        draw.text((xCoords[x], yCoords[x]), str(x+1), fill='#003E6B', font=numberFont)
        if(globalVars.usingXml == 'true'):
            draw.text((xCoords[x], yCoords[x]+(yFill/3)), globalVars.animList[x], fill='black', font=nameFont)

    img.show()
    img.save(globalVars.direct+"\\output\\CUSTOM_SPRITE_OUTLINE.png")