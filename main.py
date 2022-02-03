import initialize_provinces
import initialize_countries
import Province

def main():

    # Creating list of province objects from "province_list.csv"
    provinces = initialize_provinces.main()

    # Creating list of country objects
    countries = initialize_countries.main(provinces)

    













if __name__ == "__main__":
    main()
