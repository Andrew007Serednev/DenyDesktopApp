#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QListWidget, QPushButton, QComboBox
from PyQt5.QtCore import *
from data_provider import Order, Driver, Bus, Route
from forms.NewDriver import Ui_Dialog


class DriverDialog(QDialog):
    def __init__(self):
        super(DriverDialog, self).__init__()
        self.ui_driver = Ui_Dialog()
        self.ui_driver.setupUi(self)


