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

    def get_driver_fio_list(self):
        driver_fio_list = []
        with open(self.driver_admin, 'r') as json_file:
            driver_fio_dict = json.load(json_file)
        # driver_fio_list = driver_fio_dict.get('driver_fio_dict').values()
        for key, value in (driver_fio_dict.get('driver_fio_dict')).items():
            driver_fio_list.append(value)
        return driver_fio_list

    def set_new_driver(self):
        pass

# if __name__ == "__main__":
#     jsonData = WaybillData()
#     waybilllist = jsonData.get_waybill_list()
#     jsonData.remove_waybill_file('12-06 36 5 4-4 705')

