from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

#import stegano
from stegano import lsb
from aes_code import PrpCrypt

from os import path
import sys, time, os

import selectionWindow

FROM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),'Encrypt_Window.ui'))

class Encrypt_Screen(QMainWindow, FROM_CLASS):

    def __init__(self, parent=None):
        super(Encrypt_Screen, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_handler()
        self.btn_handlers()


    def UI_handler(self):
        self.setFixedSize(929,628)


    def btn_handlers(self):
        
        #Select Image
        self.select_IMG_btn.clicked.connect(self.select_image_handler)

        #Back Button
        self.back_button.clicked.connect(self.back_btn_operation)

        #Browse
        self.browse_btn.clicked.connect(self.browse_op_file)

        #Start
        self.start_btn.clicked.connect(self.start_operation)


    # Button Functions
    def select_image_handler(self):
        try :
            url_dir = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image Files (*.png)')
            self.image_info_display(url_dir)
        
        except :
            pass


    def back_btn_operation(self):
        self.close()
        self.open = selectionWindow.SelectionWindow()
        self.open.show()


    def browse_op_file(self):
        output_file_path = QFileDialog.getSaveFileName(self, 'Save Image As', '', 'Image Files (*.png)')
        
        #Display Output Path
        self.output_textBox.setText(output_file_path[0])
        

    def start_operation(self):
        key_box = self.textbox_key.toPlainText()
        message = self.textbox_message.toPlainText()
        image = self.path_textBox.text()
        path_save = self.output_textBox.text()

        #Start Encryption
        if (key_box != '') and (message != '') and (path_save != '') and (image != ''):
            try:
                cipher_text_byte = PrpCrypt(key_box).encrypt(message)  #Encrypted Message
                cipher_text_str = cipher_text_byte.decode()     #Covert Byte to String
                    
                cipher_image = lsb.hide(image, cipher_text_str)
                cipher_image.save(path_save)
                    
                time.sleep(1)
                QMessageBox.about(self, 'Completed', 'Done!')

                #Clear All The Input Boxes.
                self.clear_all()

            except:
                QMessageBox.about(self, 'Error',  'Operation Failed, try again.')
        
        else:
            QMessageBox.about(self, 'Error', 'Please enter all the fields to continue..')


    #Information & Progress
    def image_info_display(self, url_dir):

        try :
            #Display File Path
            file_path = url_dir[0]
            self.path_textBox.setText(file_path)

            #Display File Name
            base_name = path.basename(file_path)
            file_name = path.splitext(base_name)        #seperates filename and extension
            self.name_textBox.setText(file_name[0])

            #Display File Extension
            self.extension_textBox.setText(file_name[1])

            #Display File Size
            file_size = path.getsize(file_path)

            if file_size < 1000:
                self.size_textBox.setText( str(file_size) + ' Bytes')
        
            else :
                file_size = file_size // 1000
                self.size_textBox.setText( str(file_size) + ' KB')
        
        except :
            pass

    def clear_all(self):
        self.textbox_key.setPlainText('')
        self.textbox_message.setPlainText('')
        self.name_textBox.setText('')
        self.size_textBox.setText('')
        self.extension_textBox.setText('')
        self.path_textBox.setText('')
        self.output_textBox.setText('')


def main():
    app = QApplication(sys.argv)
    window = Encrypt_Screen()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
