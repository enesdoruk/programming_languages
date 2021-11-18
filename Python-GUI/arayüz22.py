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
            
            self.grup1 = QButtonGroup()
            self.grup2 = QButtonGroup()

            self.r1 = QRadioButton("yeşil")
            self.r2 = QRadioButton("mavi")
            self.r3 = QRadioButton("kırmızı")
            self.r4 = QRadioButton("siyah")

            self.grup1.addButton(self.r1)
            self.grup1.addButton(self.r2)

            self.grup2.addButton(self.r3)
            self.grup2.addButton(self.r4)

            
            h_box = QHBoxLayout()
            h_box.addWidget(self.r1)        
            h_box.addWidget(self.r2)
            h_box.addWidget(self.r3)
            h_box.addWidget(self.r4)
        

            #v_box = QVBoxLayout()
           
            

           

            
            self.setLayout()
            self.show()
            self.setWindowTitle("enes dayi")



          


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
