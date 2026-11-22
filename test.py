import csv
prices = {} # Initial empty dict

with open('Work/Data/prices.csv', 'rt') as file:
    f = csv.reader(file)
    for line in f:
        # row = line.split(',')
        if len(line) < 2:
            continue
        prices[line[0]] = float(line[1])

print(prices)