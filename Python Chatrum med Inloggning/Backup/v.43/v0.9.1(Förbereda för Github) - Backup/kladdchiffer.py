def myCipher(text, key):
    encryption = ''
    while len(key) < len(text):
        key += key
    key = key[:len(text)]
    print(f'Key adjusted for message: "{key}"')
    
    for i, char in enumerate(text):
        value = ord(char) + ord(key[i])
        encryption += chr(value)
    
    return encryption

def myDecipher(text, key):
    decryption = ''
    while len(key) < len(text):
        key += key
    key = key[:len(text)]
    
    for i, char in enumerate(text):
        value = ord(char) - ord(key[i])
        decryption += chr(value)

    return decryption


if __name__ == '__main__':
    key = 'Tjenare Mannen'
    #from myEncryption import myGetEncryptionKey
    #key = myGetEncryptionKey(len(uinput))
    while True:
        uinput = input("Message to encrypt\n>")
        print(f'key : {key}')
        enc = myCipher(uinput, key)
        print(f'Encrypted message:\n{enc}')
        
        dec = myDecipher(enc, key)
        print(f'Deciphered message:\n{dec}')
        
        #uinput = input("Message to decrypt\n>")