#myFernetKey = b'q7qDPOZInGtw50dngbM3MZdVKejQFzYPrURqaks5kxU='
#myFernetCipher = Fernet(myFernetKey)

def mySend(text, *password):
    if password:
        password = str(password)
        password = myFernetCipher.encrypt(password.encode())
        password = hashlib.sha3_256(password).hexdigest()
        return client.send(password)
    else:
        text = text.encode()
        text = myFernetCipher.encrypt(text)
        return client.send(text)