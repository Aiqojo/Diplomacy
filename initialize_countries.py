import ast
from Province import *
from Country import *

country_name_list = ['aus','eng','fra','ger','ita','rus','tur']

country_list = []

def main(provinces):
    for country_name in country_name_list:
        # Appending a new country object for each object in country_name_list
        country_list.append(Country(country_name, []))

    # Checking the province type for the country name 
    # and adding home supply provinces to their repsective country
    # Ex. Ankara's type is "coast_home_supply_tur" so it gets added to "tur" country object, or Turkey
    for province in provinces:
        for country in country_list:
            if country.get_name() in province.get_type():
                country.add_province(province)

    return country_list


if __name__ == "__main__":
    main()
