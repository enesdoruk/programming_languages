from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtMultimedia import *

from bs4 import BeatufilSoup

import sys
import request

class pencere(Qwidget):
    def __init__(self):

        super().__init(self)
        self.setUI()

        def setUI(self):

          self.s1 = QSlider(Qt.HOrizontal)
          self.s1.setTickPosition(QSlider,TicksBelow)
          label1 = QLabel("deger:")
          self.label2 = QLabel()

          h_box = QHBoxLayout()
          h_box.addWidget(label1)
          h_box.addWidget(self.label2)
          
          self.s1.setminimum(0)
          self.s1.setMaximum(100)
          self.s1.setSingleStep(10)

          self.s1.valueChanged.connect(self.yaz)

          
           v_box =QVBoxLayout()
           v_box.addLayout(h_box)
           v_box.addWidget(self.s1)
          


           self.sp.valueChanged.connect(self.sesDegister)
           button.clicked.connect(self.sesDegistir)
           
                               
                                             
          
           # h_box = QHBoxLayout()
            
           # v_box = QVBoxLayout()
           
            

          

            
           self.setLayout(v_box)
           self.show()
           self.setWindowTitle("enes dayi")

        def sesDegistir(self):
            self.media.setVolume(self.sp.value())
     


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
