from socket import *
import sys
serverName='localhost'
serverPort=9000

clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    message=input("Jepni kerkesen: ")
    if message=="END":
        clientSocket.cloOse()
        break
    clientSocket.send(message.encode('utf-8'))
    modifiedMessage=clientSocket.recv(1024)
    print("From Server:", modifiedMessage.decode('utf-8'))
    clientSocket.close()
    break