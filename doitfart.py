

def main():
    space = " "
    item = "o"
    buffer = ""
    
    for x in range(2):
        spacing = ""
        for y in range(50):
            spacing += space
            buffer = spacing + item
            print(buffer)
        for z in range(50):
            spacing -= space
            buffer = item + spacing
            print(buffer)       
main()