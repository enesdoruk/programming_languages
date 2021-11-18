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
           
           self.cb = QComboBox()
           self.cb.addItems(self.dogumTarihDondur())
           self.chbox = QCheckbox("kabul ediyorum")
           self.button = QPushButton("gonder")
           
            

            
            h_box = QHBoxLayout()
            h_box.addWidget(self.cb)
            h_box.addWidget(self.chbox)
            h_box.addWidget(self.button)
        

            self.button.clicked.connect(self.uygula)

            #v_box = QVBoxLayout()
           
            

          

            
            self.setLayout(form)
            self.show()
            self.setWindowTitle("enes dayi")

        
       def uygula(self):
           suankiyil = 2019
           kullaniciDogumTarihi = int(self.cb.currentText())
           yas = suankiyil - kullaniciDogumTarihi
           print( "yas:    ",yas)
          


       def dogumTarihiDondur(self):
           liste = [str(x) for x in range(1940,2000)]
           return liste


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
