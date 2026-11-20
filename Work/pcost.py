# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    data = []

    with open(filename, "rt") as file:
        rows = csv.reader(file)
        header = next(rows)
        
        for row in rows:
            data.append(row)

    overall_cost_of_shares = 0

    for d in data:
        cost_of_shares = int(d[1])*float(d[2])
        overall_cost_of_shares += cost_of_shares
        
    print(f"Total cost {overall_cost_of_shares}")

if len(sys.argv) == 2:
    filename = sys.argv[1]
# else:
#     filename = "Work/Data/portfolio.csv"
portfolio_cost(filename)