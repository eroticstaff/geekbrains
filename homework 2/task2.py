n = int(input("Count of elements: "))
a = []
for i in range(n):
    a.append(input())

for i in range(1, n, 2):
    a[i-1], a[i] = a[i], a[i-1]
print(a)