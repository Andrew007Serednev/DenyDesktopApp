import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Waybills import Ui_MainWindow
import data


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadWayBills()

    def loadWayBills(self):
        jsonData = data.JsonData()
        waybil_list = jsonData.get_waybill_list()
        self.ui.waybillList.addItems(waybil_list)
        self.ui.waybillList.setCurrentRow(0)


def app():
    app = QApplication(sys.argv)
    win = Appl()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
