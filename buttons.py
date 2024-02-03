from PyQt6 import QtWidgets, QtGui
from ui import Ui_MainWindow as ui
from ListItem import MusicList

class Execute():
        def button_random():
                random.shuffle()

        def button_on():
                spisok = [1]
                for x in spisok:
                        ui.listWidget.addItems(MusicList)
                        
        def button_off():
                spisok=[1]
                for x in spisok:
                        ui.listWidget.clear()

