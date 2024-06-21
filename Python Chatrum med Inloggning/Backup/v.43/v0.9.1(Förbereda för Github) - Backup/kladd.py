def myCipher(text, key, salt=0):
    encryption = ''
    while len(key) < len(text):
        key += key
    key = key[:len(text)]
    print(f'Key adjusted for message: "{key}"')
    
    for i, char in enumerate(text):
        value = ord(char) + ord(key[i])
        if salt: value += salt
        encryption += chr(value)
    
    return encryption.encode()

def myDecipher(text, key, salt=0):
    decryption = ''
    while len(key) < len(text):
        key += key
    key = key[:len(text)]
    
    for i, char in enumerate(text):
        value = ord(char) - ord(key[i])
        if salt: value -= salt
        decryption += chr(value)

    return decryption


while True:
    key = input("Write your key to use for encryption\n>")
    print(f'key : {key}')
    uinput = input("Message to encrypt\n>")
    enc = myCipher(uinput, key, 1337)
    print(f'Encrypted message:\n{enc}')
    dec = myDecipher(enc, key, 1337)
    print(f'Deciphered message:\n{dec}')
    
    #uinput = input("Message to decrypt\n>")
    

    

