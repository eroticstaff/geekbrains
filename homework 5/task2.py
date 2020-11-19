with open("task2_text.txt", 'r') as file:
    lines = file.readlines()
    print(f"Count of lines is {len(lines)}")
    n = 1
    for line in lines:
        print(f"Line {n} has {len(line.split(' '))} words")
        n += 1
    