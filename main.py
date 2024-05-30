#! /usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from data_provider import WaybillData, Driver
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from forms.Waybills import Ui_MainWindow
from forms.WaybillUnit import Ui_Dialog as WaybillUnitDialog
from forms.NewDriver import Ui_Dialog as NewDriverDialog
from forms.Route import Ui_Dialog as NewRouteDialog


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_waybills()
        self.ui.waybillCreateButton.clicked.connect(self.open_waybill_unit)
        self.ui.waybillDeleteButton.clicked.connect(self.delete_waybill)

        # Menu
        self.ui.action_5.triggered.connect(self.open_new_driver)
        self.ui.action_9.triggered.connect(self.open_new_route)

        # Dialogs. Drivers
        self.ui_new_driver = NewDriverDialog()

        # Dialogs. Route
        self.ui_new_route = NewRouteDialog()

    def open_new_driver(self):
        global NewDriver
        NewDriver = QtWidgets.QDialog()
        self.ui_new_driver.setupUi(NewDriver)
        self.load_drivers_list()
        NewDriver.show()
        self.ui_new_driver.driver_save_button.clicked.connect(self.save_new_driver)
        self.ui_new_driver.driver_delete_button.clicked.connect(self.remove_driver_from_list)

    def load_drivers_list(self):
        drivers_list = Driver().get_driver_fio_list_logic()
        # print(drivers_list)
        self.ui_new_driver.drivers_list.addItems(drivers_list)
        self.ui_new_driver.drivers_list.setCurrentRow(0)

    def save_new_driver(self):
        new_driver_fio_edit = self.ui_new_driver.new_driver_fio_edit.text()
        new_driver_snils_edit = self.ui_new_driver.new_driver_snils_edit.text()
        new_driver_license_edit = self.ui_new_driver.new_driver_license_edit.text()
        new_driver_start_date = self.ui_new_driver.new_driver_start_date.date().getDate()
        new_driver_end_date = self.ui_new_driver.new_driver_end_date.date().getDate()
        driver_set = {
                'new_driver_fio': new_driver_fio_edit,
                'new_driver_snils': new_driver_snils_edit,
                'new_driver_license': new_driver_license_edit,
                'new_driver_start_date': new_driver_start_date,
                'new_driver_end_date': new_driver_end_date
        }
        Driver().set_new_driver_logic(driver_set)
        self.ui_new_driver.drivers_list.clear()
        self.load_drivers_list()

    def remove_driver_from_list(self):
        current_index = self.ui_new_driver.drivers_list.currentRow()
        item = self.ui_new_driver.drivers_list.item(current_index)
        if item is None:
            return
        question = QMessageBox.question(self, 'Удаление путевого листа',
                                        'Вы точно хотите удалить выбранный путевой лист\n'
                                        f'{item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.ui_new_driver.drivers_list.takeItem(current_index)
            Driver().remove_driver_from_list_logic(item.text())
            del item

    def open_new_route(self):
        global NewRoute
        NewRoute = QtWidgets.QDialog()
        self.ui_new_route.setupUi(NewRoute)
        NewRoute.show()

    def load_waybills(self):
        waybills = WaybillData()
        waybill_list = waybills.get_waybill_list()
        self.ui.waybillList.addItems(waybill_list)
        self.ui.waybillList.setCurrentRow(0)

    def open_waybill_unit(self):
        global WaybillUnit
        WaybillUnit = QtWidgets.QDialog()
        ui_waybillunit = WaybillUnitDialog()
        ui_waybillunit.setupUi(WaybillUnit)
        WaybillUnit.show()

    def delete_waybill(self):
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
