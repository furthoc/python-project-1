#python 2.x
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('172.19.117.196',9001))
serverSocket.listen(1)
while True:
    print("ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        #send one HTTP header line into socket
        connectionSocket.send("\nHTTP/1.1 200 OK\r\n")
        connectionSocket.send(outputdata)
        #send the content of the reqested file to the client
        #sends actual HTML file to the user
        for i in range (0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        outputdata = '404 not found'
        connectionSocket.send(outputdata)
        connectionSocket.send("\nHTTP/1.1 404 not found\r\n\r\n")
        print("\nHTTP 1.1 404 not found\r\n\r\n")
        connectionSocket.close()
    #close client socket
    #fill in
    #fill in
serverSocket.close()
sys.exit() #terminates program
