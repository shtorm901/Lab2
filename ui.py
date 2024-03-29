# Form implementation generated from reading ui file 'C:\Users\crabt\OneDrive\Рабочий стол\Новая папка (2)\ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets
from ListItem import MusicAll as Music
import random
from pygame import mixer


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(219, 320, 421, 86))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 0, 0)\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(540, 20, 76, 24))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:rgb(0, 255, 0)\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(275, 0, 251, 321))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        def on():
            self.listWidget.addItems(Music)
            self.pushButton_4.clicked.disconnect()
            self.pushButton_4.clicked.connect(off)
            self.pushButton_4.setText("Off")
            self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 0, 0)\n"
"}")

        def off():
            self.listWidget.clear()
            self.pushButton_4.clicked.disconnect()
            self.pushButton_4.clicked.connect(on)
            pause()
            self.pushButton_4.setStyleSheet("QPushButton{\n"
"background-color:rgb(0, 255, 0)\n"
"}")
            self.pushButton_4.setText("On")


        def rand():
            random.shuffle(Music)
            self.listWidget.clear()
            self.listWidget.addItems(Music)

        def play(item):
            mixer.init()
            item.text() == Music
            mixer.music.load(item.text())
            mixer.music.play()


        def pause():
            mixer.init()
            mixer.music.pause()
            self.pushButton_6.clicked.disconnect()
            self.pushButton_6.setText("UnPause")
            self.pushButton_6.clicked.connect(unpause)
            self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color:rgb(0, 255, 0)\n"
"}")

        def unpause():
            mixer.init()
            mixer.music.unpause()
            self.pushButton_6.clicked.disconnect()
            self.pushButton_6.setText("Pause")
            self.pushButton_6.clicked.connect(pause)
            self.pushButton_6.setStyleSheet("QPushButton{\n"
"background-color:rgb(255, 0, 0)\n"
"}")

        self.pushButton.clicked.connect(rand)
        self.pushButton_4.clicked.connect(on)
        self.pushButton_6.clicked.connect(pause)
        self.listWidget.itemClicked.connect(play)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Rand"))
        self.pushButton_6.setText(_translate("MainWindow", "Pause"))
        self.pushButton_4.setText(_translate("MainWindow", "On"))

