import yaml
from SSID import SSID
class WRYamel:
    @staticmethod
    def yaml_loader(filepath):
        file = open(filepath,"r")
        data = yaml.load_all(file)
        return data

    @staticmethod
    def yaml_dump(filepath,data):
        with open(filepath,"a+") as file:
            yaml.dump(data,file)
            file.close()


