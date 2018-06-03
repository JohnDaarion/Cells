import csv

start_from = 0
number_of_examples = 1090

# Set path to folder with B cells data
training_file_b = '../../DATA/letterB/BHuman.csv'

# Set path to folder with M cells data
training_file_m = '../../DATA/letterM/MHuman.csv'


def append_to_file(filename, label, amount):
    data = []

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        for i, row in enumerate(reader):
            data.append([])
            data[len(data) - 1] = row[0].split(';')

    list_1 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_1.append(column[2])

    list_2 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_2.append(column[7])

    list_3 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_3.append(column[10])

    list_4 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_4.append(column[11])

    list_5 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_5.append(column[14])

    list_6 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_6.append(column[15])

    list_7 = []
    for x in range(start_from + 1, start_from + number_of_examples + 1):
        column = data[x]
        list_7.append(column[16])

    with open('../training_data.csv', 'a', newline='') as csvfile:
        fieldnames = ['1', '2', '3', '4', '5', '6', '7', 'L']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for x in range(0, amount):
            writer.writerow({'1': list_1[x], '2': list_2[x], '3': list_3[x], '4': list_4[x],
                             '5': list_5[x], '6': list_6[x], '7': list_7[x], 'L': label})


append_to_file(training_file_b, 1, number_of_examples)
append_to_file(training_file_m, 2, number_of_examples)
