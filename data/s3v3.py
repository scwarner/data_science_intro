from s3v2 import *

gucci_ties = filter_col_by_string(data_from_csv, "brandName", "Gucci")
jcrew_ties = filter_col_by_string(data_from_csv, "brandName", "J.Crew")

max_gucci = find_max(gucci_ties[1:], 2)
max_jcrew = find_max(jcrew_ties[1:], 2)

message = "{} {} tie price is = ${:03.2f}"
#print(message.format("Maximum", "Gucci", max_gucci))
#print(message.format("Maximum", "J.Crew", max_jcrew))

avg_gucci = find_average(gucci_ties, True)
avg_jcrew = find_average(jcrew_ties, True)

#print(message.format("Average", "Gucci", avg_gucci))
#print(message.format("Average", "J.Crew", avg_jcrew))

striped_ties = filter_col_by_string(data_from_csv, "print", "_striped")
print_ties = filter_col_by_string(data_from_csv, "print", "_print")
paisley_ties = filter_col_by_string(data_from_csv, "print", "_paisley")

#print("Found {} striped ties".format(number_of_records(striped_ties)))
#print("Found {} print ties".format(number_of_records(print_ties)))
#print("Found {} paisley ties".format(number_of_records(paisley_ties)))

print(message.format("Average", "paisley", find_average(paisley_ties, True)))
print(message.format("Average", "striped", find_average(striped_ties, True)))