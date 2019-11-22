import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind (('192.168.1.1',9999))
client = []
print ('Start Server')
while True :
         data , addres = sock.recvfrom(1024)
         print (addres[0], addres[1])
         if  addres not in client :
                 client.append(addres)
         for clients in client :
                 if clients == addres:
                     continue
                 sock.sendto(data,clients)