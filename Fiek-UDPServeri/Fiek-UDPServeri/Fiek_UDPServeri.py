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
        if x.lower() in zanoret:
            count+=1
    return 'Teksti i derguar permban ' + str(count) + ' zanore'

def printo(fjalia):
    return (fjalia.decode('utf-8'))

def host(par):
    return gethostbyaddr(par[0])[0]

def time(par):
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def faktoriel(par):
    return str(factorial(int(par)))

def keno(par):
    numbers = []
    for i in range(20):
        numbers.append(str(randint(1,81)))
    return ", ".join(numbers) 
#LEJLA
def bashketingellore(fjalia):
    bashketingelloret={'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','z',}
    count=0
    for x in fjalia.decode('utf-8'):
        if x in bashketingelloret:
            count+=1
    return 'Teksti i derguar permbane ' + str(count) + ' bashketingellore'

def reverse(par):
    par=par.decode('utf-8')
    fjalia=[]
    index = len(par)
    while index:
        index -= 1                    # index = index - 1
        fjalia.append(par[index])        
    return ''.join(fjalia)


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
    b'BASHKETINGELLORE' : bashketingellore ,
    b'REVERSE' : reverse ,
}

print("Serveri i gatshem per sherbim")

while True:
    data, clientAddress=serverSocket.recvfrom(2048)
    if b' ' in data:
        data=data.split()
        komanda=data[0]
        parametri=(b' '.join(data[1:]))
        if komanda==b'FAKTORIEL' and b' ' in parametri:
            mesazhi= "Shume parametra"
        elif komanda in kerkesat:
            mesazhi = kerkesat[komanda](parametri)
        else:
            mesazhi = "Kerkese jo valide."
    else:
        komanda=data
        if komanda in kerkesat:
            mesazhi = kerkesat[komanda](clientAddress)
        else:
            mesazhi = "Kerkese jo valide."
    serverSocket.sendto(mesazhi.encode('utf-8'), clientAddress )
    print("U dergua mesazhi '{}' te klienti {}:{}".format(mesazhi,clientAddress[0],clientAddress[1]))