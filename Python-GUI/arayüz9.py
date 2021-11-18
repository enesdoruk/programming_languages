# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:19:21 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    
    app = QApplication(sys.argv)
    pencere = QWidget()
    form = QFormLayout()
    
    form.addRow(QLabel("adınız:"),QLineEdit())
    sifre = QLineEdit()
    sifre.setEchoMode(QLineEdit.Password)
    form.addRow(QLabel("şifre:"),sifre)
    form.addRow(QLabel("adres:"),QTextEdit())
    
    
    
    
    
    lb1 = QLabel("cinsiyetiniz")
    rd1 = QRadioButton("erkek")
    rd2 = QRadioButton("kadın")
    
    h_box = QHBoxLayout()
    h_box.addWidget(rd1)
    h_box.addWidget(rd2)
    
    form.addRow(lb1,h_box)
    
    h_box2 = QHBoxLayout()
    btn1 = QPushButton("gönder")
    btn2 = QPushButton("iptal et")
    h_box2.addWidget(btn1)
    h_box2.addWidget(btn2)
    
    form.addRow(h_box2)
    
    pencere.setLayout(form)
    pencere.setWindowTitle("bilgi merkezi")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()
    
    