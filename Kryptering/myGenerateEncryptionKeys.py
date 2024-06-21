from cryptography.fernet import Fernet
from time import localtime

def generateKeys(path='myFernetKeys.txt',string=True):

    if string: 
        writemode, encoding = 'x', 'w'
    else: 
        writemode, encoding = 'x+b', 'wb'
        path = path[:-4] + 'ByteFile' + '.txt'
    
    try:
        open(path, writemode).close()
    except FileExistsError:
        while True:
            uinput = input("You are about to overwrite existing keys\nDo you want to continue? Yes/No\n>").strip().title()
            match uinput[0]:
                case "Y": break
                case "N" : return print('Key generation was cancelled by the user.')
                case _____: continue
                
    with open(path, encoding) as file:
        for day in range(1,32):
            key = Fernet.generate_key()
            match encoding:
                case 'w' : file.write(f'Day: {day:2} Key: {key}.\n')
                case 'wb': file.write(key);file.write(b'\n')
            
    
    return print(f'Keys written to path {path}')




def readKeys(path='myFernetKeys.txt', string=True):
    
    year,month,day,hour,minute,second,_,_,_ = localtime()

    #try:
    if string:
        with open(path) as file:
            lines = file.readlines()
            today = lines[day-1]
            key = today.split()[-1]
            return key 
            

    else:
        with open(path, 'rb') as file:
            lines = file.readlines()
            return lines[day-1]
    

if __name__ == '__main__':
    generateKeys()
    #print(readKeys())
    
    
    #generateKeys(path='myFernetKeys.txt',string=False)
    #print(readKeys('myFernetKeysByteFile.txt',string=False))
    
    #from time import localtime
    #print(localtime())