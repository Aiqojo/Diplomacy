class province:

    #abbr = abbreviation

    def __init__(self, name, type, abbr):
        self.name = name
        self.type = type
        self.abbr = abbr

    def get_info(self):
        print(self.name, self.type, self.abbr)

    def get_name(self):
        print(self.name)

    def set_name(self, name):
        self.name = name

    def get_type(self):
        print(type)

    def set_type(self, type):
        self.type = type

    def get_abbr(self):
        print(self.abbr)

    def set_abbr(self, abbr):
        self.abbr = abbr

    def __repr__(self):
        return (self.name + ' ' + self.type + ' ' + self.abbr)
    def __str__(self):
        return (self.name + ' ' + self.type + ' ' + self.abbr)






