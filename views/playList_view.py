# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/playList_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(914, 650)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bck_btn = QtWidgets.QPushButton(Form)
        self.bck_btn.setMinimumSize(QtCore.QSize(50, 50))
        self.bck_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.bck_btn.setStyleSheet("QPushButton {\n"
"    padding: 2px;\n"
"    font: bold 15px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"")
        self.bck_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icons8-back-67.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bck_btn.setIcon(icon)
        self.bck_btn.setIconSize(QtCore.QSize(30, 30))
        self.bck_btn.setObjectName("bck_btn")
        self.horizontalLayout_4.addWidget(self.bck_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("font: 20pt \"Acumin Pro\";\n"
"\n"
" border-radius: 7px;\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setStyleSheet(" border-radius: 12px;\n"
"")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setStyleSheet("background-color: rgb(170, 170, 255,0);")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setStyleSheet("background-color: rgb(0, 255, 255,0);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"\n"
" border-radius: 7px;\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.link_lin = QtWidgets.QLineEdit(self.frame)
        self.link_lin.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Alex")
        font.setPointSize(10)
        self.link_lin.setFont(font)
        self.link_lin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.link_lin.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.link_lin.setInputMask("")
        self.link_lin.setText("")
        self.link_lin.setAlignment(QtCore.Qt.AlignCenter)
        self.link_lin.setObjectName("link_lin")
        self.horizontalLayout.addWidget(self.link_lin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_2.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"\n"
" border-radius: 7px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.path_lbl = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Alex")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.path_lbl.setFont(font)
        self.path_lbl.setStyleSheet("\n"
"\n"
" border-radius: 7px;\n"
"")
        self.path_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.path_lbl.setObjectName("path_lbl")
        self.horizontalLayout_2.addWidget(self.path_lbl)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.editPath_btn = QtWidgets.QPushButton(self.frame)
        self.editPath_btn.setMinimumSize(QtCore.QSize(20, 20))
        self.editPath_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.editPath_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"\n"
" border-radius: 7px;\n"
"")
        self.editPath_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/Untitled-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editPath_btn.setIcon(icon2)
        self.editPath_btn.setIconSize(QtCore.QSize(20, 20))
        self.editPath_btn.setObjectName("editPath_btn")
        self.horizontalLayout_2.addWidget(self.editPath_btn)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.download_btn = QtWidgets.QPushButton(self.frame)
        self.download_btn.setMinimumSize(QtCore.QSize(183, 51))
        self.download_btn.setMaximumSize(QtCore.QSize(300, 51))
        self.download_btn.setStyleSheet("font: 14pt \"Acumin Pro\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(20,  190, 120);\n"
"\n"
" border-radius: 7px;\n"
"")
        self.download_btn.setObjectName("download_btn")
        self.horizontalLayout_3.addWidget(self.download_btn)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem10, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Eazy Downloader"))
        self.label_4.setText(_translate("Form", "Youtube playlist Downloader"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Description"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Status"))
        self.label.setText(_translate("Form", "Enter playlist link :"))
        self.link_lin.setPlaceholderText(_translate("Form", "Playlist Link"))
        self.label_2.setText(_translate("Form", "Default path : "))
        self.path_lbl.setText(_translate("Form", "Select Path ........."))
        self.download_btn.setText(_translate("Form", "Start Download"))
import app_resources_rc