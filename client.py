import socket
from datetime import datetime

host = '127.0.0.1'
port = 9999
s = socket.socket()

s.connect((host, port))

print("Conectado! Pronto para receber dados...")
while True:
    comandoRemoto = s.recv(20480).decode()
    print("\nComando recebido: " + comandoRemoto)

    if (comandoRemoto == "get"):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        s.send(str(timestamp).encode())
        print("Resposta: " + str(timestamp) + " -> " + str(now.strftime("%H:%M:%S")) + "\n")
    elif (comandoRemoto == "sync"):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        s.send(str(timestamp).encode())
        print("Resposta: " + str(timestamp) + " -> " + str(now.strftime("%H:%M:%S")) + "\n")
        ajusteTime = s.recv(20480).decode()
        print("Ajustar o time em: " + str(ajusteTime))