from itertools import cycle

a = [1, 2, 3]
count = 0
for i in cycle(a):
    print(i)
    if i == a[-1]:
        count+=1
    if count == 10:
        break