#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QListWidget, QPushButton, QComboBox
from PyQt5.QtCore import *
from data_provider import Order, Driver, Bus, Route
from forms.OrderWindow import Ui_MainWindow
from windows.drivers import *
from windows.bus import *
from windows.routes import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        self.main_window.action_driver.triggered.connect(self.open_new_driver)
        self.main_window.action_bus.triggered.connect(self.open_new_bus)
        self.main_window.action_route.triggered.connect(self.open_new_route)

        self.table_widget = self.main_window.tableWidget
        self.table_widget.setRowCount(len(Bus().get_bus_list_logic()))
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(
            ['Автобус', 'Маршрут', 'График', 'Водитель', ''])
        self.load_drivers_col()
        self.load_bus_col()
        self.bill_open_unit_coll()
        # self.table_widget.resizeColumnsToContents()

    def load_bus_col(self):
        bus_list = Bus().get_bus_list_logic()
        for row in range(len(bus_list)):
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(bus_list[row])))

    def load_drivers_col(self):
        max_width = 0
        for row in range(self.table_widget.rowCount()):
            drivers_list = DriversList(self)
            self.table_widget.setCellWidget(row, 3, drivers_list)
            width = drivers_list.width()
            max_width = max(max_width, width)
        self.table_widget.setColumnWidth(3, max_width + 20)

    def bill_open_unit_coll(self):
        max_width = 0
        for row in range(self.table_widget.rowCount()):
            bill_open_button = QPushButton("Открыть путевой лист")
            bill_open_button.clicked.connect(lambda checked, row=row: self.bill_open_unit(row))
            self.table_widget.setCellWidget(row, 4, bill_open_button)
            width = bill_open_button.width()
            max_width = max(max_width, width)
        self.table_widget.setColumnWidth(4, max_width+20)

    def open_new_driver(self):
        driver_dialog = DriverDialog()
        driver_dialog.exec_()

    def open_new_bus(self):
        bus_dialog = BusDialog()
        bus_dialog.exec_()

    def open_new_route(self):
        route_dialog = RoutesDialog()
        route_dialog.exec_()

    def bill_open_unit(self, row):
        print(f'Открыли {row}')


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
