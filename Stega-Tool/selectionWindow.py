from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from os import path
import sys, time, os

import encrypt_program
import decrypt_program

FROM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'SelectionWindow.ui'))

class SelectionWindow(QMainWindow, FROM_CLASS):

    def __init__(self, parent=None):
        super(SelectionWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_handlers()


    #Butten Handlers
    def btn_handlers(self):

        #Encrypt
        self.encrypt_btn.clicked.connect(self.Encrypt_Window_Open)

        #Decrypt
        self.decrypt_btn.clicked.connect(self.Decrypt_Window_Open)

        #Info 
        self.info_btn.clicked.connect(self.Info_Txt_Open)
        
    
    #Open Encryption Window
    def Encrypt_Window_Open(self):
        self.close()
        self.open = encrypt_program.Encrypt_Screen()
        self.open.show()

    #Open Encryption Window
    def Decrypt_Window_Open(self):
        self.close()
        self.open = decrypt_program.Decrypt_Screen()
        self.open.show()

    
    #Open Info.txt
    def Info_Txt_Open(self):
        try:
            os.startfile('Info.txt')
        except:
            QMessageBox.about(self, 'Error',  'Error in opening file / File not found ')


def main():
    app = QApplication(sys.argv)
    window = SelectionWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()