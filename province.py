class Province:

    #abbr = abbreviation

    def __init__(self, name, type, abbr):
        self.name = name
        self.type = type
        self.abbr = abbr
        self.country = 'no_country'

    def get_info(self):
        return (self.name, self.type, self.abbr, self.country)

    def get_name(self):
        return (self.name)

    def set_name(self, name):
        self.name = name

    def get_type(self):
        return (self.type)

    def set_type(self, type):
        self.type = type

    def get_abbr(self):
        return (self.abbr)

    def set_abbr(self, abbr):
        self.abbr = abbr

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def __repr__(self):
        return (self.name + ' ' + self.type + ' ' + self.abbr +
                ' ' + self.country + '\n')
    def __str__(self):
        return (self.name + ' ' + self.type + ' ' + self.abbr +
                ' ' + self.country + '\n')






