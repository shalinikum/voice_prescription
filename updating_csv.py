import csv
import os

def edit_credentials(dict_data):
	csv_file = "Names.csv"
	with open('Names.csv', 'w', newline="") as csv_file:  
	    writer = csv.writer(csv_file)
	    for key, value in dict_data.items():
	       writer.writerow([key, value])

	os.system('vim Names.csv')

	with open('Names.csv') as csv_file:
	    reader = csv.reader(csv_file)
	    dict_data = dict(reader)

	return dict_data

	dict1 = {'a':'b','c':'d'}
	a = edit_credentials(dict1)
	print(a)

