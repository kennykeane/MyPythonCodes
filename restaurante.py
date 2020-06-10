import sys
import os
from PyQt5.QtWidgets import *
import pymysql.cursors


class Window():

    def __init__(self):
        root = QApplication(sys.argv)
        self.window = QWidget()
        self.window.setWindowTitle('Login ')
        self.window.setGeometry(10, 10, 300, 200)
        label1 = QLabel('Usuario', self.window)
        label1.move(5, 50)
        label1 = QLabel('Senha', self.window)
        label1.move(5, 100)
        button = QPushButton('login', self.window)
        button.move(110, 130)
        usuario = QLineEdit(self.window)
        usuario.move(57, 50)
        usuario.resize(220, 20)
        senha = QLineEdit(self.window)
        senha.move(57, 100)
        senha.resize(220, 20)

        def Vericarlogin(self):
            autenticado = False
            usuarioMaster = False

            try:
                conection = pymysql.connect(
                    host='localhost',
                    user='root',
                    password='',
                    db='Restaurante',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor
                )
            except:
                aviso = QMessageBox
                aviso.setText('Erro ao conectar a Base de Dados')
                aviso.show()
                aviso.exec()

            try:
                with  conection.cursor() as cursor:
                    cursor.execute('select * from Cadastros')
                    resultados = cursor.fetchall()
            except:

                self.aviso = QMessageBox()
                self.aviso.setText('Erro ao pesquisar na base de dados')
                self.aviso.show()
                self.aviso.exec_()

            y = usuario.text()
            x = senha.text()

            for lina in resultados:
                if lina['nome'] == y and lina['senha'] == x:
                    if lina['nivel'] == 'B':
                        usuarioMaster = False
                        autenticado = False
                    if lina['nivel'] == 'A':
                        usuarioMaster = True
                    autenticado = True
                    break
                else:
                    autenticado = False

            if not autenticado:
                aviso = QMessageBox()
                aviso.setText(' senha ou nome de usuario errado ')
                aviso.show()
                aviso.exec_()

            if autenticado:

                if usuarioMaster:
                    AdminWindow()

        button.clicked.connect(Vericarlogin)
        self.window.show()
        root.exec_()

    class AdminWindow():

        window2 = QWidget()
        window2.setWindowTitle('Adminstration ')
        window2.setGeometry(10, 10, 600, 600)

        window2.show()


Window()

