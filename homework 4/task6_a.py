from itertools import count

begin = int(input("First num: "))

for i in count(begin):
    if i == 100:
        break
    print(i)