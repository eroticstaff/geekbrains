def check(array):
    for i in array:
        if array.count(i) == 1:
            yield i


array = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4,
         11]  # какой генератор в задании имелся ввиду? если что ниже второй вариант
new = list(check(array))
print(new)

a = [i for i in array if array.count(i) == 1]
print(a)
