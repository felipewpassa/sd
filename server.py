import socket
import threading

all_connections = []
all_address = []

global host
global port
global s

host = "127.0.0.1"
port = 9999
s = socket.socket()

s.bind((host, port))
s.listen(3)

quantMaquinas = int(input("Quantidade de maquinas: "))
auxQuantMaquinas = quantMaquinas

auxQuantMaquinas = auxQuantMaquinas - 1

print("Aguardando conexões...")

while auxQuantMaquinas:
    conn, address = s.accept()
    all_connections.append(conn)
    all_address.append(address)
    print("Conexão estabelecida: " + address[0])
    auxQuantMaquinas = auxQuantMaquinas - 1

while True:
    comando = input("-> ")
    if (comando == "exit"):
        break
    elif (comando == "get"):
        for idx, conn in enumerate(all_connections):
            conn.send(comando.encode())
            dados = conn.recv(20480).decode()
            connIp, connPort = conn.getsockname()
            print(connIp + " - " + str(dados))



