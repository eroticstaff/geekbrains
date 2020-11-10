summary = 0
start = True
while start:
    string = input("")
    spl = string.split(" ")
    for i in spl:
        if i != "S":
            summary += int(i)
        else:
            start = False
            break
    print(summary)
