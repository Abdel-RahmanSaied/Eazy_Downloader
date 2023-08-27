from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox
from views_mangers.main_manger import MainManager
from views_mangers.playList_manger import PlayList_manger
from views_mangers.sigleView_manger import sigleVideo_manger
from views_mangers.search_manger import SearchManager


class Easy_Downloader(QtWidgets.QStackedWidget):
    def __init__(self):
        super(Easy_Downloader, self).__init__()
        self.resize(800, 650)
        # self.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Easy Downloader"))

        self.main_manager = MainManager()
        self.playlist_manger = PlayList_manger()
        self.singleVideo = sigleVideo_manger()
        self.search_manger = SearchManager()

        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # add widgets to the stack

        self.addWidget(self.main_manager)  # 0
        self.addWidget(self.playlist_manger)  # 1
        self.addWidget(self.singleVideo)  # 2
        self.addWidget(self.search_manger)  # 3

        # # install signals
        # main screen
        self.main_manager.dwnlod_playlist_btn.clicked.connect(lambda: self.setCurrentIndex(1))
        self.main_manager.dwnlod_video_btn.clicked.connect(lambda: self.setCurrentIndex(2))
        self.main_manager.search_song_btn.clicked.connect(lambda: self.setCurrentIndex(3))
        self.main_manager.pushButton.clicked.connect(self.about_me)
        # play list screen
        self.playlist_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(0))
        self.playlist_manger.pushButton.clicked.connect(self.about_me)
        # single video screen
        self.singleVideo.bck_btn.clicked.connect(lambda: self.setCurrentIndex(0))
        self.singleVideo.pushButton.clicked.connect(self.about_me)
        # search screen
        self.search_manger.bck_btn.clicked.connect(lambda: self.setCurrentIndex(0))
        self.search_manger.pushButton.clicked.connect(self.about_me)

    def about_me(self):
        try:
            msg = QtWidgets.QMessageBox()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            msg.setWindowIcon(icon)
            msg.setStyleSheet('''font: 12pt "Acumin Pro";''')

            msg.setWindowTitle(" About Us ")
            msg.setText(" Developed by : Abdel-Rahman Saied \n  Email : abdelrahmansaied080@gmail.com")
            msg.setIcon(QMessageBox.Information)
            msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
            msg.exec_()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = Easy_Downloader()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()
