from functools import reduce

def mult(a,b):
    return a * b

a = [i for i in range(100, 1001) if i % 2 == 0]
b = reduce(mult, a)
print(b)