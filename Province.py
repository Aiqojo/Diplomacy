class Province:

    #abbr = abbreviation

    def __init__(self, name, type, abbr):
        self.name = name
        self.type = type
        self.abbr = abbr
        self.country = 'no_country'
        self.army = False
        self.ship = False
        self.can_ship = True
        self.supply = False

        if 'army' in self.type:
            army = True
        if 'ship' in self.type:
            ship = True
        if 'supply' in self.type:
            supply = True

        if 'land' in self.type:
            can_ship = False

        if 'supply' in self.type:
            supply = True

    def get_info(self):
        return (self.name, self.type, self.abbr, self.country)

    def get_unit(self):
        if self.army:
            return "army"
        elif self.ship:
            return "ship"
        else:
            return "none"

    def set_unit(self, unit):
        if not self.army or not self.ship:
            if unit == 'army':
                self.army = True
            elif unit == 'ship':
                self.ship = True


    def set_can_ship(self, bool):
        self.can_ship = bool

    def get_can_ship(self):
        return self.can_ship

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
        return (self.name + ' | ' + self.type + ' | ' +
                self.country + '\n')
    def __str__(self):
        return (self.name + ' | ' + self.type + ' | ' +
                self.country + '\n')






