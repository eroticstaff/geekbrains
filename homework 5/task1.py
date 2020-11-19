file = open("file.txt", 'w')
while True:
    string = input("Enter data:")
    if string == "":
        break
    file.write(string)
file.close()