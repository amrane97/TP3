

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)

        self.label1 = QLabel("Enter your host IP:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
       
        self.button = QPushButton("Send", self)
        self.button.move(10, 190)
        #ici_debut*****************************************************************
        self.label3 = QLabel("Enter your keyAPI:", self)
        self.label3.move(10, 60)
        self.text3 = QLineEdit(self)
        self.text3 = self.text3.move(10, 90)
        

        self.label4 = QLabel("hostname:", self)
        self.label4.move(10, 120)
        self.text4 = QLineEdit(self)
        self.text4 = self.text4.move(10, 150)
       
        #ici_fin**********************************************************************

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        #ici_debut***********************************************************************
        api_key = self.text3.text()
        ip = self.text4.text()
        #ici_fin**************************************************************************

        if hostname == "" or api_key == "" or ip == "": # j'ai modifié a partir de "" de hostname
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname, ip, api_key) # j'ai donné les parametre que j'ai rajouté dans la fonction
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()

    def __query(self, hostname, ip, api_key):# j'ai rajouté mes 2 autres String
        url = "http://%s/ip/%s?key=%s" % (hostname) % (ip) % (api_key)  
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()