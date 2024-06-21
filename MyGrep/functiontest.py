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
    
    result = colors[color] + word[:]
    return result


print(
    "Black\n"
    "Red\n"
    "Green\n"
    "Yellow\n"
    "Blue\n"
    "Purple\n"
    "Cyan\n"
    "White\n"
    "Usage: WORD COLOR\n")
while True:
    userinput = input()
    word = userinput.split()[0]
    try:
        choice = userinput.split()[1].title()
    except IndexError:
        print(word)
        continue

    print(colorword(word, color=choice))
