import socket
import threading


def read_sok(type):
    while 1 :
         data = sor.recv(1024)
         s=data.decode('utf-8')
         a=s.lower()
         if(type==1):
             print(cezarDecrypt(2,a))
         else:
             print(a)


def cezarCrypt(step,text):
    alpha = '  abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNMабвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯ0123456789'
step=1
text =input("Please write your text ").strip()
res =""
for c in text:
    res += alpha[(alpha.index(c) +step)%len(alpha)]
print('Result: "' + res + '"')


def cezarDecrypt(step,text):
    alpha = '  abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNMабвгдеєжзиіїйклмнопрстуфхцчшщьюяАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЧШЩЬЮЯ0123456789'
step=1
text =input("Please write your text ").strip()
res =""
for c in text:
    res += alpha[(alpha.index(c) +step)%len(alpha)]
print('Result: "' + res + '"')



server = '192.168.1.1',9999
alias = input("Login : ").strip()
type=int(input("Please choise 1- crypt, another  - decrypt"))
sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto((alias+' Connect to server').encode('utf-8'), server)
potok = threading.Thread(target= read_sok(type))
potok.start()
while 1 :
    mensahe = cezarCrypt(2,input())
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)