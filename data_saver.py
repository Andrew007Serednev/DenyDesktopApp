# -*- coding: utf-8 -*-


import json
import psycopg2
from pathlib import Path


# Data saver facilitates interaction between JSON files in local folder and database. DB->JSON=get, JSON->DB=send

class Drivers:
    def __init__(self):
        self.data_file = Path('.\\admin\\drivers.json')
        self.data_dict = dict()


    def get_driver_fio_list(self):
        driver_fio_list = ['Середнев Андрей Андреевич', 'Середнев Тимофей Андреевич',
                           'Шаломов Владислав Александрович', 'Шаломов Виктор Александрович',
                           'Данилов Данила Данилович']  # DB getter mock

        driver_fio_dict = {}
        for driver_fio in driver_fio_list:
            driver_fio_dict[driver_fio_list.index(driver_fio)] = driver_fio
        self.data_dict['driver_fio_dict'] = driver_fio_dict
        with open(self.data_file, 'w') as json_file:
            json.dump(self.data_dict, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def send_new_driver_fio(self):
        pass


d = Drivers()
d.get_driver_fio_list()
