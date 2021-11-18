# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:23:37 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def pencere():
    app = QApplication(sys.argv)
    pencere=QWidget()
    pencere.setGeometry(50,50,300,300)
    h_box=QHBoxLayout()
    
    button1 = QPushButton(pencere)
    button1.setText("ML")
    
    button2 = QPushButton(pencere)
    button2.setText("AI")

    h_box.addWidget(button1)
    h_box.addWidget(button2)
    
    pencere.setLayout(h_box)

    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()    