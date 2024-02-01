from PyQt6 import QtWidgets, QtGui
import sys
from ui import Ui_MainWindow
from ListItem import MusicList as Music
import random

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
                       
    def button_random():
        random.shuffle(Music)

    def button_on():
        spisok = [1]
        for x in spisok:
            ui.listWidget.addItems(Music)

    def button_off(spisok):
        spisok = [1]
        for x in spisok:
            ui.listWidget.clear()
         
    ui.pushButton_4.clicked.connect(button_on)
    ui.pushButton_5.clicked.connect(button_off)
    ui.pushButton.clicked.connect(button_random)
                                                    
    sys.exit(app.exec())
