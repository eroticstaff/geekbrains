n = input("Enter n: ")
i = 0
max = 0
while(i != len(n)):
    if int(n[i]) > max:
        max = int(n[i])
    i += 1
print(max)