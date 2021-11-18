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
            
            self.giris1 = QLineEDit()
            self.giris2 = QLineEDit()
            gonder = QPushButton("hesapla")
            self.yazi1 = QLabel("sayi1")
            self.yazi2 =QLabel("sayi2")
            self.sonuc = QLabel("")
            self.sonuc.setAlignment()

            self.r1 = QRadioButton("topla")
            self.r2 = QRadioButton("çıkar")
            self.r3 = QRadioButton("çarp")
            self.r4 = QRadioButton("böl")

            form.addRow(self.yazi1,self.giris1)
            form.addRow(self.yazi2,self.giris2)
            

            
            h_box3 = QHBoxLayout()
            h_box3.addWidget(self.r1)        
            h_box3.addWidget(self.r2)
            h_box3.addWidget(self.r3)
            h_box3.addWidget(self.r4)
            form.addRow(h_box3)
            form.addRow(self.sonuc)
            form.addRow(gonder)
        

            #v_box = QVBoxLayout()
           
            

            gonder.clicked.connect(self.hesapla)

            
            self.setLayout(form)
            self.show()
            self.setWindowTitle("enes dayi")

        toplam = 0
        bolme = 1
        carpma = 1
        cikarma = 0
        def hesapla(self):

            if self.r1.ischecked:
                sayi1 = int(self.giris1.text())
                sayi2 = int(self.girsi2.text())
                toplam = sayi1+sayi2
                self.sonuc.setText(str(toplam))

            if self.r2.ischecked:
                sayi1 = int(self.giris1.text())
                sayi2 = int(self.girsi2.text())
                cikarma = sayi1-sayi2
                self.sonuc.setText(str(cikarma))

            if self.r3.ischecked:
                sayi1 = int(self.giris1.text())
                sayi2 = int(self.girsi2.text())
                carpma = sayi1*sayi2
                self.sonuc.setText(str(carpma))

            if self.r4.ischecked:
                sayi1 = int(self.giris1.text())
                sayi2 = int(self.girsi2.text())
                bolme = sayi1//sayi2
                self.sonuc.setText(str(bolme))

                    
          


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
