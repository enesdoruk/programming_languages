# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:32:50 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    def yap():
        print(giris.text())
    app = QApplication(sys.argv)
    pencere = QWidget()
    giris = QLineEdit()
    giris2 = QTextEdit()
    
    giris.textChanged.connect(yap)
    giris.setText("abdullah enes doruk")
    
    v_box = QVBoxLayout()
    v_box.addWidget(giris)
    v_box.addWidget(giris2)
    
    pencere.setLayout(v_box)
    
    
    pencere.setWindowTitle("arayüz13")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()    