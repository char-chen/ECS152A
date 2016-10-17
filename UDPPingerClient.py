
import random
import time
from socket import *

UDP_Addr = ('128.120.211.98', 24001)

#similar to the server set up
#set up a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1,10):
    message = "Hello Host!!!"
    clientSocket.sendto(message.encode(), UDP_Addr)

#timeout
#listener
while True:
    reply, addr = clientSocket.recvfrom(1024)
    print (reply)

clientSocket.close()
