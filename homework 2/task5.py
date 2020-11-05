my_list = [7, 5, 3, 3, 2]
while True:
    new = int(input("Enter rating number: "))
    if new in my_list:
        index = my_list.index(new)
        my_list.insert(index+1, new)
    else:
        my_list.append(new)
        my_list.sort(reverse=True)
    print("Result:", my_list)