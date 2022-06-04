# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import csv

ii = 0

with open('file.txt', 'r', encoding='utf8', newline='') as f_input, \
     open(str(ii + 1) + 'output.csv', 'w', encoding='utf8', newline='') as f_output:

    input_lines = filter(lambda x: len(x) > 2 and x[0] == '|', f_input)

    csv_input = csv.reader(input_lines, delimiter='|')
    csv_output = csv.writer(f_output)

    for row in csv_input:
        csv_output.writerow(col.strip() for col in row[1:-1])