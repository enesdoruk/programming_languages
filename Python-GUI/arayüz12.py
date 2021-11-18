# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 23:28:56 2019

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
    
    baslik = QLabel("<u> Devrenin sonu</u>")
    baslik.setFont(QFont("Halvetica",14,QFont.Bold))
    baslik.setAlignment(Qt.AlignCenter)

    
    gonderim = QLabel("<a href=\"http://www.khanacademy.org.tr/altkategori.asp?cat=245\">dökümanları incele !</a>")
    resim = QLabel()
    resim.setPixmap(QPixmap("enes.PNG"))
    youtube = QLabel("<a href=\"https://www.youtube.com/watch?v=ONIWp_yNJ8g&list=PLK6Whnd55IH5rbIrl61H2l-560LddyHO5&index=8\">devre videoları izle !</a>")
    youtube.setAlignment(Qt.AlignRight)
    
    
    v_box = QVBoxLayout()
    v_box.addWidget(baslik)
    v_box.addWidget(gonderim)
    v_box.addWidget(resim)
    v_box.addWidget(youtube)
    
    youtube.setOpenExternalLinks(True)
    gonderim.setOpenExternalLinks(True)
    
    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)
    pencere.setWindowTitle("Devre yanıyor")
    pencere.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    pencere()
    