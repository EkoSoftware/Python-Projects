import socket

SERVER_IP = '192.168.1.20'  # Change this to your server's IP address
SERVER_PORT = 7890  # Change this to the port your server is listening on

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        message = input("Enter message to send: ")
        #message = message + '\0'
        # Send message to server
        client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

        # Receive response from server
        data, server_address = client_socket.recvfrom(1024)
        print("Received from server:", data.decode())

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()