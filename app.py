# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox

from pytubefix import YouTube

import requests
from io import BytesIO

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 781, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.show_button = QtWidgets.QPushButton(parent=self.tab)
        self.show_button.setGeometry(QtCore.QRect(590, 40, 171, 28))
        self.show_button.setCheckable(True)
        self.show_button.setObjectName("show_button")
        self.show_button.clicked.connect(self.check_info    )
        self.get_link = QtWidgets.QLineEdit(parent=self.tab)
        self.get_link.setGeometry(QtCore.QRect(80, 40, 501, 22))
        self.get_link.setObjectName("get_link")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 751, 271))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 731, 22))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(parent=self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(340, 80, 391, 171))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 321, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("A:\Projects\YTDownApp\images\youtube.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)
        self.label_3 = QtWidgets.QLabel(parent=self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 360, 55, 16))
        self.label_3.setObjectName("label_3")
        self.save_path = QtWidgets.QLineEdit(parent=self.tab)
        self.save_path.setGeometry(QtCore.QRect(60, 360, 501, 22))
        self.save_path.setObjectName("save_path")
        self.save_path.setText("Comming Soon...")
        self.pushButton = QtWidgets.QPushButton(parent=self.tab)
        self.pushButton.setGeometry(QtCore.QRect(570, 360, 191, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click)
        self.show_button_2 = QtWidgets.QPushButton(parent=self.tab)
        self.show_button_2.setGeometry(QtCore.QRect(320, 440, 121, 28))
        self.show_button_2.setObjectName("show_button_2")
        self.show_button_2.clicked.connect(self.download_video)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.show_button.setText(_translate("MainWindow", "Check"))
        self.label.setText(_translate("MainWindow", "Video Link"))
        self.groupBox.setTitle(_translate("MainWindow", "Information"))
        self.label_3.setText(_translate("MainWindow", "Save in"))
        self.pushButton.setText(_translate("MainWindow", "Choose"))
        self.show_button_2.setText(_translate("MainWindow", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Check"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings"))

    
    def check_info(self):
        url = self.get_link.text()
        yt = YouTube(url)
        title = yt.title
        description = yt.description
        img = yt.thumbnail_url
        self.lineEdit.setText(title)
        self.textEdit.setText(description)
        pixmap = self.load_image_from_url(img)
        if pixmap:
            self.label_2.setPixmap(pixmap)
        else:
            self.label_2.setText("Image not downloaded")

    def load_image_from_url(self, link):
        try:
            responce = requests.get(link)
            responce.raise_for_status()
            image_data = BytesIO(responce.content)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(image_data.read())
            
            return pixmap
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None
    def on_click(self):
        coming = QMessageBox()
        coming.setWindowTitle("Comming Soon... - by HorekiSun")
        coming.setText("    Comming Soon...")
        coming.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close
        )
        coming.exec()

    def download_video(self):
        url = self.get_link.text()
        video = YouTube(url)
        downloader = video.streams.get_highest_resolution()
        downloader.download()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
