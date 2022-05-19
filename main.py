import json
import os
import sys
from dotenv import load_dotenv
from GUI.MainGUIWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from API import SpotifyAPI

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def main():
    client = SpotifyAPI.SpotifyAPI(CLIENT_ID, CLIENT_SECRET)
    data = client.get_artist_info('i declare war')
    print(json.dumps(data, indent=2))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
