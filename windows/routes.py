#! /usr/bin/python3
# -*- coding: utf-8 -*-
import itertools
import logging
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QListWidget, QPushButton, QComboBox, QListWidgetItem, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from data_provider import Order, Driver, Bus, Route
from forms.NewRoute import Ui_Dialog


class RoutesDialog(QDialog):
    def __init__(self):
        super(RoutesDialog, self).__init__()
        self.ui_routes = Ui_Dialog()
        self.ui_routes.setupUi(self)

        self.table_routes = self.ui_routes.table_routes
        self.table_routes.setColumnCount(3)
        self.table_routes.setHorizontalHeaderLabels(['Маршрут', 'График', 'Время'])
        self.ui_routes.button_add_route.clicked.connect(self.save_new_route)
        self.ui_routes.button_del_route.clicked.connect(self.remove_route)
        # self.load_route_table()

        self.ui_routes.list_routes.setCurrentRow(0)
        self.ui_routes.list_bus_counts.setCurrentRow(0)
        self.ui_routes.list_routes.itemSelectionChanged.connect(self.create_new_route)
        self.ui_routes.list_bus_counts.itemSelectionChanged.connect(self.create_new_route)

    def create_new_route(self):
        route_num = self.ui_routes.list_routes.currentItem().text()
        graphic_num = self.ui_routes.list_bus_counts.currentItem().text()
        self.table_routes.setRowCount(int(graphic_num))
        print(f'NUM: {graphic_num}, {type(graphic_num)}')
        for i in range(int(graphic_num)):
            item_route_num = QTableWidgetItem(route_num)
            item_graphic = QTableWidgetItem(str(i+1))
            item_time = QTableWidgetItem("07:00")
            self.table_routes.setItem(i, 0, item_route_num)
            self.table_routes.setItem(i, 1, item_graphic)
            self.table_routes.setItem(i, 2, item_time)

    def save_new_route(self):
        route_num = self.ui_routes.list_routes.currentItem().text()
        graphic_count = self.ui_routes.list_bus_counts.currentText()
        routes_set = {
            'route_num': route_num,
            'graphic': {
                'graphic_num': graphic_count,
                'time': {}
            }
        }
        for i in self.table_routes.rowCount():
            item_time = self.table_routes.takeItem(2, i)
            routes_set['graphic']['time'][i] = item_time

        print(f'SET: \n{routes_set}')
        # Route().save_new_route_logic(routes_set)
        # # self.load_route_table()

    def load_route_table(self):
        routes_dict = Route().get_route_dict_logic()
        self.table_routes.setRowCount(len(routes_dict))
        for i, (key, row) in enumerate(routes_dict):
            item_route_num = QTableWidgetItem(str(row['route_num']))
            item_route_num.setData(Qt.UserRole, key)
            item_graphic_num = QTableWidgetItem(str(row['graphic_num']))
            item_time_line = QTableWidgetItem(str(row['time_line']))
            self.table_routes.setItem(i, 0, item_route_num)
            self.table_routes.setItem(i, 1, item_graphic_num)
            self.table_routes.setItem(i, 2, item_time_line)

    def remove_route(self):
        current_row = self.table_routes.currentRow()
        if current_row is None:
            return
        question = QMessageBox.question(self, 'Удаление маршрута',
                                        'Вы точно хотите удалить выбранный маршрут?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            key = self.table_routes.item(current_row, 1).data(Qt.UserRole)
            print(key)
            self.table_routes.removeRow(current_row)
            Route().remove_route_from_list_logic(key)
