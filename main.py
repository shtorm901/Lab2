from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
import sys
from ui import Ui_MainWindow
import random
from ListItem import MusicList as Music


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()


        def rand():
                random.shuffle(Music)


        def on():
                spisok = [1]
                for x in spisok:
                        ui.listWidget.addItems(Music)


        def off():
                ui.listWidget.clear()

        def play():
                filename = 'NEFFEX - Rare.mp3'
                effect = QSoundEffect()
                effect.setSource(QUrl.fromLocalFile(filename))
                effect.setVolume(100)
                effect.play()


        def stop():
                pass

ui.pushButton.clicked.connect(rand)
ui.pushButton_4.clicked.connect(on)
ui.pushButton_5.clicked.connect(off)
ui.pushButton_2.clicked.connect(play)

sys.exit(app.exec())