import os
import warnings
import uuid
from utils import resource_path
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from pytube import YouTube
from PyQt5.QtWidgets import QFileDialog

warnings.filterwarnings("ignore", category=DeprecationWarning)


class DownloadThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self, url, path, audio_only=False):
        QThread.__init__(self)
        self.url = url
        self.path = path
        self.audio_only = audio_only

    def rename_out_file(self, out_file):
        mp3, mp4 = '.mp3', '.mp4'
        base, ext = os.path.splitext(out_file)
        if out_file.endswith(mp3):
            new_file = base + uuid.uuid4().hex + mp3
        elif out_file.endswith(mp4):
            new_file = base + uuid.uuid4().hex + mp4

        os.rename(out_file, new_file)

    def run(self):
        try:
            yt = YouTube(self.url)
            if self.audio_only:
                yt = YouTube(self.url)

                video = yt.streams.filter(only_audio=True).first()

                out_file = video.download(output_path=self.path)
                self.rename_out_file(out_file)

            else:
                vid = yt.streams.get_highest_resolution()
                out = vid.download(self.path)
                self.rename_out_file(out)

            self.signal.emit("Download completed!")
        except Exception as e:
            self.signal.emit("Connection Problem!")


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 211)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 271, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 160, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 80, 131, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Youtube Downloader"))
        icon = QIcon(resource_path('ytb.ico'))
        Dialog.setWindowIcon(icon)
        self.label.setText(_translate("Dialog", "URL"))
        self.label_2.setText(_translate("Dialog", "Path"))
        self.pushButton.setText(_translate("Dialog", "Video"))
        self.pushButton_2.setText(_translate("Dialog", "Audio"))
        self.pushButton_3.setText(_translate("Dialog", "Choose Folder"))

        self.pushButton.clicked.connect(self.download_video)
        self.pushButton_2.clicked.connect(self.download_audio)
        self.pushButton_3.clicked.connect(self.open_folder)

    def open_folder(self):
        self.file = str(QFileDialog.getExistingDirectory(
            None, "Select Directory"))

    def download_video(self):
        got_link = self.lineEdit.text()

        if len(got_link.strip()) == 0:
            QMessageBox.critical(None, "Error", "Empty URL!")
            return
        try:
            got_path = self.file
        except:
            QMessageBox.critical(None, "Error", "Empty PATH!")
            return
        self.download_thread = DownloadThread(got_link, got_path)
        self.download_thread.signal.connect(self.download_finished)
        self.download_thread.start()

    def download_audio(self):

        got_link = self.lineEdit.text()

        if len(got_link.strip()) == 0:
            QMessageBox.critical(None, "Error", "Empty URL!")
            return
        try:
            got_path = self.file
        except:
            QMessageBox.critical(None, "Error", "Empty PATH!")
            return

        self.download_thread = DownloadThread(
            got_link, got_path, audio_only=True)
        self.download_thread.signal.connect(self.download_finished)
        self.download_thread.start()

    def download_finished(self, message):
        if "Download completed!" in message:
            os.startfile(self.download_thread.path)
            QMessageBox.information(None, "Notify", "Success!")
            self.lineEdit.clear()
        else:
            QMessageBox.critical(None, "Error", message)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
