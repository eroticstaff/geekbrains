with open("task3_text.txt", 'r', encoding='utf-8') as file:
    print("Оклад меньше 20000 у данных лиц:")
    mean = 0
    n = 0
    for line in file:
        surname, oklad = line.split(' ')
        if int(oklad) < 20000:
            print(surname)
        mean += int(oklad)
        n += 1
    print(f"Средний доход равен {mean/n}р")
