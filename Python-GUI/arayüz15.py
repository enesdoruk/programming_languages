


from pyQt5.QtWidgets import *
from pyQt5.QtGui import *
from pyQt5.QtCore import *

import sys

class pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):
        self.giris = QLineEdit()
        button = QPushButton("yaziyi yazdir")
        
        v_box =QVBoxLayout()
        v_box.addWidget(self.giris)
        v_box.addWidget(button)
        
        self.setLayout(v_box)
                
        button.clicked.connect(self.yap)
        self.show()
        
        def yap(self):
            self.setWindowTitle(self.giri.text())
            
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())        
        