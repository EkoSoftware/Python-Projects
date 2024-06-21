import socket
import os
import threading

SERVER_IP = '192.168.1.162'
SERVER_PORT = 7890  

def receive_messages(client_socket):
      while True:
          data, server_address = client_socket.recvfrom(1024)
          
          servermessage = data.decode()
          for i in servermessage: 
            if i == '\n': 
              i = ' '
          servermessage = servermessage[:-3] + "<(Server)\n"
          print(f"{servermessage:>50}Send>", end="")
          


def send_messages(client_socket):
      print("Send>", end="")
      while True:
          message = input()
          client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()
    
    receive_thread.join()
    send_thread.join()


    client_socket.close()
    




if __name__ == "__main__":
    main()
    