from PyQt5 import QtWidgets , QtCore , QtGui
from views import main_view
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog , QApplication
from pytube import Playlist
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *

class MainManager(QtWidgets.QWidget, main_view.Ui_Form):
    # checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(MainManager, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = MainManager()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()