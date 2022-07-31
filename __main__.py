from PyQt5 import QtWidgets , QtGui , QtCore
from views_mangers.main_manger import MainManager

class encoder(QtWidgets.QStackedWidget):
    def __init__(self):
        super(encoder, self).__init__()
        self.resize(800, 650)
        self.setMaximumSize(QtCore.QSize(800, 650))
        self.main_manager = MainManager()

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.main_manager)

        # # install signals
        # self.start_manger.start_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        # self.start_manger.exit_btn.clicked.connect(self.handle_close)

    def handle_encode(self):
        self.main_manager.encode()

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = encoder()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()










