from Province import *
    

class Unit:
    
    def __init__(self, country, type, location):
        self.country = country
        self.type = type
        self.location = location

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country
    
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def __repr__(self):
        return (self.country + ' ' + self.type + ' at ' + self.provinces + '\n')
    def __str__(self):
        return (self.country + ' ' + self.type + ' at ' + self.provinces + '\n')







