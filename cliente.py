'''-----------------------------------------|
|             Trabalho de LRSO              |
|-------------------------------------------|
| Dupla: Luiz Gustavo Bragança dos Santos   |
|        Pedro Augusto Prosdocimi           |
|-------------------------------------------'''

# imports
import votar_ui
import socket
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# endereco IP do servidor
HOST = '127.0.0.1'

# Porta do servidor
PORT = 8000

#  difinindo variaveis globais
tcp = ""

def configuracao():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destino = (HOST, PORT)

    # abrindo conexao TCP
    tcp.connect(destino)
# fim configuracao()


if __name__ == "__main__":
    # configurando a conexao
    configuracao()

    # inicializando a tela de votacao
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = votar_ui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # mostra a tela
    MainWindow.show()

    sys.exit(app.exec_())
    
    # fechando conexao TCP
    tcp.close()
    