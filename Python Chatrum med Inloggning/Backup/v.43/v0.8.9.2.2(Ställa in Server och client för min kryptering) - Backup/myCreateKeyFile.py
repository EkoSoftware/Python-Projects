from time import localtime
from myEncryption import myGetEncryptionKey


def myGenerateKeys(path='myKeys.txt'):    
    try:
        open(path, 'x+b').close()
    except FileExistsError:
        while True:
            uinput = input("You are about to overwrite existing keys\nDo you want to continue? Yes/No\n>").strip().title()
            match uinput[0]:
                case "Y": break
                case "N": return print('Key generation was cancelled by the user.')
                case ___: continue
                
    with open(path, 'wb') as file:
        for day in range(1,32):
            key = myGetEncryptionKey(1024).encode()
            file.write(key+b'\n')
            
            
    return print(f'Keys written to path {path}')
            
            
def myReadKeys(path='myKeys.txt'):
    year,month,day,hour,minute,second,_,_,_ = localtime()
    try:
        open(path,'rb').close()
    except FileNotFoundError:
        myGenerateKeys()
        
    with open(path, 'rb') as file:
        lines = file.readlines()
        today = lines[day-1]
        key = today.split()[-1]
        return key
    

if __name__ == '__main__':
    myGenerateKeys()
    print(f'Todays key:\n{myReadKeys()}')