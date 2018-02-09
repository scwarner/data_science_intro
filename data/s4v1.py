from s3v3 import *

import csv

def write_to_file(filename, data_sample):
    example = csv.writer(open(filename, 'w', encoding='utf-8'), dialect='excel')
    example.writerows(data_sample)

write_to_file("_files/s4_silk_ties.csv", silk_ties)
