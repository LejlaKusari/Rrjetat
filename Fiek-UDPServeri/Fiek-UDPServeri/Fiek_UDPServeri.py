from socket import*
import datetime
from random import randint
from math import factorial

serverSocket=socket(AF_INET,SOCK_DGRAM)
serverPort=9000
serverSocket.bind(('',serverPort))

def ip(addr):
    return 'IP adresa e klientit eshte ' + addr[0]

def port(addr):
    return 'Klienti eshte duke perdorur portin: ' + str(addr[1])

def zanore(fjalia):
    zanoret = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for x in fjalia.decode('utf-8'):
        if x in zanoret:
            count+=1
    return 'Teksti i derguar permban ' + str(count) + ' zanore'

def printo(fjalia):
    return fjalia

def host(par):
    # return hostname
    pass

def time(par):
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def faktoriel(par):
    factorial(int(par))

def keno(par):
    res = ''
    for i in range(20):
        res += str(randint(1,81)) + ', '
    return res   

 
kerkesat = {
    b'IP': ip,
    b'PORT': port,
    b'ZANORE': zanore,
    b'PRINTO':printo ,
    b'HOST': host,
    b'TIME': time,
    b'KENO': keno,
    b'FAKTORIEL': faktoriel ,
    b'KONVERTO': 1,
}

print("Serveri i gatshem per sherbim")

while True:
    data, clientAddress=serverSocket.recvfrom(2048)
    komanda, parametri = '', 0
    mesazhi = ''
    if b' ' in data:
        komanda, parametri = data.split()
        mesazhi = kerkesat[komanda](parametri)
    else:
        komanda = data
        mesazhi = kerkesat[komanda](clientAddress)
    if komanda in kerkesat:
        serverSocket.sendto(mesazhi.encode('utf-8'), clientAddress)
   
   