from random import randint

with open("task5_text.txt", 'w', encoding='utf-8') as file:
    numbers = [str(randint(0, 100)) for i in range(20)]
    file.write(" ".join(numbers))
with open("task5_text.txt", 'r', encoding='utf-8') as file:
    sum = sum([int(i) for i in file.read().split(" ")])
    print(sum)
