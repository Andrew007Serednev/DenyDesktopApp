#! /usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import datetime

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from data_provider import Order, Driver, Bus, Route
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from forms.Orders import Ui_MainWindow
from forms.OrderUnit import Ui_Dialog as orderUnitDialog
from forms.NewDriver import Ui_Dialog as NewDriverDialog
from forms.NewBus import Ui_Dialog as NewBusDialog
from forms.NewRoute import Ui_Dialog as NewRouteDialog


class Appl(QMainWindow):
    def __init__(self):
        super(Appl, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_orders()
        self.plan_order_date()

        self.ui.calendar_order.clicked.connect(self.plan_order_date)
        self.ui.create_plan_order_button.clicked.connect(self.create_plan_order)
        self.ui.add_time_to_plan_button.clicked.connect(self.add_order_time)
        self.ui.order_edit_button.clicked.connect(self.open_order_unit)
        # self.ui.order_create_button.clicked.connect(self.open_new_order_unit)
        self.ui.order_delete_button.clicked.connect(self.delete_order_unit)

        # Menu
        self.ui.action_5.triggered.connect(self.open_new_driver)
        self.ui.action_8.triggered.connect(self.open_new_bus)
        self.ui.action_9.triggered.connect(self.open_new_route)

        # Dialogs
        self.ui_new_driver = NewDriverDialog()
        self.ui_new_bus = NewBusDialog()
        self.ui_new_route = NewRouteDialog()

    # ORDERS
    def load_orders(self):
        route_list = Route().get_route_list_logic()
        self.ui.route_order_list.addItems(sorted(route_list))

    def plan_order_date(self):
        self.order_date = self.ui.calendar_order.selectedDate().toString('dd-MM-yy')
        orders = Order()
        order_list = orders.get_order_list_logic(self.order_date)
        self.ui.order_list.clear()
        self.ui.order_list.addItems(order_list)
        self.ui.order_list.setCurrentRow(0)
        self.ui.order_list.sortItems()
        return self.order_date

    def create_plan_order(self):
        order_date = self.plan_order_date()
        order_route = self.ui.route_order_list.currentText()
        order_count = self.ui.order_count_list.currentText()
        orders_plan_list = []
        for order_num in range(int(order_count)):
            orders_plan_set = {
                'new_order_date': order_date,
                'new_order_route': order_route,
                'new_order_num': order_num + 1
            }
            if not Order().check_uni_item(order_date, order_route):
                orders_plan_list.append(orders_plan_set)
            else:
                QMessageBox.critical(self, 'Добавление графика', f'График на дату {order_date} \n для маршрута '
                                                                 f'{order_route} существует', QMessageBox.Yes)
        print(f'ORDER PLAN: {orders_plan_list}')
        Order().create_orders_plan(orders_plan_list)
        self.plan_order_date()

    def add_order_time(self):
        current_item = self.ui.order_list.currentItem().text()
        print(f'UI ITEM: {current_item} \n')
        planned_order_time = self.ui.time_order_edit.time().toString('hh:mm')
        order_set = {
            'planned_order_time': planned_order_time
        }
        print(f'UI SAVE EDIT: {order_set} \n')
        order_time = Order().add_order_time_logic(current_item, order_set)
        print(f'TIME: {order_time}, {type(order_time)}')


    def open_order_unit(self):
        global orderUnit
        orderUnit = QtWidgets.QDialog()
        ui_orderunit = orderUnitDialog()
        ui_orderunit.setupUi(orderUnit)
        orderUnit.show()

    def delete_order_unit(self):
        current_index = self.ui.order_list.currentRow()
        item = self.ui.order_list.item(current_index)
        if item is None:
            return
        question = QMessageBox.question(self, 'Удаление путевого листа',
                                        'Вы точно хотите удалить выбранный путевой лист\n'
                                        f'{item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            item = self.ui.order_list.takeItem(current_index)
            Order().remove_order_file(item.text())
            del item

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
        current_item = self.ui_new_driver.drivers_list.currentItem().text()  # Антон
        print(f'UI SAVE ITEM: {current_item} \n')
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        edited_driver_fio_edit = self.ui_new_driver.new_driver_fio_edit.text()
        edited_driver_snils_edit = self.ui_new_driver.new_driver_snils_edit.text()
        edited_driver_license_edit = self.ui_new_driver.new_driver_license_edit.text()
        edited_driver_start_date = self.ui_new_driver.new_driver_start_date.date().getDate()
        edited_driver_end_date = self.ui_new_driver.new_driver_end_date.date().getDate()
        driver_set = {
                'new_driver_fio': edited_driver_fio_edit,  # Вася
                'new_driver_snils': edited_driver_snils_edit,
                'new_driver_license': edited_driver_license_edit,
                'new_driver_start_date': edited_driver_start_date,
                'new_driver_end_date': edited_driver_end_date
        }
        print(f'UI SAVE EDIT: {driver_set} \n')
        if edited_driver_fio_edit != current_item:
            if not Driver().check_uni_item(edited_driver_fio_edit):
                Driver().update_edited_driver_logic(driver_set, current_item)
            else:
                QMessageBox.critical(self, 'Добавление водителя', f'Водитель {edited_driver_fio_edit} существует',
                                     QMessageBox.Yes)
        else:
            Driver().update_edited_driver_logic(driver_set, current_item)
        self.ui_new_driver.drivers_list.clear()
        self.load_drivers_list()
        self.ui_new_driver.drivers_list.sortItems()

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

    #BUS
    def open_new_bus(self):
        global NewBus
        NewBus = QtWidgets.QDialog()
        self.ui_new_bus.setupUi(NewBus)
        self.load_bus_list()
        NewBus.show()
        self.ui_new_bus.bus_save_button.clicked.connect(self.save_new_bus)
        self.ui_new_bus.bus_edit_button.clicked.connect(self.save_edited_bus)
        self.ui_new_bus.bus_delete_button.clicked.connect(self.remove_bus_from_list)
        self.ui_new_bus.bus_list.itemClicked.connect(self.edit_bus_from_list)

    def load_bus_list(self):
        bus_list = Bus().get_bus_list_logic()
        self.ui_new_bus.bus_list.addItems(bus_list)
        self.ui_new_bus.bus_list.sortItems()
        self.ui_new_bus.bus_list.setCurrentRow(0)

    def save_new_bus(self):
        new_bus_num_edit = self.ui_new_bus.new_bus_num_edit.text()
        new_bus_gosnomer_edit = self.ui_new_bus.new_bus_gosnomer_edit.text()
        new_bus_model_edit = self.ui_new_bus.new_bus_model_edit.text()
        new_bus_odometr_edit = self.ui_new_bus.new_bus_odometr_edit.text()
        new_item = QListWidgetItem(new_bus_num_edit)
        if not Bus().check_uni_item(new_bus_num_edit):
            self.ui_new_bus.bus_list.addItem(new_item)
            print(f'NEW: {new_item.text()}')
            self.ui_new_bus.bus_list.sortItems()
            self.ui_new_bus.bus_list.setCurrentItem(new_item)
            bus_set = {
                    'new_bus_num': new_bus_num_edit,
                    'new_bus_gosnomer': new_bus_gosnomer_edit,
                    'new_bus_model': new_bus_model_edit,
                    'new_bus_odometr': new_bus_odometr_edit
            }
            Bus().save_new_bus_logic(bus_set)
            self.ui_new_bus.new_bus_num_edit.clear()
            self.ui_new_bus.new_bus_gosnomer_edit.clear()
            self.ui_new_bus.new_bus_model_edit.clear()
            self.ui_new_bus.new_bus_odometr_edit.clear()
        else:
            QMessageBox.critical(self, 'Добавление автобуса', f'Автобус с номером {new_bus_num_edit} существует',
                                 QMessageBox.Yes)

    def edit_bus_from_list(self):
        current_item = self.ui_new_bus.bus_list.currentItem()
        bus_edit_set = Bus().edit_bus_from_list_logic(current_item.text())
        print(f'EDIT: {bus_edit_set}')
        self.ui_new_bus.new_bus_num_edit.setText(bus_edit_set['new_bus_num'])
        self.ui_new_bus.new_bus_gosnomer_edit.setText(bus_edit_set['new_bus_gosnomer'])
        self.ui_new_bus.new_bus_model_edit.setText(bus_edit_set['new_bus_model'])
        self.ui_new_bus.new_bus_odometr_edit.setText(bus_edit_set['new_bus_odometr'])
        print(f'UI EDIT: {bus_edit_set} \n')

    def save_edited_bus(self):
        current_item = self.ui_new_bus.bus_list.currentItem().text()
        print(f'UI SAVE ITEM: {current_item} \n')
        edited_bus_num_edit = self.ui_new_bus.new_bus_num_edit.text()
        edited_bus_gosnomer_edit = self.ui_new_bus.new_bus_gosnomer_edit.text()
        edited_bus_model_edit = self.ui_new_bus.new_bus_model_edit.text()
        edited_bus_odometr_edit = self.ui_new_bus.new_bus_odometr_edit.text()
        bus_set = {
                'new_bus_num': edited_bus_num_edit,
                'new_bus_gosnomer': edited_bus_gosnomer_edit,
                'new_bus_model': edited_bus_model_edit,
                'new_bus_odometr': edited_bus_odometr_edit
        }
        print(f'UI SAVE EDIT: {bus_set} \n')
        if edited_bus_num_edit != current_item:
            if not Bus().check_uni_item(edited_bus_num_edit):
                Bus().update_edited_bus_logic(bus_set, current_item)
            else:
                QMessageBox.critical(self, 'Добавление автобуса', f'Автобус № {edited_bus_num_edit} существует',
                                     QMessageBox.Yes)
        else:
            Bus().update_edited_bus_logic(bus_set, current_item)
        self.ui_new_bus.bus_list.clear()
        self.load_bus_list()
        self.ui_new_bus.bus_list.sortItems()

    def remove_bus_from_list(self):
        current_item = self.ui_new_bus.bus_list.currentItem()
        if current_item is None:
            return
        question = QMessageBox.question(self, 'Удаление автобуса',
                                        'Вы точно хотите удалить выбранный автобус\n'
                                        f'{current_item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.ui_new_bus.bus_list.takeItem(self.ui_new_bus.bus_list.indexFromItem(current_item).row())
            Bus().remove_bus_from_list_logic(current_item.text())
            print(f'UI DEL: {current_item.text()} \n')
            del current_item

    # ROUTES
    def open_new_route(self):
        global NewRoute
        NewRoute = QtWidgets.QDialog()
        self.ui_new_route.setupUi(NewRoute)
        self.load_route_list()
        NewRoute.show()
        self.ui_new_route.route_save_button.clicked.connect(self.save_new_route)
        self.ui_new_route.route_edit_button.clicked.connect(self.save_edited_route)
        self.ui_new_route.route_delete_button.clicked.connect(self.remove_route_from_list)
        self.ui_new_route.route_list.itemClicked.connect(self.edit_route_from_list)

    def load_route_list(self):
        route_list = Route().get_route_list_logic()
        self.ui_new_route.route_list.addItems(route_list)
        self.ui_new_route.route_list.sortItems()
        self.ui_new_route.route_list.setCurrentRow(0)

    def save_new_route(self):
        new_route_num_edit = self.ui_new_route.new_route_edit.text()
        new_item = QListWidgetItem(new_route_num_edit)
        if not Route().check_uni_item(new_route_num_edit):
            self.ui_new_route.route_list.addItem(new_item)
            print(f'NEW: {new_item.text()}')
            self.ui_new_route.route_list.sortItems()
            self.ui_new_route.route_list.setCurrentItem(new_item)
            route_set = {
                    'new_route_num': new_route_num_edit
            }
            Route().save_new_route_logic(route_set)
            self.ui_new_route.new_route_edit.clear()
        else:
            QMessageBox.critical(self, 'Добавление маршрута', f'Маршрут с номером {new_route_num_edit} существует',
                                 QMessageBox.Yes)

    def edit_route_from_list(self):
        current_item = self.ui_new_route.route_list.currentItem()
        route_edit_set = Route().edit_route_from_list_logic(current_item.text())
        print(f'EDIT: {route_edit_set}')
        self.ui_new_route.new_route_edit.setText(route_edit_set['new_route_num'])
        print(f'UI EDIT: {route_edit_set} \n')

    def save_edited_route(self):
        current_item = self.ui_new_route.route_list.currentItem().text()
        print(f'UI SAVE ITEM: {current_item} \n')
        edited_route_num_edit = self.ui_new_route.new_route_edit.text()
        route_set = {
                'new_route_num': edited_route_num_edit
        }
        print(f'UI SAVE EDIT: {route_set} \n')
        if edited_route_num_edit != current_item:
            if not Route().check_uni_item(edited_route_num_edit):
                Route().update_edited_route_logic(route_set, current_item)
            else:
                QMessageBox.critical(self, 'Добавление маршрута', f'Маршрут № {edited_route_num_edit} существует',
                                     QMessageBox.Yes)
        else:
            Route().update_edited_route_logic(route_set, current_item)
        self.ui_new_route.route_list.clear()
        self.load_route_list()
        self.ui_new_route.route_list.sortItems()

    def remove_route_from_list(self):
        current_item = self.ui_new_route.route_list.currentItem()
        if current_item is None:
            return
        question = QMessageBox.question(self, 'Удаление маршрута',
                                        'Вы точно хотите удалить выбранный маршрут\n'
                                        f'{current_item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.ui_new_route.route_list.takeItem(self.ui_new_route.route_list.indexFromItem(current_item).row())
            Route().remove_route_from_list_logic(current_item.text())
            print(f'UI DEL: {current_item.text()} \n')
            del current_item


def app():
    app = QApplication(sys.argv)
    win = Appl()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app()
