import socket
import threading

all_connections = []
all_address = []

global host
global port
global s

host = "10.0.0.106"
port = 9999
s = socket.socket()

s.bind((host, port))
s.listen(3)

quantMaquinas = int(input("Quantidade de slaves: "))
auxQuantMaquinas = quantMaquinas

print("Aguardando conexões...")

while auxQuantMaquinas:
    conn, address = s.accept()
    all_connections.append(conn)
    all_address.append(address)
    print("Conexão estabelecida: " + address[0])
    auxQuantMaquinas = auxQuantMaquinas - 1

while True:
    print()
    comando = input("-> ")
    print()
    if (comando == "exit"):
        break
    elif (comando == "get"):
        for idx, conn in enumerate(all_connections):
            conn.send(comando.encode())
            dados = conn.recv(20480).decode()
            connIp, connPort = conn.getsockname()
            print(connIp + " - " + str(dados))
    elif (comando == "sync"):
        acum = 0
        cont = 0
        times = []
        for idx, conn in enumerate(all_connections):
            conn.send(comando.encode())
            timeData = conn.recv(20480).decode()
            connIp, connPort = conn.getpeername()
            print(connIp + " - " + str(timeData))
            times.append({'ip': connIp, 'conn': conn, 'timestamp': timeData})
            acum += float(timeData)
            cont += 1
        media = acum / cont

        #print('acum: ' + str(acum) + ' / cont: ' + str(cont) + ' = media: ' + str(media))

        for time in times: #Calcula a diferenca entre a media e o horario de cada maquina
            #print("media " + str(media) + ' <- timestamp -> ' + str(time['timestamp']))
            diferenca = float(media) - float(time['timestamp'])
            print(str(time['ip']) + ' -> ' + str(diferenca))
            time['conn'].send(str(diferenca).encode())