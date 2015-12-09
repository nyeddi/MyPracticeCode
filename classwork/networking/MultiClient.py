from socket import *

host = 'localhost'
name = raw_input('Enter name: ')
port = int(raw_input('Enter server port: '))
bufsiz = 1024
addr = (host, port)

tcpClient = socket(AF_INET , SOCK_STREAM)
tcpClient.connect(addr)

# sending name
tcpClient.send(name)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpClient.send(data)
raw_input('Enter to Quit')
tcpClient.close()
