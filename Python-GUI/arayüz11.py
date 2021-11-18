# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:16:41 2019

@author: user
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

def pencere():
    
    app = QApplication(sys.argv)
    pencere = QWidget()
    label = QLabel()
    label.setText("<a href=\"www.google.com\">Google'a git</a>")
    label.setOpenExternalLinks(True)
    
    label2 = QLabel()
    label2.setPixmap(QPixmap("enes.PNG"))
    
    
    v_box = QVBoxLayout()
    v_box.addWidget(label2)
    
    
    
    
    
    
    pencere.setLayout(v_box)
    pencere.setWindowTitle("QLABEL")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()    