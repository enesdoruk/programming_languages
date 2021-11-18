# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:05:31 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import time

bekle = time.sleep

print("Loading", end='')
for i in range(20):
    print(".", sep='', end='')
    bekle(0.3)


def pencere():
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setGeometry(50,50,500,500)
    h_box=QHBoxLayout()
    v_box=QVBoxLayout()
    
    button1 = QPushButton("button1")
    button2 = QPushButton("button2")
    v_box.addWidget(button1)
    v_box.addStretch()
    v_box.addWidget(button2)
   
    
    button3 = QPushButton("button3")
    button4 = QPushButton("button4")
    h_box.addWidget(button3)
    h_box.addStretch()
    h_box.addWidget(button4)
    
    v_box.addLayout(h_box)
    
  
    window.setLayout(v_box)
    
    window.show()
    sys.exit(app.exec())
    
    
    
if __name__ == "__main__":
    pencere()
    