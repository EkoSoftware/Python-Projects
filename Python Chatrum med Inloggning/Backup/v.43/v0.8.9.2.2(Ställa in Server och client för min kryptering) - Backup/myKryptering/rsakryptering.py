import rsa
import os

#site : https://www.section.io/engineering-education/rsa-encryption-and-decryption-in-python/
def myGenerateRSA():
    publicKey, privateKey = rsa.newkeys(2048)
    with open('pubKey.pem', 'wb') as file:
        file.write(publicKey.save_pkcs1('PEM'))
    with open('pvtKey.pem', 'wb') as file:
        file.write(privateKey.save_pkcs1('PEM'))

def myLoadRSA():
    with open('pubKey.pem', 'rb') as file:
        publicKey = rsa.PublicKey.load_pkcs1(file.read())
    with open('pvtKey.pem', 'rb') as file:
        privateKey = rsa.PrivateKey.load_pkcs1(file.read())
    return [privateKey, publicKey]

def myEncryptRSA(message, key):
    return rsa.encrypt(message.encode(), key)

def myDecryptRSA(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode()
    except:
        return False

if not os.path.exists('pubKey.pem') \
    and os.path.exists('pvtKey.pem'):
    myGenerateRSA()

if __name__ == '__main__':
    encMsg = myEncryptRSA("simon", myLoadRSA()[0])
    pvtKey, pubKey = myLoadRSA()
    print()
    print(encMsg)
    
    print()
    print(pubKey)
    
    print(myDecryptRSA(encMsg, pvtKey))


    
    