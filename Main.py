from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit
from PyQt5 import QtWidgets
import sys

#Classe de objettots da janela principal
class Ui_mainWindow(QMainWindow):
    #Construtor da classe
    def __init__(self,):    
        #   Chama o construtor da classe pai QMainWindow
        super(Ui_mainWindow, self).__init__()
        #Configurações da janela
        self.setWindowTitle ("Primeira Janela do Chatbot")
        self.setGeometry(100, 100, 600, 400)
        self.setupUi()

    # Método para configurar os elementos da interface    
    def setupUi(self): 
        # Cria um campo de texto
        self.text = QLabel(self)
        self.text.move(50, 50)   
        # Cria botões
        self.btn1 = QtWidgets.QPushButton(self)
        self.btn1.setText('Botão 1') 
        self.btn1.clicked.connect(self.on_click)
        
    def on_click(self):
        # Ação a ser executada quando o botão for clicado
        print('Botão clicado!')
        self.btn1.move(50, 100)
        self.text.setText(' Esse texto foi alteradoaaaaaaaaaaaaaaaa')   
        self.text.adjustSize()

def main():
    # Cria uma instância da aplicação 
    app = QApplication(sys.argv)
    Window = Ui_mainWindow()  
   
    #Mostra a janela
    Window.show()
    sys.exit(app.exec_())  


main()  # Chama a função main para iniciar o aplicativo