def int_func(string):
    return string.capitalize()


string = input("")
result = " ".join(int_func(s) for s in string.split(" "))
print(result)
