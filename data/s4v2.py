from s4v1 import *

def write_brand_price_file(filename, data_sample):
    brand_index = 5
    price_index = 2

    new_array = []
    for record in data_sample:
        new_record = [None] * 2
        new_record[0] = record[brand_index]
        new_record[1] = record[price_index]
        new_array.append(new_record)

    write_to_file(filename, new_array)

#write_brand_price_file('_files/s4_brand_price.csv', gucci_ties)

def write_max_min(filename, data_sample):
    min = find_max_min(data_sample, 2, "min")
    max = find_max_min(data_sample, 2, "max")

    new_array = []
    for record in data_sample:
        if (float(record[2]) == min) or (float(record[2]) == max):
            new_array.append(record)

    write_to_file(filename, new_array)

#write_max_min('_files/s4_max_min.csv', gucci_ties[1:])

def write_two_cols(filename, data_sample, col1, col2):
    new_array = []
    for record in data_sample:
        new_record = [None] * 2
        new_record[0] = record[col1]
        new_record[1] = record[col2]
        new_array.append(new_record)

    write_to_file(filename, new_array)

#write_two_cols('_files/s4_write_two.csv', gucci_ties[1:], 3, 7)

