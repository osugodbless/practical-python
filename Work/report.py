# Exercise 2.4
import csv

def read_portfolio(filename) -> list[tuple[str, int, float]]:
    portfolio_ls = []

    with open(filename, 'rt') as file:
        headers = next(file)

        for line in csv.reader(file):
            if len(line) != 3:
                continue
            portfolio_temp = (line[0], int(line[1]), float(line[2]))
            portfolio_ls.append(portfolio_temp)

    return portfolio_ls

filename = 'Work/Data/portfolio.csv'
print(read_portfolio(filename))
