# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:06:58 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    
    app =QApplication(sys.argv)
    window = QWidget()
    v_box = QVBoxLayout()
    window.setGeometry(50,50,500,500)
    
    button1 = QPushButton(window)
    button1.setText("kabul")
    
    
    button2 = QPushButton(window)
    button2.setText("red")
    
    
    
    v_box.addWidget(button1)
    v_box.addStretch()
    v_box.addWidget(button2)
    
    window.setLayout(v_box)
    
    
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()