from province import *

class Country:

    def __init__(self, name, provinces):
        self.name = name
        self.provinces = provinces

    def get_provinces(self):
        return (''.join(str(province) for province in self.provinces))

    def add_province(self, province):
        self.provinces.append(province)

    def remove_province(self, province):
        self.provinces.remove(province)

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name



