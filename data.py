import json
import pathlib


class JsonData:

    def get_waybill_list(self):
        directory = pathlib.Path('.\waybills')
        pattern = '*.json'
        waybillist = []
        for currentFile in directory.glob(pattern):
            waybillist.append(currentFile.stem)
        print(waybillist)
        return waybillist

# if __name__ == "__main__":
#     jsonData = JsonData()
#     waybilllist = jsonData.get_waybill_list()
