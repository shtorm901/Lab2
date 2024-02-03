from PyQt6 import QtWidgets, QtGui
import sys
from ui import Ui_MainWindow
import random
from buttons import Execute

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
                            
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()

        ui.pushButton.clicked.connect(Execute.button_random)
        ui.pushButton_4.clicked.connect(Execute.button_on)
        ui.pushButton_5.clicked.connect(Execute.button_off)

        sys.exit(app.exec())
