from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

from os import path
import sys
import selectionWindow

from threading import Thread
import time

FROM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'LoadingScreen.ui'))
LIMIT_TIME = 100

class Ex(QThread):
    countChanged = pyqtSignal(int)

    def run(self):
        count = 0

        while count <= LIMIT_TIME:
            count = count + 1
            time.sleep(0.04)
            self.countChanged.emit(count)


class LoadingScreen(QMainWindow, FROM_CLASS):

    def __init__(self, parent=None):
        super(LoadingScreen,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.onStart()


    def onStart(self):
        self.calc = Ex()
        self.calc.countChanged.connect(self.countChangedProcess)
        self.calc.start()


    def countChangedProcess(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            #time.sleep(1)
            self.close_currentApp()


    def close_currentApp(self):
        self.close()
        self.open = selectionWindow.SelectionWindow()
        self.open.show()
        

def main():
    app = QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()