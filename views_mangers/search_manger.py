from PyQt5 import QtWidgets , QtCore , QtGui
from views import search_view
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog , QApplication
from pytube import Search
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

class SearchManager(QtWidgets.QWidget, search_view.Ui_Form):
    # checkAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(SearchManager, self).__init__()
        self.setupUi(self)
        self.search_btn.clicked.connect(self.run)
    def run(self):
        msg = QtWidgets.QMessageBox()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg.setWindowIcon(icon)

        if len(self.link_lin.text()) != 0 :
            self.tableWidget.setRowCount(0)
            rowPosition = self.tableWidget.rowCount()
            items_list = []
            try :
                keyword = Search((self.link_lin.text()))
                for item in keyword.results :
                    items_list.append(item)

                for item in items_list[::-1]:
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(0, 0, QTableWidgetItem(item.title))
                    self.tableWidget.setItem(0, 1, QTableWidgetItem(item.watch_url ))

            except Exception as search_error :
                print(search_error)
        else:
            msg.setWindowTitle("Warning")
            msg.setText("You must enter keyword ! ")
            msg.setIcon(QMessageBox.Critical)
            msg.setStyleSheet('''font: 12pt "Acumin Pro";''')
            msg.exec_()
if __name__ == "__main__":
    import qdarkstyle
    app = QtWidgets.QApplication([])
    w = SearchManager()
    w.show()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()

# header = self.tableWidget.horizontalHeader()
# header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
# header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

