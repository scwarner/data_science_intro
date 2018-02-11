from s5v1 import *

from prettytable import PrettyTable

def my_table():
    x = PrettyTable(['Style', "Average Price"])
    x.add_row(['Print', pretty_average(print_ties)])
    x.add_row(['Striped', pretty_average(striped_ties)])
    x.add_row(['Paisley', pretty_average(paisley_ties)])
    print(x)

def pretty_average(my_number):
    pretty_avg = "${:03.2f}".format(find_average(my_number))
    return pretty_avg

#my_table()

def count_prices_for_brands(data_sample, brand, min_price, max_price):
    count = 0
    for row in data_sample:
        if str(row[0]) == str(brand):
            if min_price < float(row[1]) < max_price:
                count += 1
    return count
