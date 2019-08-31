import mainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtWidgets import QFileDialog
from img import showImg
import os


def openFileclicked(self):
    try:
        with open("tools.ini", 'r') as f:
            rootPath = f.read()
    except:
        rootPath = "c:/"

    fileName = QFileDialog.getOpenFileName(None, " ", rootPath,
                                           "bmp Files (*.bmp);;jpg Files (*.jpg);;jpeg Files (*.jpeg);;png Files (*.png)")
    if fileName[0]:
        showImg(fileName[0])

        try:
            os.remove("tools.ini")
        except:
            pass

        with open("tools.ini", 'w') as f:
            f.write(os.path.dirname(fileName[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(window)
    ui.openFile.clicked.connect(openFileclicked)
    window.show()
    app.exit(app.exec_())
