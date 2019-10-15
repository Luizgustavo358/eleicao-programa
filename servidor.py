'''-----------------------------------------|
|             Trabalho de LRSO              |
|-------------------------------------------|
| Dupla: Luiz Gustavo Bragança dos Santos   |
|        Pedro Augusto Prosdocimi           |
|-------------------------------------------'''

# imports
import sys
import _thread
import queue
import socket
import threading
import servidor_porta
from PyQt5 import QtCore, QtGui, QtWidgets

# endereco IP do servidor
HOST = '127.0.0.1'

# Porta do servidor
PORT = 8000

# variaveis globais
candidatos = []
votos = []
thread_lock = threading.Lock()


def mostra_dialog():
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = servidor_porta.Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    # pegando a porta
    PORT = ui.get_port()

    sys.exit(app.exec_())
# fim mostra_dialog()


def add_candidatos():
    candidatos.append()
# fim add_candidatos()


if __name__ == "__main__":
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("porta:", PORT)
    mostra_dialog()    
    print("porta:", PORT)
