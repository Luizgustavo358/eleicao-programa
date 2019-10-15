# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servidor-porta.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(295, 213)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 30, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 41, 17))
        self.label_2.setObjectName("label_2")
        self.porta = QtWidgets.QLineEdit(Dialog)
        self.porta.setGeometry(QtCore.QRect(100, 90, 113, 25))
        self.porta.setObjectName("porta")
        self.iniciar_btn = QtWidgets.QPushButton(Dialog)
        self.iniciar_btn.setGeometry(QtCore.QRect(100, 150, 80, 25))
        self.iniciar_btn.setObjectName("iniciar_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Servidor"))
        self.label_2.setText(_translate("Dialog", "Porta"))
        self.iniciar_btn.setText(_translate("Dialog", "iniciar"))
    #

    def get_port(self):
        return self.porta.text()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
