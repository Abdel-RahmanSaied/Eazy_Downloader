import os
from PyQt5 import QtWidgets, QtCore, QtGui
from views import playList_view
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog, QApplication
from pytube import Playlist
from threading import Thread
import multiprocessing
import threading
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *


class Play_list_download(QThread):
    download_complete = pyqtSignal()
    update_values_signal = pyqtSignal()
    downloaded_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.play_list_url = ""
        self.download_path = ""
        self.video_name = ''
        self.video_description = ''
        self.video_status = ''
        self.progress_value = 0

        self.download_progress = True

        self.msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.msg.setWindowIcon(icon)

    def get_play_list(self, playList):

        try:
            p_url = Playlist(playList)
        except Exception as url_error:
            print(url_error)
        return p_url

    def run(self):

        try:
            play_list = Play_list_download().get_play_list(self.play_list_url)
            playlist_length = len(play_list.videos)
            counter = 1
            while self.download_progress == True:
                for video in play_list.videos:
                    if self.download_progress == True:
                        self.video_name = video.title
                        self.video_description = video.description
                        self.video_status = "In Progress .... "
                        self.update_values_signal.emit()


                        filters = video.streams.filter(progressive=True, file_extension='mp4')
                        filters.get_highest_resolution().download(output_path=self.download_path)
                        # video.streams.first().download()
                        self.video_status = " Downloded "
                        self.progress_value = int(counter / playlist_length) * 100
                        self.downloaded_signal.emit()
                        counter += 1
                    else:
                        break
                self.download_progress = False
                print("stopped")
                self.download_complete.emit()
        except Exception as d:
            print("Error while download the video with error : ", d)
            self.msg.setWindowTitle("Error")
            self.msg.setText("Error while download the video with error : " + str(d))
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setStyleSheet('''font: 12pt "Acumin Pro";''')


class PlayList_manger(QtWidgets.QWidget, playList_view.Ui_Form):
    # checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(PlayList_manger, self).__init__()
        self.setupUi(self)
        self.download_btn.clicked.connect(self.start_download)
        self.start_download = True
        self.stop_download = False
        self.editPath_btn.clicked.connect(self.select_path_to_save)
        self.Play_List = Play_list_download()
        self.Play_List.download_complete.connect(self.download_finished)
        self.Play_List.update_values_signal.connect(self.update_Labels)
        self.counter = 0
        self.Play_List.downloaded_signal.connect(self.update_status)

    def start_download(self):
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)
        if self.start_download:
            if len(self.link_lin.text()) > 8:
                if self.path_lbl.text() != "Select Path .........":
                    try:
                        self.Play_List.download_progress = True
                        self.Play_List.play_list_url = self.link_lin.text()
                        self.Play_List.download_path = self.path_lbl.text()
                        print(self.Play_List.play_list_url)
                        if len(self.Play_List.play_list_url) > 32:
                            self.Play_List.start()

                            self.download_btn.setText("Stop Download")
                            self.download_btn.setStyleSheet('''
                                                                font: 14pt "Acumin Pro";
                                                                background-color: rgb(255, 0, 0);
                                                                color: rgb(255, 255, 255);
                                                                background-color: rgb(255,  0, 0);
                                                                 border-radius: 7px;                                        
                                                                ''')
                            self.start_download = False
                            self.stop_download = True
                        else:
                            try:
                                msg.setWindowTitle("Warning")
                                msg.setText("              Invalid URL !              ")
                                msg.setIcon(QMessageBox.Critical)
                                msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
                                msg.exec_()
                            except Exception as msg_error:
                                print(msg_error)
                    except Exception as t:
                        print("xxxxxxxxxx", t)

                else:
                    msg.setWindowTitle("Warning")
                    msg.setText("please select download path !")
                    msg.setIcon(QMessageBox.Critical)
                    msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
                    msg.exec_()
            else:
                msg.setWindowTitle("Warning")
                msg.setText("please enter playlist link !")
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
                msg.exec_()

        elif self.stop_download:
            try:
                print(self.Play_List.download_progress)
                self.Play_List.download_progress = False
            except Exception as f:
                print(f)

            self.download_btn.setText("Start Download")
            self.download_btn.setStyleSheet('''
                                        font: 14pt "Acumin Pro";
                                        color: rgb(255, 255, 255);
                                        background-color: rgb(20,  190, 120);                                     
                                         border-radius: 7px;                              
                                                ''')
            self.start_download = True
            self.stop_download = False

    def download_finished(self):
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)

        self.download_btn.setText("Start Download")
        self.download_btn.setStyleSheet('''
                                    font: 14pt "Acumin Pro";
                                    color: rgb(255, 255, 255);
                                    background-color: rgb(20,  190, 120);                                     
                                     border-radius: 7px;                              
                                            ''')
        self.start_download = True
        self.stop_download = False

        msg.setWindowTitle("Successfully")
        msg.setText("Download Finished !")
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
        msg.exec_()

    def update_Labels(self):
        try:
            self.tableWidget.setRowCount(self.counter)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(self.counter, 0, QTableWidgetItem(str(self.Play_List.video_name)))
            self.tableWidget.setItem(self.counter, 1, QTableWidgetItem(str(self.Play_List.video_description)))
            self.tableWidget.setItem(self.counter, 2, QTableWidgetItem(str(self.Play_List.video_status)))
            self.counter += 1
        except Exception as T:
            print(T)

    def update_status(self):
        if self.counter != 0:
            self.tableWidget.setItem(self.counter - 1, 2, QTableWidgetItem(str(self.Play_List.video_status)))
        self.progressBar.setValue(self.Play_List.progress_value)

    def select_path_to_save(self):
        self.filepath_to_save = QFileDialog.getExistingDirectory(self, 'Hey! Select a path', "E:\\")
        if len(self.filepath_to_save) != 0:
            self.path_lbl.setText(self.filepath_to_save)
        else:
            self.path_lbl.setText("Select Path .........")


if __name__ == "__main__":
    import qdarkstyle

    app = QtWidgets.QApplication([])
    w = PlayList_manger()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
