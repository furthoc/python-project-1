from socket import *
import sys

server_host = sys.argv[1]
server_port = sys.argv[2]
filename = sys.argv[3]

hostport = server_host, server_port

try:
	client_socket = socket(AF_INET,SOCK_STREAM)
	client_socket.connect((server_host,int(server_port)))
	header = {
	"first_header" : "GET /%s HTTP/1.1" %(filename),
	"Host": hostport,
	}
	http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
	print http_header
	client_socket.send("%s\r\n\r\n" %(http_header))

except IOError:

	sys.exit()
final=""
response_message=client_socket.recv(1024)
while response_message:
	final += response_message
	response_message = client_socket.recv(1024)

client_socket.close()
print "final:",final