import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.setWindowTitle("Программа")
        self.setGeometry(300, 250, 500, 500)


def application():
    app = QApplication(sys.argv)
    window = Appl()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
