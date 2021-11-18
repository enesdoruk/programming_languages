# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:22:14 2019

@author: user
"""


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


def pencere():
    
    app = QApplication(sys.argv)
    pencere = QWidget()
    pencere.setGeometry(40,40,500,500)
    izgara = QGridLayout()
    
    for i in range(0,3):
        for j in range(0,3):
            izgara.addWidget(QPushButton("str:{},stn:{}".format(i,j)),i,j)
    
    

    
    
    pencere.setLayout(izgara)
    
    
    
    
    pencere.setWindowTitle("arayüz_geliştirme")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()    
    
    
    