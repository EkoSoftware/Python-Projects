from sys import argv
import os
from time import sleep

# Globals
nlines = 0
foundwords = 0
foundlines = 0
red = "\x1b[0;31m"
white = "\x1b[0;37m"

class Line():
    def __init__(self, row, line:list):
        self.col = 0
        self.maxcol = len(line)
        self.animating_lines = list()
        
    def next(self):
        if self.col < self.maxcol:
            self.col += 1
            index = self.line[self.col]
            self.animating_lines.append(index)

    def get_lines(self) -> list:
        return self.animating_lines
    
            
        

def DepthFirstSearch(lines:list) -> None:
    global nlines, foundlines, foundwords, red, white
    
    for line in lines:
        nlines += 1
        if find in line: 
            foundlines += 1
        line = line.split()
        for word in line:
            if word == find:
                foundwords += 1
                for char in word:
                    print(f'{red}{char}', end='', flush=True)
                print(" ",end='')
            else:
                for char in word:
                    print(f'{white}{char}', end='',flush=True)
                print(" ",end='')

            sleep(0.010)
            if word is line[-1]:
                print()
        

def BreadthFirstSearch(lines:list) -> None:
    global nlines, foundlines, foundwords, red, white
    

# Main 
os.system("clear")
if len(argv) != 3:
    print(f'Usage: python3.12 mygrep.py "FIND" "PATH"'); 
    exit(1)

find = argv[1]
path = argv[2]

if not os.path.exists(path):
    print(f'{path} doesnt exist ( Wrong path? )')
    exit(1)

# Search begins here
lines = list()
with open(path, 'r') as file:
    lines = file.readlines()

DepthFirstSearch(lines)



# End Stats
print()
print(f'Lines read {nlines}')
print(f'Matching lines {foundlines}')
print(f'Matching words {foundwords}')
    


        
