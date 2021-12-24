import math


def check_sides(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


def count_square(a, b, c):
    p = (a + b + c) / 2
    square = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return square


def find_max_combination(d):
    combinations = []
    for x in d:
        for y in d:
            for z in d:
                if check_sides(x, y, z):
                    square = count_square(x, y, z)
                    combinations.append(square)
    max_square = max(combinations)
    return max_square


data = [i for i in range(1, 1000001)]
print(find_max_combination(data))
