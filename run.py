from extract.extract import FileParser
from transform.src1 import Src1
from transform.src2 import Src2
from restaurant.restuarant import Restaurant


def main():

    file_parser = FileParser()
    file_parser.get_files_names()

    for filename in file_parser.full_paths:
        restaurant_data = file_parser.read_data(filename)
        if restaurant_data is None:
            continue
        if "src1" in filename:
            src1 = Src1(restaurant_data)
            restaurant = Restaurant(src1.process())
        if "src2" in filename:
            src2 = Src2(restaurant_data)
            restaurant = Restaurant(src2.process())

        restaurant.get_open_restaurants()


if __name__ == '__main__':
    main()
