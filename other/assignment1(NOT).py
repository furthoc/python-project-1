#import socket module
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000 #Prepare a sever socket
serverSocket.bind(('192.168.0.15' , serverPort))#Fill in start
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    serverSocket.listen(5)
    connectionSocket,addr = serverSocket.accept()
    try:

        message = connectionSocket.recv(1024)  #Fill in start          #Fill in end

        filename = message.split()[1] #returns the 2nd value and assigns to filename
        f = open(filename[1:])
        outputdata = f.read(1024)


        #Send one HTTP header line into socket
        #fill in start
        connectionSocket.send('HTTP/1.1 200\nContent-Type: text/html\r\n\r\n')
        #fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #fill in start
        connectionSocket.send("HTTP/1.1 404 not found\r\n\r\n") 
        connectionSocket.send("<html><head></head><body><h1>404 not found</h1></body></html>\r\n")
        #fill in end
        #Close client socket
        #fill in start
        connectionSocket.close()   
        #fill in end        
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    