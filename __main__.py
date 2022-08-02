from PyQt5 import QtWidgets , QtGui , QtCore
from views_mangers.main_manger import MainManager
from views_mangers.playList_manger import PlayList_manger
from views_mangers.sigleView_manger import sigleVideo_manger
from views_mangers.search_manger import SearchManager

class encoder(QtWidgets.QStackedWidget):
    def __init__(self):
        super(encoder, self).__init__()
        self.resize(800, 650)
        self.setMaximumSize(QtCore.QSize(800, 650))
        self.main_manager = MainManager()
        self.playlist_manger = PlayList_manger()
        self.singleVideo = sigleVideo_manger()
        self.search_manger = SearchManager()

        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.main_manager) #0
        self.addWidget(self.playlist_manger) #1
        self.addWidget(self.singleVideo) #2
        self.addWidget(self.search_manger) #3

        # # install signals
        # main screen
        self.main_manager.dwnlod_playlist_btn.clicked.connect(lambda : self.setCurrentIndex(1))
        self.main_manager.dwnlod_video_btn.clicked.connect(lambda : self.setCurrentIndex(2))
        self.main_manager.search_song_btn.clicked.connect(lambda : self.setCurrentIndex(3))
        self.main_manager.pushButton.clicked.connect(self.playlist_manger.about_me)
        # play list screen
        self.playlist_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(0))
        # single video screen
        self.singleVideo.bck_btn.clicked.connect(lambda : self.setCurrentIndex(0))
        # search screen
        self.search_manger.bck_btn.clicked.connect(lambda : self.setCurrentIndex(0))
        self.search_manger.pushButton.clicked.connect(self.playlist_manger.about_me)
    def handle_encode(self):
        self.main_manager.encode()

if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = encoder()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()










