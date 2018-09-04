#
# UPD Pinger client.
#
import time
from socket import *

pings = 1

# Send ping 10 times.
for pings in range(10):

    # Create a UDP socket.
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Set a timeout value of 1 second.
    clientSocket.settimeout(1)

    # Ping to server
    message = 'test'

    # Define address and port.
    addr = ('172.19.117.196', 12000)

    # Send ping.
    start = time.time()
    clientSocket.sendto(message, addr)

    # If data is received back from server, print.
    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print '{0} {1} {2}'.format(data, pings, elapsed)

    # If data is not received back from server, print it has timed out.
    except timeout:
        print 'REQUEST TIMED OUT'

it = raw_input("press any key to close: ")
