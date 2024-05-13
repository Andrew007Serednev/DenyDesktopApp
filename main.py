import sys
from data_provider import WaybillData, Driver
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from forms.Waybills import Ui_MainWindow
from forms.WaybillUnit import Ui_Dialog as WaybillUnitDialog
from forms.NewDriver import Ui_Dialog as NewDriverDialog


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadWayBills()
        self.ui.waybillCreateButton.clicked.connect(self.openWaybillUnit)
        self.ui.waybillDeleteButton.clicked.connect(self.deleteWaybill)
        #Menu
        self.ui.action_5.triggered.connect(self.openNewDriver)
        #Dialogs
        self.ui_new_driver = NewDriverDialog()

    def openNewDriver(self):
        global NewDriver
        NewDriver = QtWidgets.QDialog()
        self.ui_new_driver.setupUi(NewDriver)
        self.loadDriversList()
        NewDriver.show()

    def loadDriversList(self):
        drivers = Driver()
        drivers_list = drivers.get_driver_fio_list()
        print(drivers_list)
        self.ui_new_driver.drivers_list.addItems(drivers_list)
        self.ui_new_driver.drivers_list.setCurrentRow(0)

    def loadWayBills(self):
        waybills = WaybillData()
        waybill_list = waybills.get_waybill_list()
        self.ui.waybillList.addItems(waybill_list)
        self.ui.waybillList.setCurrentRow(0)

    def openWaybillUnit(self):
        global WaybillUnit
        WaybillUnit = QtWidgets.QDialog()
        ui_waybillunit = WaybillUnitDialog()
        ui_waybillunit.setupUi(WaybillUnit)
        WaybillUnit.show()

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
            WaybillData().remove_waybill_file(item.text())
            del item


def app():
    app = QApplication(sys.argv)
    win = Appl()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
