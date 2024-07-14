#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, \
    QListWidget, QPushButton, QComboBox, QListWidgetItem, QMessageBox
from PyQt5.QtCore import *
from data_provider import Order, Driver, Bus, Route
from forms.NewDriver import Ui_Dialog


class DriverDialog(QDialog):
    def __init__(self):
        super(DriverDialog, self).__init__()
        self.ui_driver = Ui_Dialog()
        self.ui_driver.setupUi(self)
        self.load_drivers_list()

        self.ui_driver.driver_save_button.clicked.connect(self.save_new_driver)
        self.ui_driver.driver_edit_button.clicked.connect(self.save_edited_driver)
        self.ui_driver.driver_delete_button.clicked.connect(self.remove_driver_from_list)
        self.ui_driver.drivers_list.itemClicked.connect(self.edit_driver_from_list)

    def load_drivers_list(self):
        drivers_list = Driver().get_driver_fio_list_logic()
        self.ui_driver.drivers_list.addItems(drivers_list)
        self.ui_driver.drivers_list.sortItems()
        self.ui_driver.drivers_list.setCurrentRow(0)

    def save_new_driver(self):
        new_driver_fio_edit = self.ui_driver.new_driver_fio_edit.text()
        new_driver_snils_edit = self.ui_driver.new_driver_snils_edit.text()
        new_driver_license_edit = self.ui_driver.new_driver_license_edit.text()
        new_driver_start_date = self.ui_driver.new_driver_start_date.date().getDate()
        new_driver_end_date = self.ui_driver.new_driver_end_date.date().getDate()
        new_item = QListWidgetItem(new_driver_fio_edit)
        print(f'{new_driver_fio_edit}, {new_driver_snils_edit}, {new_driver_license_edit},'
              f'{new_driver_start_date}, {new_driver_end_date}')
        if not Driver().check_uni_item(new_driver_fio_edit):
            self.ui_driver.drivers_list.addItem(new_item)
            print(f'NEW: {new_item.text()}')
            self.ui_driver.drivers_list.sortItems()
            # driver_index = self.ui_new_driver.drivers_list.indexFromItem(new_item).row()
            self.ui_driver.drivers_list.setCurrentItem(new_item)
            driver_set = {
                    # 'new_driver_id': driver_index,
                    'new_driver_fio': new_driver_fio_edit,
                    'new_driver_snils': new_driver_snils_edit,
                    'new_driver_license': new_driver_license_edit,
                    'new_driver_start_date': new_driver_start_date,
                    'new_driver_end_date': new_driver_end_date
            }
            Driver().save_new_driver_logic(driver_set)
            self.ui_driver.new_driver_fio_edit.clear()
            self.ui_driver.new_driver_snils_edit.clear()
            self.ui_driver.new_driver_license_edit.clear()
            self.ui_driver.new_driver_start_date.date().currentDate()
            self.ui_driver.new_driver_end_date.date().currentDate()
        else:
            QMessageBox.critical(self, 'Добавление водителя', f'Водитель {new_driver_fio_edit} существует',
                                 QMessageBox.Yes)

    def edit_driver_from_list(self):
        current_item = self.ui_driver.drivers_list.currentItem()
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        driver_edit_set = Driver().edit_driver_from_list_logic(current_item.text())
        print(f'EDIT: {driver_edit_set}')
        self.ui_driver.new_driver_fio_edit.setText(driver_edit_set['new_driver_fio'])
        self.ui_driver.new_driver_snils_edit.setText(driver_edit_set['new_driver_snils'])
        self.ui_driver.new_driver_license_edit.setText(driver_edit_set['new_driver_license'])
        self.ui_driver.new_driver_start_date.setDate(QDate(
            driver_edit_set['new_driver_start_date'][0],
            driver_edit_set['new_driver_start_date'][1],
            driver_edit_set['new_driver_start_date'][2]))
        self.ui_driver.new_driver_end_date.setDate(QDate(
            driver_edit_set['new_driver_end_date'][0],
            driver_edit_set['new_driver_end_date'][1],
            driver_edit_set['new_driver_end_date'][2]))
        print(f'UI EDIT: {driver_edit_set} \n')

    def save_edited_driver(self):
        current_item = self.ui_driver.drivers_list.currentItem().text()  # Антон
        print(f'UI SAVE ITEM: {current_item} \n')
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        edited_driver_fio_edit = self.ui_driver.new_driver_fio_edit.text()
        edited_driver_snils_edit = self.ui_driver.new_driver_snils_edit.text()
        edited_driver_license_edit = self.ui_driver.new_driver_license_edit.text()
        edited_driver_start_date = self.ui_driver.new_driver_start_date.date().getDate()
        edited_driver_end_date = self.ui_driver.new_driver_end_date.date().getDate()
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
        self.ui_driver.drivers_list.clear()
        self.load_drivers_list()
        self.ui_driver.drivers_list.sortItems()

    def remove_driver_from_list(self):
        current_item = self.ui_driver.drivers_list.currentItem()
        # current_index = self.ui_new_driver.drivers_list.indexFromItem(current_item).row()
        if current_item is None:
            return
        question = QMessageBox.question(self, 'Удаление водителя',
                                        'Вы точно хотите удалить выбранного водителя\n'
                                        f'{current_item.text()} ?',
                                        QMessageBox.Yes | QMessageBox.No)
        if question == QMessageBox.Yes:
            self.ui_driver.drivers_list.takeItem(self.ui_driver.drivers_list.indexFromItem(current_item).row())
            Driver().remove_driver_from_list_logic(current_item.text())
            print(f'UI DEL: {current_item.text()} \n')
            del current_item


class DriversList(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.setStyleSheet('font-size: 14px')
        driver_list = Driver().get_driver_fio_list_logic()
        self.addItems(driver_list)
        self.currentIndexChanged.connect(self.getComboValue)

    def getComboValue(self):
        print(self.currentText())
        return self.currentText()