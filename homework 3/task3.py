def my_func(a, b, c):
    r = [a, b, c]
    r.sort(reverse=True)
    return r[0] + r[1]


print(my_func(1, 2, 3))
