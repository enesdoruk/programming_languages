from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from bs4 import BeatufilSoup

import sys
import request

class pencere(Qwidget):
    def __init__(self):

        super().__init(self)
        self.setUI()

        def setUI(self):
            self.cb = QCheckBox("anlaşmayı okudum")
            button =QPushButton("gonder")
            
           
            

            
            h_box = QHBoxLayout()
            h_box.addWidget(self.cb)
            h_box.addWidget(button)
        

            #v_box = QVBoxLayout()
           
            button.clicked.connect(self.yap)

          

            
            self.setLayout(form)
            self.show()
            self.setWindowTitle("enes dayi")

        def yap(self):
            if self.cb.isChecked():
                print("kabul ettin")
            else:
                print("kabul etmedin")
       
                    
          


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
