# Exercise 1.5

def height_of_bounce(height: int, bounce: float):
    for i in range(1, 11):
        height = height * bounce
        print(i, round(height, 4))

height_of_bounce(100, (3/5))