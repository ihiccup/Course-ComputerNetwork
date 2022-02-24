from socket import *
import sys


server_name = 'localhost'
server_port = 5994
server_address = (server_name, server_port)
buffer_size = 2048
err404_page_path = './page_not_found.html'

# Prepare a server socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

while True:
    print('Waiting for client...')
    connection_socket, addr = server_socket.accept()
    print(f"Client: {addr[0]}:{addr[1]}")
    try:
        message = connection_socket.recv(buffer_size).decode()
        file_name = message.split()[1]
        f = open(file_name[1:])
        output_data = f.read()

        # Send one HTTP header line into socket
        connection_socket.send("HTTP/1.1 200 OK\n".encode("utf-8"))
        connection_socket.send("Content-Type: text/html\n\n".encode('utf-8'))

        # Send the content of the requested file to the client
        connection_socket.send(output_data.encode("utf-8"))
        connection_socket.send("\n".encode("utf-8"))
        f.close()
        connection_socket.close()
    except IOError:
        f = open(err404_page_path, 'r')
        output_data = f.read()
        connection_socket.send("HTTP/1.1 404 Bad Request\n\n".encode('utf-8'))
        connection_socket.send(output_data.encode('utf-8'))
        connection_socket.send('\n'.encode('utf-8'))
        f.close()
        connection_socket.close()
    server_socket.close()
    print('Socket Closed...')
    sys.exit()
