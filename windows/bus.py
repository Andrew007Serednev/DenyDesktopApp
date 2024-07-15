#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QListWidget, QPushButton, QComboBox, QListWidgetItem, QMessageBox
from PyQt5.QtCore import *
from data_provider import Order, Driver, Bus, Route
from forms.NewBus import Ui_Dialog


class BusDialog(QDialog):
    def __init__(self):
        super(BusDialog, self).__init__()
        self.ui_bus = Ui_Dialog()
        self.ui_bus.setupUi(self)
        self.load_bus_list()

        self.ui_bus.bus_save_button.clicked.connect(self.save_new_bus)
        self.ui_bus.bus_edit_button.clicked.connect(self.save_edited_bus)
        self.ui_bus.bus_delete_button.clicked.connect(self.remove_bus_from_list)
        self.ui_bus.bus_list.itemClicked.connect(self.edit_bus_from_list)

    def load_bus_list(self):
        bus_list = Bus().get_bus_list_logic()
        self.ui_bus.bus_list.addItems(bus_list)
        self.ui_bus.bus_list.sortItems()
        self.ui_bus.bus_list.setCurrentRow(0)

    def save_new_bus(self):
        new_bus_num_edit = self.ui_bus.new_bus_num_edit.text()
        new_bus_gosnomer_edit = self.ui_bus.new_bus_gosnomer_edit.text()
        new_bus_model_edit = self.ui_bus.new_bus_model_edit.text()
        new_bus_odometr_edit = self.ui_bus.new_bus_odometr_edit.text()
        new_item = QListWidgetItem(new_bus_num_edit)
        if not Bus().check_uni_item(new_bus_num_edit):
            self.ui_bus.bus_list.addItem(new_item)
            print(f'NEW: {new_item.text()}')
            self.ui_bus.bus_list.sortItems()
            self.ui_bus.bus_list.setCurrentItem(new_item)
            bus_set = {
                    'new_bus_num': new_bus_num_edit,
                    'new_bus_gosnomer': new_bus_gosnomer_edit,
                    'new_bus_model': new_bus_model_edit,
                    'new_bus_odometr': new_bus_odometr_edit
            }
            Bus().save_new_bus_logic(bus_set)
            self.ui_bus.new_bus_num_edit.clear()
            self.ui_bus.new_bus_gosnomer_edit.clear()
            self.ui_bus.new_bus_model_edit.clear()
            self.ui_bus.new_bus_odometr_edit.clear()
        else:
            QMessageBox.critical(self, 'Добавление автобуса', f'Автобус с номером {new_bus_num_edit} существует',
                                 QMessageBox.Yes)

    def edit_bus_from_list(self):
        current_item = self.ui_bus.bus_list.currentItem()
        bus_edit_set = Bus().edit_bus_from_list_logic(current_item.text())
        print(f'EDIT: {bus_edit_set}')
        self.ui_bus.new_bus_num_edit.setText(bus_edit_set['new_bus_num'])
        self.ui_bus.new_bus_gosnomer_edit.setText(bus_edit_set['new_bus_gosnomer'])
        self.ui_bus.new_bus_model_edit.setText(bus_edit_set['new_bus_model'])
        self.ui_bus.new_bus_odometr_edit.setText(bus_edit_set['new_bus_odometr'])
        print(f'UI EDIT: {bus_edit_set} \n')

    def save_edited_bus(self):
        current_item = self.ui_bus.bus_list.currentItem().text()
        print(f'UI SAVE ITEM: {current_item} \n')
        edited_bus_num_edit = self.ui_bus.new_bus_num_edit.text()
        edited_bus_gosnomer_edit = self.ui_bus.new_bus_gosnomer_edit.text()
        edited_bus_model_edit = self.ui_bus.new_bus_model_edit.text()
        edited_bus_odometr_edit = self.ui_bus.new_bus_odometr_edit.text()
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
        self.ui_bus.bus_list.clear()
        self.load_bus_list()
        self.ui_bus.bus_list.sortItems()

    def remove_bus_from_list(self):
        current_item = self.ui_bus.bus_list.currentItem()
        if current_item is None:
            return
        question = QMessageBox.question(self, 'Удаление автобуса',
                                        'Вы точно хотите удалить выбранный автобус\n'
                                        f'{current_item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.ui_bus.bus_list.takeItem(self.ui_bus.bus_list.indexFromItem(current_item).row())
            Bus().remove_bus_from_list_logic(current_item.text())
            print(f'UI DEL: {current_item.text()} \n')
            del current_item


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
