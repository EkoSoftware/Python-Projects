from sys import argv
import os

def colorword(word:str, color="Red")-> str:
    colors  = {
        "Black":"\x1b[0;30m",
        "Red":"\x1b[0;31m",
        "Green":"\x1b[0;32m",
        "Yellow":"\x1b[0;33m",
        "Blue":"\x1b[0;34m",
        "Purple":"\x1b[0;35m",
        "Cyan":"\x1b[0;36m",
        "White":"\x1b[0;37m"
    }
    if color not in colors:
        return None
    
    result = colors[color] + word[:] + colors["White"]
    return result


if len(argv) != 3:
    print(f'Usage: python3.12 mygrep.py "FIND" "PATH"'); 
    exit(1)
    

find = argv[1]
path = argv[2]

if not os.path.exists(path):
    print(f'{path} doesnt exist ( Wrong path? )')
    exit(1)
    


# Main function
#while True:
#    userinput = input()
#    word = userinput.split()[0]
#    try:
#        choice = userinput.split()[1].title()
#    except IndexError:
#        print(word)
#        continue
#
#    print(colorword(word, color=choice))

with open(path, 'r') as file:
    lines = file.readlines()
    newlines = list()
    nlines = 0
    foundlines = 0
    foundwords = 0

    
    for line in lines:
        newlinelist = list()
        nlines += 1
        if find in line: 
            for word in line.split():
                if find in word:
                    newlinelist.append(colorword(word))
                    foundwords += 1
                    print(colorword(word))
                else:
                    newlinelist.append(word)
            foundlines += 1
            
            newlinestring = " ".join(newlinelist)
            newlines.append(newlinestring)
            print(f'Line[{nlines}]: {newlinestring}')
        
    
# End Stats
    print()
    print(f'Lines read {nlines}')
    print(f'Matching lines {foundlines}')
    print(f'Matching words {foundwords}')
    

        
