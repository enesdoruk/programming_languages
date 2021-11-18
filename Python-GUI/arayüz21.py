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
            aciklama = QLabel("")
            baslik = qLabel("arayüz macerası")
            logo = QLabel()
            self.giris = QLineEdit()
            gonder = QPushButton()
            self.alinanEntryler = QTextEdit()

            baslik.setFont(QFOnt("Arial",15,QFont.Bold))
            baslik.setAlignment(Qt.AlignCenter)


            logo.setPixmap(QPixmap("..............png"))
            logo.setAlignment(Qt.AlignCenter)
            
            gonder = setIcon(QIcon("..............png"))

            h_box = QHBoxLayout()
            h_box.addwidget(aciklama)
            h_box.addWidget(self.giris)
            h_box.addWidget(self.gonder)

        

            v_box = QVBoxLayout()
            v_box.addWidget(baslik)
            v_box.addWidget(logo)
            v_box.addWidget(self.alinanEntryler)
            v_box.addWidget(h_box)
            

            gonder.clicked.connect(self.uygula)

            
            self.setLayout(v_box)
            self.show()
            self.setWindowTitle("enes dayi")



            def uygula(self):

                url = str(self.giris.text())
                response = request.get(url)
                content = response.content

                soup = BeautifulSoup(content,"html_parser")

                liste = list()

                for  i in soup.find_all("div",attrs = {"class": "content"}):
                    liste.append(i.text)

                toplamYazi =""
                
                for i in liste:

                    
                    toplamYazi += i+"\n"

                self.alinanEntryler.setText(toplamYazi)


if __name__ == "__main__":

    app = QAPplication(sys.argv)
    pencere = pencere()
    sys.exit(app.exec())
