import csv
from pprint import pprint
from typing import Any

filename = 'Work/Data/portfolio.csv'

# Exercise 2.4
def read_portfolio_tuple(filename) -> list[tuple[str, int, float]]:
    portfolio_ls = []

    with open(filename, 'rt') as file:
        headers = next(file)

        for line in csv.reader(file):
            if len(line) != 3:
                continue
            portfolio_temp = (line[0], int(line[1]), float(line[2]))
            portfolio_ls.append(portfolio_temp)

    return portfolio_ls


# Exercise 2.5
def read_portfolio_dict(filename) -> list[dict[str, Any]]:
    portfolio_ls = []

    with open(filename, 'rt') as file:
        headers = next(file).strip('\n').split(',')
    
        for line in csv.reader(file):
            if len(line) != 3:
                continue

            portfolio_dict: dict[str, Any] = {}
            portfolio_dict[headers[0]] = line[0]
            portfolio_dict[headers[1]] = int(line[1])
            portfolio_dict[headers[2]] = float(line[2])
            portfolio_ls.append(portfolio_dict)

    return portfolio_ls


# Exercise 2.6
def read_prices(filename) -> dict:
    prices = {}
    with open(filename, 'rt') as file:
        for row in csv.reader(file):
            if len(row) != 2:
                continue
            prices[row[0]] = float(row[1])

    return prices



portfolio = read_portfolio_dict(filename)
cost = sum([ p['shares'] * p['price'] for p in portfolio ])

port_tuple = [ p for p in portfolio ]
pprint(port_tuple)