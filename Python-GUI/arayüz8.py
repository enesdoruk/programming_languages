# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 21:08:05 2019

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
    
    form.addRow(QLabel("adınız: "),QLineEdit())
    
    lb1 = QLabel("cinsiyetiniz:")
    rd1 = QRadioButton("erkek")
    rd2 = QRadioButton("kadın")
    
    
    h_box = QHBoxLayout()
    h_box.addWidget(rd1)
    h_box.addStretch()
    h_box.addWidget(rd2)
    
    form.addRow(lb1,h_box)
    form.addRow(QPushButton("gönder"))
    
    
    
    
    pencere.setLayout(form)
    pencere.setWindowTitle("python")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()    
    