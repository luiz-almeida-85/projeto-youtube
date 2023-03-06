# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mhyt import yt_download

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(180, 270, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_download.setFont(font)
        self.bt_download.setCheckable(False)
        self.bt_download.setObjectName("bt_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 190, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 230, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(130, 191, 291, 21))
        self.txt_link.setText("")
        self.txt_link.setObjectName("txt_link")
        self.txt_titulo = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_titulo.setGeometry(QtCore.QRect(130, 231, 291, 21))
        self.txt_titulo.setText("")
        self.txt_titulo.setObjectName("txt_titulo")
        self.rb_mp3 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp3.setGeometry(QtCore.QRect(110, 301, 43, 16))
        self.rb_mp3.setChecked(True)
        self.rb_mp3.setObjectName("rb_mp3")
        self.rb_mp4 = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_mp4.setGeometry(QtCore.QRect(110, 320, 43, 16))
        self.rb_mp4.setChecked(False)
        self.rb_mp4.setObjectName("rb_mp4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 60, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, -10, 271, 201))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ### Botão Download ###

        self.bt_download.clicked.connect(self.download)

    def download(self):

        if self.rb_mp4.isChecked() == True:
            url = self.txt_link.text()
            titulo = self.txt_titulo.text()
            titulo_mp4 = titulo + '.mp4'
            yt_download(url,titulo_mp4)
        elif self.rb_mp3.isChecked() == True:


            try:
                url = self.txt_link.text()
                titulo = self.txt_titulo.text()
                titulo_mp3 = titulo + '.mp3'
                yt_download(url,titulo_mp3, ismusic = True, codec = 'mp3')
            except:
                pass



    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "LINK:"))
        self.label_2.setText(_translate("MainWindow", "Titulo:"))
        self.rb_mp3.setText(_translate("MainWindow", "MP3"))
        self.rb_mp4.setText(_translate("MainWindow", "MP4"))
        self.label_4.setText(_translate("MainWindow", "Download"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/png-clipart-youtube-logo-graphics-youtube-text-logo-removebg-preview.png\"/></p></body></html>"))

### Imagem ###
import youtube

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

