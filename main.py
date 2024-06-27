#! /usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import datetime

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from data_provider import orderData, Driver
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from forms.Orders import Ui_MainWindow
from forms.OrderUnit import Ui_Dialog as orderUnitDialog
from forms.NewDriver import Ui_Dialog as NewDriverDialog
from forms.Route import Ui_Dialog as NewRouteDialog


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_orders()
        self.ui.orderCreateButton.clicked.connect(self.open_order_unit)
        self.ui.orderDeleteButton.clicked.connect(self.delete_order)

        # Menu
        self.ui.action_5.triggered.connect(self.open_new_driver)
        self.ui.action_9.triggered.connect(self.open_new_route)

        # Dialogs. Drivers
        self.ui_new_driver = NewDriverDialog()

        # Dialogs. Route
        self.ui_new_route = NewRouteDialog()

    # DRIVERS
    def open_new_driver(self):
        global NewDriver
        NewDriver = QtWidgets.QDialog()
        self.ui_new_driver.setupUi(NewDriver)
        self.load_drivers_list()
        NewDriver.show()
        self.ui_new_driver.driver_save_button.clicked.connect(self.save_new_driver)
        self.ui_new_driver.driver_edit_button.clicked.connect(self.save_edited_driver)
        self.ui_new_driver.driver_delete_button.clicked.connect(self.remove_driver_from_list)
        self.ui_new_driver.drivers_list.itemClicked.connect(self.edit_driver_from_list)

    def load_drivers_list(self):
        drivers_list = Driver().get_driver_fio_list_logic()
        self.ui_new_driver.drivers_list.addItems(drivers_list)
        self.ui_new_driver.drivers_list.sortItems()
        self.ui_new_driver.drivers_list.setCurrentRow(0)

    def save_new_driver(self):
        new_driver_fio_edit = self.ui_new_driver.new_driver_fio_edit.text()
        new_driver_snils_edit = self.ui_new_driver.new_driver_snils_edit.text()
        new_driver_license_edit = self.ui_new_driver.new_driver_license_edit.text()
        new_driver_start_date = self.ui_new_driver.new_driver_start_date.date().getDate()
        new_driver_end_date = self.ui_new_driver.new_driver_end_date.date().getDate()
        new_item = QListWidgetItem(new_driver_fio_edit)
        if not Driver().check_uni_item(new_driver_fio_edit):
            self.ui_new_driver.drivers_list.addItem(new_item)
            print(f'NEW: {new_item.text()}')
            self.ui_new_driver.drivers_list.sortItems()
            # driver_index = self.ui_new_driver.drivers_list.indexFromItem(new_item).row()
            self.ui_new_driver.drivers_list.setCurrentItem(new_item)
            driver_set = {
                    # 'new_driver_id': driver_index,
                    'new_driver_fio': new_driver_fio_edit,
                    'new_driver_snils': new_driver_snils_edit,
                    'new_driver_license': new_driver_license_edit,
                    'new_driver_start_date': new_driver_start_date,
                    'new_driver_end_date': new_driver_end_date
            }
            Driver().save_new_driver_logic(driver_set)
            self.ui_new_driver.new_driver_fio_edit.clear()
            self.ui_new_driver.new_driver_snils_edit.clear()
            self.ui_new_driver.new_driver_license_edit.clear()
            self.ui_new_driver.new_driver_start_date.date().currentDate()
            self.ui_new_driver.new_driver_end_date.date().currentDate()
        else:
            QMessageBox.critical(self, 'Добавление водителя', f'Водитель {new_driver_fio_edit} существует',
                                 QMessageBox.Yes)

    def edit_driver_from_list(self):
        current_item = self.ui_new_driver.drivers_list.currentItem()
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        driver_edit_set = Driver().edit_driver_from_list_logic(current_item.text())
        print(f'EDIT: {driver_edit_set}')
        self.ui_new_driver.new_driver_fio_edit.setText(driver_edit_set['new_driver_fio'])
        self.ui_new_driver.new_driver_snils_edit.setText(driver_edit_set['new_driver_snils'])
        self.ui_new_driver.new_driver_license_edit.setText(driver_edit_set['new_driver_license'])
        self.ui_new_driver.new_driver_start_date.setDate(QDate(
            driver_edit_set['new_driver_start_date'][0],
            driver_edit_set['new_driver_start_date'][1],
            driver_edit_set['new_driver_start_date'][2]))
        self.ui_new_driver.new_driver_end_date.setDate(QDate(
            driver_edit_set['new_driver_end_date'][0],
            driver_edit_set['new_driver_end_date'][1],
            driver_edit_set['new_driver_end_date'][2]))
        print(f'UI EDIT: {driver_edit_set} \n')

    def save_edited_driver(self):
        current_item = self.ui_new_driver.drivers_list.currentItem()
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        edited_driver_fio_edit = self.ui_new_driver.new_driver_fio_edit.text()
        edited_driver_snils_edit = self.ui_new_driver.new_driver_snils_edit.text()
        edited_driver_license_edit = self.ui_new_driver.new_driver_license_edit.text()
        edited_driver_start_date = self.ui_new_driver.new_driver_start_date.date().getDate()
        edited_driver_end_date = self.ui_new_driver.new_driver_end_date.date().getDate()
        driver_set = {
                'new_driver_fio': edited_driver_fio_edit,
                'new_driver_snils': edited_driver_snils_edit,
                'new_driver_license': edited_driver_license_edit,
                'new_driver_start_date': edited_driver_start_date,
                'new_driver_end_date': edited_driver_end_date
        }
        Driver().update_edited_driver_logic(driver_set)
        self.ui_new_driver.drivers_list.clear()
        self.load_drivers_list()
        self.ui_new_driver.drivers_list.sortItems()
        print(f'UI SAVE EDIT: {driver_set} \n')

    def remove_driver_from_list(self):
        current_item = self.ui_new_driver.drivers_list.currentItem()
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        if current_item is None:
            return
        question = QMessageBox.question(self, 'Удаление водителя',
                                        'Вы точно хотите удалить выбранного водителя\n'
                                        f'{current_item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.ui_new_driver.drivers_list.takeItem(self.ui_new_driver.drivers_list.indexFromItem(current_item).row())
            Driver().remove_driver_from_list_logic(current_item.text())
            print(f'UI DEL: {current_item.text()} \n')
            del current_item

    # ROUTES
    def open_new_route(self):
        global NewRoute
        NewRoute = QtWidgets.QDialog()
        self.ui_new_route.setupUi(NewRoute)
        NewRoute.show()

    # ORDERS
    def load_orders(self):
        orders = orderData()
        order_list = orders.get_order_list()
        self.ui.orderList.addItems(order_list)
        self.ui.orderList.setCurrentRow(0)

    def open_order_unit(self):
        global orderUnit
        orderUnit = QtWidgets.QDialog()
        ui_orderunit = orderUnitDialog()
        ui_orderunit.setupUi(orderUnit)
        orderUnit.show()

    def delete_order(self):
        current_index = self.ui.orderList.currentRow()
        item = self.ui.orderList.item(current_index)
        if item is None:
            return
        question = QMessageBox.question(self, 'Удаление путевого листа',
                                        'Вы точно хотите удалить выбранный путевой лист\n'
                                        f'{item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.ui.orderList.takeItem(current_index)
            orderData().remove_order_file(item.text())
            del item


def app():
    app = QApplication(sys.argv)
    win = Appl()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
