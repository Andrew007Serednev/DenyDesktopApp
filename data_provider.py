#! /usr/bin/python3
# -*- coding: utf-8 -*-


import json
import pathlib


# Data provider get data from JSON files, remove data in json files and set data to json files in local folder
# for interaction with App tasks. App->JSON=set, JSON->App=get


class WaybillData:
    def __init__(self):
        self.directory = pathlib.Path('.\\waybills')

    def get_waybill_list(self):
        pattern = '*.json'
        waybillist = []
        for currentFile in self.directory.glob(pattern):
            waybillist.append(currentFile.stem)
        print(waybillist)
        return waybillist

    def remove_waybill_file(self, name):
        json_file = pathlib.Path.joinpath(self.directory, name).with_suffix('.json')
        json_file.unlink()


class Driver:
    def __init__(self):
        self.driver_admin = pathlib.Path('.\\admin\\drivers.json')

    def get_driver_fio_list_logic(self):
        driver_fio_list = []
        with open(self.driver_admin, 'r') as json_file:
            driver_fio_dict = json.load(json_file)
        for value in driver_fio_dict.values():
            driver_fio_list.append(value.get('new_driver_fio'))
        return driver_fio_list

    def set_new_driver_logic(self, driver_set):
        new_driver = {}
        with open(self.driver_admin, 'r') as json_file:
            data = json.loads(json_file.read())
        if not data:
            max_driver_id = 0
        else:
            max_driver_id = max([int(item) for item in data.keys()])
        max_driver_id += 1
        new_driver[max_driver_id] = driver_set
        data.update(new_driver)
        with open(self.driver_admin, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def remove_driver_from_list_logic(self, driver_fio):
        del_item = None
        with open(self.driver_admin, 'r') as json_file:
            driver_fio_dict = json.load(json_file)
            for pare in driver_fio_dict.items():
                if pare[1]['new_driver_fio'] == driver_fio:
                    del_item = pare[0]
                    break
            del driver_fio_dict[del_item]
        with open(self.driver_admin, 'w') as json_file:
            json.dump(driver_fio_dict, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))


# if __name__ == "__main__":
#     jsonData = WaybillData()
#     waybilllist = jsonData.get_waybill_list()
#     jsonData.remove_waybill_file('12-06 36 5 4-4 705')

