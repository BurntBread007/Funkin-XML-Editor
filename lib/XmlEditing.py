from io import FileIO
import lib.GlobalVars as GlobalVars

def run():
    scanXml()

def scanXml():
    dir = GlobalVars.direct
    xml = "test.xml"
    
    # Opens user-given XML, saves it to both a Contents and Lines
    file = open(dir+GlobalVars.userFiles+xml, "r")
    fileContents = file.read()
    fileLines = fileContents.split("\n")
    file.close()
    
    newFile = open(dir+GlobalVars.output+xml, "r")
    newFileList = list()
    newFileList = fileLines
    animType = list()
    
    for i in range(len(fileLines)):
        up = "UP"
        down = "DOWN"
        left = "LEFT"
        right = "RIGHT"
        hey = "HEY"
        idle = "IDLE"
        miss = " MISS"

        anim = ""
        if(up in newFileList[i].upper()):
            anim = up
        elif(down in newFileList[i].upper()):
            anim = down
        elif(left in newFileList[i].upper()):
            anim = left
        elif(right in newFileList[i].upper()):
            anim = right
        elif(hey in newFileList[i].upper()):
            anim = hey
        elif(idle in newFileList[i].upper()):
            anim = idle
        if(miss in newFileList[i].upper()):
            anim = anim + miss
        animType.append(anim)

    print(animType)
    newFile.close()