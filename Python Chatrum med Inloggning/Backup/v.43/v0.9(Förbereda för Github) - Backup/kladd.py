def myCipher(string, key):
    for i, char in enumerate(string):
        match char:
            case 'å': char.replace('å','aoaoaoao')
            case 'ä': char.replace('ä','aeaeaeae')
            case 'ö': char.replace('ö','oeoeoeoe')
    
    length = len(key)
    keyBytes = key.encode('utf-8')
    strBytes = string.encode('utf-8')
    
    encryption = []
    for i, byte in enumerate(strBytes):
        keyByte = keyBytes[i % length]
        cryptedByte = (byte + keyByte) % 256
        encryption.append(cryptedByte)
    
    return bytes(encryption)
    
def myDecipher(string, key):
    length = len(key)
    keyBytes = key.encode('utf-8')
    strBytes = string

    decryption = []
    for i, byte in enumerate(strBytes):
        keyByte = keyBytes[i % length]
        decryptedByte = (byte - keyByte) % 256
        decryption.append(decryptedByte)

    decrypted_String = [chr(x) for x in decryption]
    text = ''.join(decrypted_String)
    
    for i, char in enumerate(string):
        match char:
            case 'aoaoaoao': char.replace('aoaoaoao','å')
            case 'aeaeaeae': char.replace('aeaeaeae','ä')
            case 'oeoeoeoe': char.replace('oeoeoeoe','ö')
    
    return text

if __name__ == '__main__':
    from myEncryption import myGetEncryptionKey
    key = myGetEncryptionKey(1024)
    print(f'key : {key}')
    
    while True:
        uinput = input("Message to encrypt\n>")
        enc = myCipher(uinput, key)
        print(f'Encrypted message:\n{enc}')
        dec = myDecipher(enc, key)
        print(f'Deciphered message:\n{dec}')
        
        #uinput = input("Message to decrypt\n>")