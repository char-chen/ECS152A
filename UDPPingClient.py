
# Charles Chen, Will Wu
# 912054270, 912082297
import random
import time
from socket import *

UDP_Addr = ('127.0.0.1', 12000)
#similar to the server set up
#set up a socket
client = socket(AF_INET, SOCK_DGRAM)
client.settimeout(1)

#Monday to Sunday
wDays =  ['M', 'T', 'W', 'R', 'F', 'S', 'U']

for i in range(1,11):
    currTime = time.gmtime()
    message = "Ping " + str(i) + " " + str(currTime.tm_year) + "-" + str(currTime.tm_mon) + "-" + \
              str(currTime.tm_mday) + " " + wDays[currTime.tm_wday] + " " + \
              str(currTime.tm_hour) + ":" + str(currTime.tm_min) + " UTC"
    print(message)
    start = time.time()
    client.sendto(message.encode(),UDP_Addr)
    try:
        data , addr = client.recvfrom(1024)
        end = time.time()
        print(data)
        rttTime = "RTT: " + str((end- start)*1000)
        print(rttTime)
        #print a new line
        print("")
    except timeout:
        print("Request timed out")
        print("")
        continue
    
client.close()
