def division(a, b):
    if b == 0:
        print("Error: Division by zero")
        return None
    return a / b


a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(division(a,b))