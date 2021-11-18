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

           self.setGeometry(100,100,700,700)

           self.setAutoFillBackground(True)
           
           self.p = self.palette()

           self.p.setColor(self.backgroundRole(),Qt.blue) 

           self.setPalette(self.p)

           self.media = QMediaPlayer()

           self.media.setMedia(QMediaContent(QUrl.formLocalFile("...............mp3")))

           self.sp = QSpinBox()
           self.sp.setRange(1,100)
           

           button = QPushButton("şarkıyı çal")
           v_box =QVBoxLayout()
           v_box.addWidget(button)
           v_box.addWidget(self.sp)


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
