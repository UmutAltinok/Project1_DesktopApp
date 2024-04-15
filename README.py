from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget

class loginekrani(QMainWindow):
    def kontrol(self):
        print("Tıklandı")

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        icerik=QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı Adı:"))
        ka=QLineEdit()
        icerik.addWidget(ka)
        icerik.addWidget(QLabel("Şifre:"))
        sf=QLineEdit()
        icerik.addWidget(sf)
        buton1=QPushButton("Çevir")
        icerik.addWidget(buton1)
        icerik.addWidget(QLabel("Sonuç:"))
        araclar=QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

        buton1.clicked.connect(self.kontrol)

uygulama = QApplication([])
pencere = loginekrani()
pencere.show()
uygulama.exec()