# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:40:11 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    def yap():
        şifre = 12345
        kadi = "enesdoruk"
        
        if kadi ==g1.text() and şifre == g2.text():
            durumLabel.setText("Hoşgeldiniz")
            g1.clear()
            g2.clear()
        else:
            durumLabel.setText("kullanıcı adı veya şifre hatalı")
            g1.clear()
            g2.clear()
            
    
    app = QApplication(sys.argv)
    pencere = QWidget()
    form = QFormLayout()
    g1 = QLineEdit()
    g1.setFont(QFont("Arial",12))
    g2 = QLineEdit()
    
    button = QPushButton("giriş yap")
    durumLabel = QLabel("")
    durumLabel.setFont(QFont("Arial",12))
    
    g2.setEchoMode(QLineEdit.Password)
    
    form.addRow(QLabel("kullanıcı adı"),g1)
    form.addRow(QLabel("şifre"),g2)
    form.addRow(button)
    form.addRow(durumLabel)

    button.clicked.connect(yap)
    
    pencere.setLayout(form)
    
    pencere.setWindowTitle("Giriş")
    pencere.show()
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    pencere() 
    