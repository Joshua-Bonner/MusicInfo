import sys

from PyQt5 import QtWidgets
from GUI.MainGUIWindow import Ui_MainWindow


def main():
    # data = client.get_artist_info('i declare war')
    # print(json.dumps(data, indent=2))
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
