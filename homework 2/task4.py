string = input("Input string: ")
a = string.split(' ')
for i in range(len(a)):
    if len(a[i]) > 10:
        print(i,a[i][:10])
    else:
        print(i,a[i])