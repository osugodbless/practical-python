# Exercise 1.27
data = []

with open("Work/Data/portfolio.csv", "rt") as file:
    header = next(file).strip("\n").split(",")
    
    for line in file:
       row = line.strip("\n").split(",")
       data.append(row)

overall_cost_of_shares = 0

for d in data:
    cost_of_shares = int(d[1])*float(d[2])
    overall_cost_of_shares += cost_of_shares
    
print(f"Total cost {overall_cost_of_shares}")