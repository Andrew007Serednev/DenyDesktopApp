#! /usr/bin/python3
# -*- coding: utf-8 -*-
import itertools
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
        self.table_routes.setColumnCount(4)
        self.table_routes.setHorizontalHeaderLabels(['День', 'Маршрут', 'График', 'Время'])
        self.ui_routes.button_add_route.clicked.connect(self.save_new_route)
        self.ui_routes.button_del_route.clicked.connect(self.remove_route)

        self.load_route_table()

    def save_new_route(self):
        day_type = self.ui_routes.list_days.currentItem().text()
        route_num = self.ui_routes.list_routes.currentItem().text()
        graphic_num = self.ui_routes.list_graphics.currentItem().text()
        time_line = self.ui_routes.time_line.time().toString('HH:mm')
        routes_set = {
            'day_type': day_type,
            'route_num': route_num,
            'graphic_num': graphic_num,
            'time_line': time_line
        }
        Route().save_new_route_logic(routes_set)
        self.load_route_table()

    def load_route_table(self):
        routes_dict = Route().get_route_dict_logic()
        self.table_routes.setRowCount(len(routes_dict))
        for i, (key, row) in enumerate(routes_dict):
            item_day_type = QTableWidgetItem(str(row["day_type"]))
            item_route_num = QTableWidgetItem(str(row['route_num']))
            item_route_num.setData(Qt.UserRole, key)
            item_graphic_num = QTableWidgetItem(str(row['graphic_num']))
            item_time_line = QTableWidgetItem(str(row['time_line']))
            self.table_routes.setItem(i, 0, item_day_type)
            self.table_routes.setItem(i, 1, item_route_num)
            self.table_routes.setItem(i, 2, item_graphic_num)
            self.table_routes.setItem(i, 3, item_time_line)

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
