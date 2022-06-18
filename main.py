import sys

from PyQt5 import QtWidgets
from GUI.MainGUIWindow import Ui_MainWindow


def main():
    """Main driver

    :return:
    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
