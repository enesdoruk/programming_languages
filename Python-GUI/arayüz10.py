# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 22:59:41 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    
    app = QApplication(sys.argv)
    pencere = QWidget()
    
    label = QLabel("merhaba shake me, after the party ")
    label.setAlignment(Qt.AlignCenter)
    label.setFont(QFont("Arial",15,QFont.Bold))
    
    
    v_box = QVBoxLayout()
    v_box.addWidget(label)
    
    
    
    
    
    
    pencere.setLayout(v_box)
    pencere.setWindowTitle("QLABEL")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()    