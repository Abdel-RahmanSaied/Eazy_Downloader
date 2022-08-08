import os
from PyQt5 import QtWidgets , QtCore , QtGui
from views import sigleVideo_view
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog , QApplication
from pytube import YouTube
from threading import Thread
import multiprocessing
import threading
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *


class Play_list_download(QThread):
    download_complete = pyqtSignal()
    update_values_signal = pyqtSignal()
    downloaded_signal = pyqtSignal()
    def __init__(self ,*args, **kwargs):
        super().__init__()

        self.play_list_url = ""
        self.download_path = ""
        self.video_name = ''
        self.video_description = ''
        self.video_status = ''
        self.video_type = ''
        self.progress_value = 0

        self.download_progress = True

    def msg_exec(self , title , text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(str(title))
        msg.setText(str(text))
        msg.setIcon(QMessageBox.Critical)
        msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
        msg.exec_()

    def run(self):
        msg2 = QtWidgets.QMessageBox()
        try :
            video_url = self.play_list_url
            try :
                video_url = YouTube(self.play_list_url)
            except Exception as link_error :
                print(link_error)
                # try :
                #     Play_list_download().msg_exec("Warning" ," invalid URL ! " )
                # except Exception as g :
                #     print(g)

            if self.video_type == "MP3":
                video = video_url.streams.filter(only_audio=True).first()
            else:
                video = video_url.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                #video.get_highest_resolution()
            self.video_name = video_url.title
            self.video_description = video_url.description
            self.video_status = "In Progress .... "
            self.update_values_signal.emit()

            out_file = video.download(output_path=self.download_path)
            if self.video_type == "MP3":
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                counter = 2
                while True  :
                    if os.path.exists(new_file) == True:
                        new_file = base+"-"+str(counter) + '.mp3'
                        counter+=1
                    else:
                        break
                os.rename(out_file, new_file )
            if self.video_type == "MP4":
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp4'
                counter = 2
                while True:
                    if os.path.exists(new_file) == True:
                        new_file = base + "-" + str(counter) + '.mp4'
                        counter += 1
                    else:
                        break
                os.rename(out_file, new_file)

            self.video_status = " Downloded "
            self.progress_value = 100
            self.downloaded_signal.emit()

            self.download_progress = False
            self.download_complete.emit()
        except Exception as d :
            print("xxxxxxxxffffffffx",d)
            # try :
            #     Play_list_download().msg_exec("Warning" ," Invalid URL ! " )
            # except Exception as g :
            #     print(g)
            # try :
            #     msg2.setWindowTitle("Warning")
            #     msg2.setText("Invalid URLss !")
            #     msg2.exec_()
            # except Exception as msg_error  :
            #     print(msg_error)

class sigleVideo_manger(QtWidgets.QWidget, sigleVideo_view.Ui_Form):
    # checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(sigleVideo_manger, self).__init__()
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
        # self.pushButton.clicked.connect(self.about_me)

    def start_download(self):
        msg = QtWidgets.QMessageBox()
        if self.start_download  == True :
            if len(self.link_lin.text()) >8 :
                if self.path_lbl.text() != "Select Path ........." :
                    try :
                        self.progressBar.setValue(0)
                        self.Play_List.video_type =  self.type_compobox.currentText()
                        self.Play_List.download_progress = True
                        self.Play_List.play_list_url = self.link_lin.text()
                        self.Play_List.download_path = self.path_lbl.text()
                        if len(self.Play_List.play_list_url)> 32 :
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
                        else :
                            try :
                                msg.setWindowTitle("Warning")
                                msg.setText("              Invalid URL !              ")
                                msg.setIcon(QMessageBox.Critical)
                                msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
                                msg.exec_()
                            except Exception as msg_error  :
                                print(msg_error)
                    except Exception as t :
                        print("xxxxxxxxxx",t)

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

        elif  self.stop_download == True :
            try  :
                print(self.Play_List.download_progress )
                self.Play_List.download_progress = False
            except Exception as f :
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

        msg.setWindowTitle("Successfully ")
        msg.setText("Download Finished !")
        msg.setIcon(QMessageBox.Information)
        msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
        msg.exec_()

    def update_Labels(self):
        try :
            self.tableWidget.setRowCount(0)
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(0, 0, QTableWidgetItem(str(self.Play_List.video_name)))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(str(self.Play_List.video_description)))
            self.tableWidget.setItem(0, 2, QTableWidgetItem(str(self.Play_List.video_status)))

        except Exception as T :
            print(T)
    def update_status(self):
        self.tableWidget.setItem(0 , 2, QTableWidgetItem(str(self.Play_List.video_status)))
        self.progressBar.setValue(self.Play_List.progress_value)


    def select_path_to_save(self):
        self.filepath_to_save = QFileDialog.getExistingDirectory(self, 'Hey! Select a path', "E:\\")
        if len(self.filepath_to_save) != 0 :
            self.path_lbl.setText(self.filepath_to_save)
        else:
            self.path_lbl.setText("Select Path .........")


if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = sigleVideo_manger()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)