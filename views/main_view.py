# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/main_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(799, 650)
        Form.setMaximumSize(QtCore.QSize(800, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 322, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dwnlod_playlist_btn = QtWidgets.QPushButton(Form)
        self.dwnlod_playlist_btn.setMinimumSize(QtCore.QSize(161, 161))
        self.dwnlod_playlist_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.dwnlod_playlist_btn.setStyleSheet("QPushButton {\n"
"\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.dwnlod_playlist_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dwnlod_playlist_btn.setIcon(icon1)
        self.dwnlod_playlist_btn.setIconSize(QtCore.QSize(150, 150))
        self.dwnlod_playlist_btn.setObjectName("dwnlod_playlist_btn")
        self.verticalLayout_3.addWidget(self.dwnlod_playlist_btn)
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setMaximumSize(QtCore.QSize(161, 16777215))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dwnlod_video_btn = QtWidgets.QPushButton(Form)
        self.dwnlod_video_btn.setMinimumSize(QtCore.QSize(161, 161))
        self.dwnlod_video_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.dwnlod_video_btn.setStyleSheet("QPushButton {\n"
"\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.dwnlod_video_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/icons8.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dwnlod_video_btn.setIcon(icon2)
        self.dwnlod_video_btn.setIconSize(QtCore.QSize(150, 150))
        self.dwnlod_video_btn.setObjectName("dwnlod_video_btn")
        self.verticalLayout_2.addWidget(self.dwnlod_video_btn)
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setMaximumSize(QtCore.QSize(161, 16777215))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.search_song_btn = QtWidgets.QPushButton(Form)
        self.search_song_btn.setMinimumSize(QtCore.QSize(161, 161))
        self.search_song_btn.setMaximumSize(QtCore.QSize(161, 161))
        self.search_song_btn.setStyleSheet("QPushButton {\n"
"\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #827397;\n"
"}")
        self.search_song_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/icons8-search-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_song_btn.setIcon(icon3)
        self.search_song_btn.setIconSize(QtCore.QSize(100, 100))
        self.search_song_btn.setObjectName("search_song_btn")
        self.verticalLayout.addWidget(self.search_song_btn)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setMaximumSize(QtCore.QSize(161, 16777215))
        font = QtGui.QFont()
        font.setFamily("Acumin Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("font: 20pt \"Acumin Pro\";\n"
"\n"
" border-radius: 7px;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem6 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet(" border-radius: 12px;\n"
"")
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem7, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eazy Downloader"))
        self.label_11.setText(_translate("Form", "Download Playlist"))
        self.label_12.setText(_translate("Form", "Download single video"))
        self.label_13.setText(_translate("Form", "search by name"))
        self.label_4.setText(_translate("Form", "Eazy Downloader"))
import app_resources_rc
