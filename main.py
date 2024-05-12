import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QErrorMessage
from Waybills import Ui_MainWindow
import data


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadWayBills()
        self.ui.waybillDeleteButton.clicked.connect(self.deleteWaybill)

    def loadWayBills(self):
        waybills = data.WaybillData()
        waybill_list = waybills.get_waybill_list()
        self.ui.waybillList.addItems(waybill_list)
        self.ui.waybillList.setCurrentRow(0)

    def deleteWaybill(self):
        current_index = self.ui.waybillList.currentRow()
        item = self.ui.waybillList.item(current_index)
        if item is None:
            return
        question = QMessageBox.question(self, 'Удаление путевого листа',
                                        'Вы точно хотите удалить выбранный путевой лист\n'
                                        f'{item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.ui.waybillList.takeItem(current_index)
            data.WaybillData().remove_waybill_file(item.text())
            del item

def app():
    app = QApplication(sys.argv)
    win = Appl()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
