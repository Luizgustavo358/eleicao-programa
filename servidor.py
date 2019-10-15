'''-----------------------------------------|
|             Trabalho de LRSO              |
|-------------------------------------------|
| Dupla: Luiz Gustavo Bragança dos Santos   |
|        Pedro Augusto Prosdocimi           |
|-------------------------------------------'''

# imports
import _thread
import queue
import socket
import threading

# endereco IP do servidor
HOST = ''

# Porta do servidor
PORT = 8000

# variaveis globais
candidatos = []
votos = []
thread_lock = threading.Lock()

if __name__ == "__main__":
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    origem = (HOST, PORT)
