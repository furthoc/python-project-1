#import socket module
#tcp server (sock STREAM instead of SOCK_DGRAM
from socket import *
import sys
HOST = '172.19.117.129' #local IP of host 
PORT = 9001 #arbitrary number 
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind((HOST, PORT))
while True: #while the socket/port is open
    #Establish the connection
    print('Ready to serve...')
    serverSocket.listen(5) #serves 5 connections before refusing anymore incoming connections
    connectionSocket, addr = serverSocket.accept() #acepting any incomming connections to the socket
    try:
        message = connectionSocket.recv(1024)#reciving and storing data from the socket, max size is 1024b, this is the url
        print("--------MESSAGE---------")
        print(message)
        #message is just the header of the connection
        print("--------FILENAME---------")
        filename = message.split()[1] #splits the url and finds the selected file identified by [1]
        print(filename)
        #filename is just /index.html
        print("--------F---------")
        f = open(filename[1:]) #opens the requested file (index.html)
        print(f)
        #this is the command to open the file at the selected location
        print("--------OUTPUTDATA---------")
        outputdata = f.read(1024) #storing the information from the selected file, storing 1024 bits
        print(outputdata)
        #output data is just the html code from index.html
        print("--------END LINE---------")
        #Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\r\n\r\n') #this is sending this line to to the server
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)): #sending the data from the html file to the client that is connected
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError: #for error handling, if selected file isnt found then show this
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n") #sending the error message in header format
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n") #showing the error message on the webpage
        #Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit() #Terminate the program                                   
