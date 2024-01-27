from PyQt6 import QtWidgets, QtGui
import sys
from ui import Ui_MainWindow
import random

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def button_on_off():
            p = 'Егор Крид - Будильник'
            q = 'Rain Paris - Pain'
            r = 'NEFFEX - Never Back Down'
            d = 'NEFFEX - Rare'
            f = 'Jann - Gladiator'
            k = 'NEFFEX - Make Moves'
            o = 'Skillet - Hero'
            spisok = [1]
            for x in spisok:
                ui.listWidget.addItem(format(p))
                ui.listWidget.addItem(format(q))
                ui.listWidget.addItem(format(r))
                ui.listWidget.addItem(format(d))
                ui.listWidget.addItem(format(f))
                ui.listWidget.addItem(format(o))
            flag = 1

    def button_random(spisok):
        length = len(spisok)
        for i in range(0, length):
            rnd = random.randint(0, length - 1)
            temp = spisok[i]
            spisok[i] = spisok[rnd]
            spisok[rnd] = temp
        
    ui.pushButton.clicked.connect(button_random)
    ui.pushButton_4.clicked.connect(button_on_off)
                                                    
    sys.exit(app.exec())
