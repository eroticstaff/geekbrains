def my_func(x, y):
    t = 1
    for i in range(abs(y)):
        t *= 1 / x
    return t


print(my_func(3, -7))
