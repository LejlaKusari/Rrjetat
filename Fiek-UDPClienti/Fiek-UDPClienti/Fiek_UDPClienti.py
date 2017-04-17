from socket import*
import sys

serverName='localhost'
serverPort=9000

clientSocket=socket(family=AF_INET,type=SOCK_DGRAM)
while True:
    message= input("Jepni kerkesen:  ")
    if message == "END":
        clientSocket.close()
        break
    clientSocket.sendto(message.encode('utf-8'),(serverName,serverPort))
    modifiedMessage=clientSocket.recv(2048)
    print(modifiedMessage.decode('utf-8'))
#clientSocket.close()