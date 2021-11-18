from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
          
           # h_box = QHBoxLayout()
            
           # v_box = QVBoxLayout()
           
            

          

            
           self.setLayout(form)
           self.show()
           self.setWindowTitle("enes dayi")

        
     


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
