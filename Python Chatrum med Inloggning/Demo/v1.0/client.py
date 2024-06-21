import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
def myLogin(client):
    while True:
        message = client.recv(1024).decode('utf-8')
        client.send(input(message).encode('utf-8'))
        message = client.recv(1024).decode('utf-8')
        client.send(input(message).encode('utf-8'))
        if client.recv(1024).decode('utf-8') == "Login successful!":
            print("Login successful!")
            break
        else:
            print("Login Failed!")
            continue

def myRegistration(client):
    while True:
        username = client.recv(1024).decode('utf-8')
        client.send(f"REGISTER {input(username)}".encode('utf-8'))
        password = client.recv(1024).decode('utf-8')
        client.send(input(password).encode('utf-8'))
        auth = client.recv(1024).decode('utf-8')
        print(auth)
        
#myLogin(client)
myRegistration(client)