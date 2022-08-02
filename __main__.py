from PyQt5 import QtWidgets , QtGui , QtCore
from views_mangers.main_manger import MainManager
from views_mangers.playList_manger import PlayList_manger
from views_mangers.sigleView_manger import sigleVideo_manger

class encoder(QtWidgets.QStackedWidget):
    def __init__(self):
        super(encoder, self).__init__()
        self.resize(800, 650)
        self.setMaximumSize(QtCore.QSize(800, 650))
        self.main_manager = MainManager()
        self.playlist_manger = PlayList_manger()
        self.singleVideo = sigleVideo_manger()

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.main_manager) #0
        self.addWidget(self.playlist_manger) #2
        self.addWidget(self.singleVideo) #3

        # # install signals
        self.main_manager.dwnlod_playlist_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.main_manager.dwnlod_video_btn.clicked.connect(lambda : self.setCurrentIndex(2))
        self.playlist_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(0))
        self.singleVideo.bck_btn.clicked.connect(lambda : self.setCurrentIndex(0))

    def handle_encode(self):
        self.main_manager.encode()

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = encoder()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()










