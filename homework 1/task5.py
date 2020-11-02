v = int(input("Выручка: "))
i = int(input("Издержки: "))
if v > i:
    print("Фирма работает в прибыль")
    rent = (v - i) / v
    print("Рентабельность =", rent)
    count = int(input("Количество сотрудников: "))
    adv = (v - i) / count
    print("Прибыль фирмы в расчете на одного сотрудника =", adv)
else:
    print("Фирма работает в убыток")
