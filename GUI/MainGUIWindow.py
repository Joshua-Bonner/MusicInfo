# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Resources\QtDesignerUIs\MainGUIWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
import sys
import os
from dotenv import load_dotenv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QEvent, Qt
from API import SpotifyAPI


class TextEdit(QtWidgets.QTextEdit):
    """Subclass of a QTextEdit that will allow the altering of the way in
       which certain events are handled

    """

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            return
        super().keyPressEvent(event)


class Ui_MainWindow(object):
    """Main UI Class that will utilize the SpotifyAPI

    """

    def __init__(self):
        # Grab .env variables
        load_dotenv()
        CLIENT_ID = os.getenv('CLIENT_ID')
        CLIENT_SECRET = os.getenv('CLIENT_SECRET')

        # Instantiate a SpotifyAPI client object
        self.client = SpotifyAPI.SpotifyAPI(CLIENT_ID, CLIENT_SECRET)

        # Initialize class variables
        self.musicData = dict()
        self.dataKeys = list()
        self.curIndex = 0

    def setupUi(self, MainWindow):
        """Defines and sets up GUI objects using a MainWindow object
           Most of this was automatically generated by PyQt5 generator

        :param MainWindow: PyQt5 object instantiated in main
        :return:
        """

        # MAIN WINDOW
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # SEARCH PROMPT LABEL
        self.searchPrompt = QtWidgets.QLabel(self.centralwidget)
        self.searchPrompt.setGeometry(QtCore.QRect(10, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.searchPrompt.setFont(font)
        self.searchPrompt.setObjectName("searchPrompt")

        # SEARCH FIELD TEXTEDIT
        self.searchField = TextEdit(self.centralwidget)
        self.searchField.setEnabled(True)
        self.searchField.setGeometry(QtCore.QRect(100, 10, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.searchField.setFont(font)
        self.searchField.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.searchField.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.searchField.setInputMethodHints(QtCore.Qt.ImhNone)
        self.searchField.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.searchField.setLineWidth(15)
        self.searchField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchField.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchField.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.searchField.setDocumentTitle("")
        self.searchField.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        # SEARCH BY LABEL
        self.by = QtWidgets.QLabel(self.centralwidget)
        self.by.setGeometry(QtCore.QRect(550, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.by.setFont(font)
        self.by.setObjectName("by")

        # SEARCH BUTTON
        self.searchBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.search())
        self.searchBtn.setGeometry(QtCore.QRect(420, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchBtn.setFont(font)
        self.searchBtn.setDefault(False)
        self.searchBtn.setFlat(False)
        self.searchBtn.setObjectName("searchBtn")

        # LINE
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 671, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # MUSIC INFO LABEL
        self.musicInfoLabel = QtWidgets.QLabel(self.centralwidget)
        self.musicInfoLabel.setGeometry(QtCore.QRect(10, 110, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.musicInfoLabel.setFont(font)
        self.musicInfoLabel.setObjectName("musicInfoLabel")

        # CLOSE BUTTON
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: sys.exit())
        self.closeBtn.setGeometry(QtCore.QRect(580, 400, 101, 31))
        self.closeBtn.setObjectName("closeBtn")

        # SEARCH BOX
        self.searchBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchBox.setGeometry(QtCore.QRect(590, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchBox.setFont(font)
        self.searchBox.setAutoFillBackground(False)
        self.searchBox.setFrame(True)
        self.searchBox.setObjectName("searchBox")
        self.searchBox.addItem("")
        self.searchBox.addItem("")
        self.searchBox.addItem("")

        # NEXT BUTTON
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showNextEntry())
        self.nextBtn.setEnabled(False)
        self.nextBtn.setGeometry(QtCore.QRect(580, 100, 81, 31))
        self.nextBtn.setObjectName("nextBtn")

        # PREVIOUS BUTTON
        self.PrevBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showPrevEntry())
        self.PrevBtn.setEnabled(False)
        self.PrevBtn.setGeometry(QtCore.QRect(490, 100, 81, 31))
        self.PrevBtn.setDefault(False)
        self.PrevBtn.setObjectName("PrevBtn")

        # MUSIC INFO QTEXTBROWSER
        self.infoTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.infoTextBrowser.setGeometry(QtCore.QRect(10, 140, 671, 251))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.infoTextBrowser.setFont(font)
        self.infoTextBrowser.setObjectName("infoTextBrowser")

        MainWindow.setCentralWidget(self.centralwidget)

        # MENU BAR
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")

        # MENU FILE
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        # MENU ABOUT
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)

        # MENU QUIT SELECTION
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(lambda: sys.exit())

        # MENU ABOUT SELECTION
        # TODO: Complete implementation of About Page
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def resetState(self):
        """Resets class variables to initial state

        :return:
        """
        self.musicData = {}
        self.dataKeys = []
        self.curIndex = 0
        self.nextBtn.setEnabled(False)
        self.PrevBtn.setEnabled(False)
        self.infoTextBrowser.setPlainText('')

    def search(self):
        """GUI hook up for when the searchBtn is pressed.
           Uses the search functionality present in the SpotifyAPI class

        :return:
        """
        # reset state of GUI class variables
        self.resetState()

        # grab search string from user input in the GUI
        searchString = self.searchField.toPlainText()
        queryType = self.searchBox.currentText()

        # call to SpotifyAPI depending on the type of search
        try:
            if queryType == 'Artist':
                self.musicData = self.client.get_artist_info(searchString)
            elif queryType == 'Album':
                self.musicData = self.client.get_album_info(searchString)
            elif queryType == 'Track':
                self.musicData = self.client.get_track_info(searchString)
            else:
                print("Error")
        except:
            print("No search string provided!")

        # set keys object
        self.dataKeys = list(self.musicData.keys())

        # set text browser with information retrieved from the SpotifyAPI
        try:
            if len(self.dataKeys) == 0:
                self.infoTextBrowser.setPlainText(queryType + " \"" + searchString + "\" does not exist on Spotify!")
            if len(self.dataKeys) >= 1:
                self.infoTextBrowser.setPlainText(self.displayData())
                if len(self.dataKeys) > 1:
                    self.nextBtn.setEnabled(True)
        except:
            print("Error in UI search")

    def displayData(self) -> str:
        """Displays the current information by index in the musicData object

        :return: formatted string to be used by the infoTextBrowser UI object
        """
        retStr = ''
        curKey = self.dataKeys.__getitem__(self.curIndex)
        data = dict(self.musicData.get(curKey))
        for key in data.keys():
            retStr += key + ": " + str(data.get(key)).strip('[]') + "\n"
        return retStr

    def showNextEntry(self):
        """On click event for nextBtn to show next entry in the musicData object

        :return:
        """
        try:
            self.PrevBtn.setEnabled(True)
            self.curIndex += 1
            self.infoTextBrowser.setPlainText(self.displayData())
            if (list(self.dataKeys)[self.curIndex]) is not (list(self.dataKeys)[-1]):
                self.nextBtn.setEnabled(True)
            else:
                self.nextBtn.setEnabled(False)
        except:
            print("Next item does not exist")

    def showPrevEntry(self):
        """On click event for prevBtn to show previous entry in the musicData object

        :return:
        """
        try:
            if self.curIndex != 0:
                self.curIndex -= 1
                self.infoTextBrowser.setPlainText(self.displayData())
                if self.curIndex == 0:
                    self.PrevBtn.setEnabled(False)
                    self.nextBtn.setEnabled(True)
                else:
                    self.PrevBtn.setEnabled(True)
        except:
            print("Previous item does not exist")

    def retranslateUi(self, MainWindow):
        """Default function created by the PyQt5 library

        :param MainWindow:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Music Info"))
        self.searchPrompt.setText(_translate("MainWindow", "Search : "))
        self.searchField.setPlaceholderText(_translate("MainWindow", "Enter search query here"))
        self.by.setText(_translate("MainWindow", "By :"))
        self.searchBtn.setText(_translate("MainWindow", "Search"))
        self.musicInfoLabel.setText(_translate("MainWindow", "Music Info -"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.searchBox.setItemText(0, _translate("MainWindow", "Artist"))
        self.searchBox.setItemText(1, _translate("MainWindow", "Album"))
        self.searchBox.setItemText(2, _translate("MainWindow", "Track"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))
        self.PrevBtn.setText(_translate("MainWindow", "Prev"))
        self.infoTextBrowser.setPlaceholderText(_translate("MainWindow",
                                                           "\"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\""))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
