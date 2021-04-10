# Simplifies the editing of .xml files used in FNF spritesheets.
#
# Made my BurntBread007 on gamebanana.net
import io

def main():
    xml = open('BOYFRIEND.xml', 'r')
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

# Initializes frame variables
    xFrame = 0
    yFrame = 0
    spaceFrame = 5

# Prints Header
    print("================================================================")
    print("==        XML Editor for Friday Night Funkin (KADE)           ==")
    print("==        version 0.1, beta testing                           ==")
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
    framesPerRow = frameCount % 5
    xResolution = xFrame * framesPerRow
    yResolution = yFrame * 7

# Finds coordinates for each frame.
    framesMapped = 0
    xFilled = 0
    yFilled = 0
    for x in frameCount:
        if(xFilled < (framesPerRow*xFrame)):
            xFilled = xFilled + xFrame
        elif(xFilled >= (framesPerRow*xFrame)):
            yFilled = yFilled + yFrame
main()