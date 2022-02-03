from Province import *
from Country import *

province_list = []

def main():

    return initialize_provinces("province_list.csv")


def initialize_provinces(file):
    with open(file) as f:
        for line in f:
            arr = []
            arr.append(line.strip().split(","))
            #print(arr)

            province_list.append(Province(arr[0][0], arr[0][1], arr[0][2]))

            arr.clear()

    #print(province_list)

    

    return province_list


if __name__ == "__main__":
    main()

