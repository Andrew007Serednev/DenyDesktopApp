import json
import pathlib


class WaybillData:
    def __init__(self):
        self.directory = pathlib.Path('.\waybills')

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


# if __name__ == "__main__":
#     jsonData = WaybillData()
#     waybilllist = jsonData.get_waybill_list()
#     jsonData.remove_waybill_file('12-06 36 5 4-4 705')
