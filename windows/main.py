#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QListWidget, QPushButton, QComboBox
from PyQt5.QtCore import *
from data_provider import Order, Driver, Bus, Route
from forms.OrderWindow import Ui_MainWindow
from windows.drivers import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)

        self.main_window.action_driver.triggered.connect(self.open_new_driver)

        self.table_widget = self.main_window.tableWidget
        self.table_widget.setRowCount(7)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(
            ['Водитель', 'Автобус', 'Маршрут'])
        self.load_drivers_col()
        self.load_bus_col()

    def load_drivers_col(self):
        for row in range(self.table_widget.rowCount()):
            drivers_list = DriversList(self)
            self.table_widget.setCellWidget(row, 0, drivers_list)

    def load_bus_col(self):
        for row in range(self.table_widget.rowCount()):
            bus_list = BusList(self)
            self.table_widget.setCellWidget(row, 1, bus_list)

    def open_new_driver(self):
        driver_dialog = DriverDialog()
        driver_dialog.exec_()


class BusList(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 14px')
        bus_list = Bus().get_bus_list_logic()
        self.addItems(bus_list)
        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())
        return self.currentText()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
