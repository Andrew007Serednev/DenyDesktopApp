#! /usr/bin/python3
# -*- coding: utf-8 -*-


import json
import pathlib


# Data provider get data from JSON files, remove data in json files and set data to json files in local folder
# for interaction with App tasks. App->JSON=set, JSON->App=get


class OrderData:
    def __init__(self):
        self.directory = pathlib.Path('data/orders')

    def get_order_list(self):
        pattern = '*.json'
        orderist = []
        for currentFile in self.directory.glob(pattern):
            orderist.append(currentFile.stem)
        print(orderist)
        return orderist

    def remove_order_file(self, name):
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

    def save_new_driver_logic(self, driver_set):
        new_driver = {}
        with open(self.driver_admin, 'r') as json_file:
            data = json.loads(json_file.read())
        if len(data.keys()) == 0:
            max_driver_id = 0
        else:
            max_driver_id = max([int(item) for item in data.keys()])
            max_driver_id += 1
        new_driver[max_driver_id] = driver_set
        data.update(new_driver)
        with open(self.driver_admin, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def update_edited_driver_logic(self, driver_set, current_item):
        print(f'BACK SAVE ITEM: {current_item} \n')
        with open(self.driver_admin, 'r') as json_file:
            data = json.loads(json_file.read())
        for pare in data.items():
            if pare[1]['new_driver_fio'] == current_item:
                pare[1].update(driver_set)
        print(f"Back UPDATE: {driver_set}")
        with open(self.driver_admin, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def edit_driver_from_list_logic(self, current_item):
        edit_item = None
        with open(self.driver_admin, 'r') as json_file:
            driver_fio_dict = json.load(json_file)
        for pare in driver_fio_dict.items():
            if pare[1]['new_driver_fio'] == current_item:
                edit_item = pare[0]
                print(f"Back EDIT: {pare[1]}")
                break
        return driver_fio_dict[edit_item]

    def remove_driver_from_list_logic(self, current_item):
        del_item = None
        with open(self.driver_admin, 'r') as json_file:
            driver_fio_dict = json.load(json_file)
            for pare in driver_fio_dict.items():
                if pare[1]['new_driver_fio'] == current_item:
                    del_item = pare[0]
                    break
            del driver_fio_dict[del_item]

        with open(self.driver_admin, 'w') as json_file:
            json.dump(driver_fio_dict, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def check_uni_item(self, item_text):
        uni_flag = False
        with open(self.driver_admin, 'r') as json_file:
            driver_fio_dict = json.load(json_file)
            for pare in driver_fio_dict.items():
                if pare[1]['new_driver_fio'] == item_text:
                    uni_flag = True
                    break
        return uni_flag


class Bus:
    def __init__(self):
        self.bus_admin = pathlib.Path('.\\admin\\bus.json')

    def get_bus_list_logic(self):
        bus_list = []
        with open(self.bus_admin, 'r') as json_file:
            bus_dict = json.load(json_file)
        for value in bus_dict.values():
            bus_list.append(value.get('new_bus_num'))
        return bus_list

    def save_new_bus_logic(self, bus_set):
        new_bus = {}
        with open(self.bus_admin, 'r') as json_file:
            data = json.loads(json_file.read())
        if len(data.keys()) == 0:
            max_bus_id = 0
        else:
            max_bus_id = max([int(item) for item in data.keys()])
            max_bus_id += 1
        new_bus[max_bus_id] = bus_set
        data.update(new_bus)
        with open(self.bus_admin, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def update_edited_bus_logic(self, bus_set, current_item):
        print(f'BACK SAVE ITEM: {current_item} \n')
        with open(self.bus_admin, 'r') as json_file:
            data = json.loads(json_file.read())
        for pare in data.items():
            if pare[1]['new_bus_num'] == current_item:
                pare[1].update(bus_set)
        print(f"Back UPDATE: {bus_set}")
        with open(self.bus_admin, 'w', encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def edit_bus_from_list_logic(self, current_item):
        edit_item = None
        with open(self.bus_admin, 'r') as json_file:
            bus_num_dict = json.load(json_file)
        for pare in bus_num_dict.items():
            if pare[1]['new_bus_num'] == current_item:
                edit_item = pare[0]
                print(f"Back EDIT: {pare[1]}")
                break
        return bus_num_dict[edit_item]

    def remove_bus_from_list_logic(self, current_item):
        del_item = None
        with open(self.bus_admin, 'r') as json_file:
            bus_num_dict = json.load(json_file)
            for pare in bus_num_dict.items():
                if pare[1]['new_bus_num'] == current_item:
                    del_item = pare[0]
                    break
            del bus_num_dict[del_item]

        with open(self.bus_admin, 'w') as json_file:
            json.dump(bus_num_dict, json_file, ensure_ascii=False, indent=4, separators=(',', ':'))

    def check_uni_item(self, item_text):
        uni_flag = False
        with open(self.bus_admin, 'r') as json_file:
            bus_num_dict = json.load(json_file)
            for pare in bus_num_dict.items():
                if pare[1]['new_bus_num'] == item_text:
                    uni_flag = True
                    break
        return uni_flag


# if __name__ == "__main__":
#     jsonData = orderData()
#     orderlist = jsonData.get_order_list()
#     jsonData.remove_order_file('12-06 36 5 4-4 705')

