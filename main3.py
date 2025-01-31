import sys
import os

import datetime
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import file_opener
import finder_9_3

home = str(Path.home())
first_char = len(home)
dir_list = os.listdir(home)

found1 = True
globReady = False



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):
        #self.cur_dir = home
        self.cur_dir = ''
        self.cur_word = None
        self.search_button = QPushButton('Search')
        self.ok_button = QPushButton('Ok')

        self.clicked_search = False
        self.search_button.clicked.connect(self.search_btn_clicked)

        self.searchEdit = QLineEdit()

        self.listwidget = QListWidget()

        self.listwidget.setFixedSize(1100, 400)
        self.listwidget.itemClicked.connect(self.btn_ok_result)


        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(self.searchEdit, 1, 0)
        layout.addWidget(self.search_button, 1, 1)
        layout.addWidget(self.listwidget, 2, 0, 1, 6)
        layout.addWidget(self.ok_button, 6, 1)
        #layout.addWidget(self.exit_button, 6, 2)


        self.setLayout(layout)
        self.setGeometry(300, 200, 1100, 700)
        self.show()

    def search_btn_clicked(self, text_input):
        self.clicked_search = True
        sender = self.sender()
        words = self.searchEdit.text()
        self.cur_word = words
        keyword = words.strip()
        if(globReady == True):
            list_of_search_results = finder_9_3.searchDomain(keyword)

        self.listwidget.clear()

        for item in list_of_search_results:
            item = os.path.join(self.cur_dir, item)
            if os.path.isfile(item):
                icon = QtGui.QIcon('hard-drive-disk-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            elif os.path.isdir(item):
                icon = QtGui.QIcon('folder-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            else:
                icon = QtGui.QIcon('hard-drive-disk-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''


### Highliter
    def btn_ok_result(self, file):
        # print(file.text())
        # print(self.clicked_search)

        if self.clicked_search is not False:
            # print(self.clicked_search)
            # print(self.cur_word)
            if file.text()[-4:] == 'xlsx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == 'docx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == 'pptx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    # w.show()

    while (found1):
        finder_9_3.creat()
        found1 = False
        globReady = True
    sys.exit(app.exec_())
