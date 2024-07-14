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
        self.table_widget.setRowCount(len(Bus().get_bus_list_logic()))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(
            ['Автобус', 'Маршрут', 'График', 'Водитель'])
        self.load_drivers_col()
        self.load_bus_col()

    def load_bus_col(self):
        bus_list = Bus().get_bus_list_logic()
        for row in range(len(bus_list)):
            print(bus_list[row])
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(bus_list[row])))

    def load_drivers_col(self):
        for row in range(self.table_widget.rowCount()):
            drivers_list = DriversList(self)
            self.table_widget.setCellWidget(row, 3, drivers_list)

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
