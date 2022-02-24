from socket import *


buffer_size = 4096
server_name = 'localhost'
server_port = 5994
server_address = (server_name, server_port)
client_request = 'GET /index.html HTTP/1.1\n'

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(server_address)

client_socket.send(client_request.encode('utf-8'))
message = client_socket.recv(buffer_size)
print(message.decode())
client_socket.close()
print('Done...')
