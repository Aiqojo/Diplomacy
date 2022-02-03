from province import *
from country import *

province_list = []

def main():

    return initialize("province_list.csv")


def initialize(file):
    with open(file) as f:
        for line in f:
            arr = []
            arr.append(line.strip().split(","))
            #print(arr)

            province_list.append(province(arr[0][0], arr[0][1], arr[0][2]))

            arr.clear()

    

    return province_list


if __name__ == "__main__":
    main()

