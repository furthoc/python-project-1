from socket import *
import sys
#taking the argument from the command line
server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]
#setting where we are going to connect, the % wasnt used as it was no needed
hostport = server_host, server_port
#start trying to connect
try:
	client_socket = socket(AF_INET,SOCK_STREAM) #setup a socket for the server to pass data through to
	client_socket.connect((server_host,int(server_port)))
	header = { #creating our own header as we are looking for a specific file we need to define the file in the get 
	"first_header" : "GET /%s HTTP/1.1" %(filename),
	"Host": hostport,
	}
	http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header) #combining and sending the header to the server 
	print http_header #to see what it looks like
	client_socket.send("%s\r\n\r\n" %(http_header))
#if there is an error while running that isnt to do with what file we are looking for, then shut down the client 
except IOError:

	sys.exit()
final="" #empty variable to store the outputs of the file in
response_message=client_socket.recv(1024)
while response_message: #while we are receiving data 
	final += response_message #add the received data line by line into the empty final variable
	response_message = client_socket.recv(1024)

client_socket.close() #close the socket when all lines are copied into the varible
print "final:",final #print the variable