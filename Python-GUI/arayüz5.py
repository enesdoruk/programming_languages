# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:59:22 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    
    app = QApplication(sys.argv)
    window = QWidget()
    h_box = QHBoxLayout()
    
    button1 = QPushButton("kabul")
    button2 = QPushButton("red")
    
    h_box.addWidget(button1)
    h_box.addWidget(button2)
    
    
    window.setLayout(h_box)
    
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    pencere()