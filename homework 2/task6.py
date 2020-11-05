items = [(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
         (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
         (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
result = {}
for item in items:
    for category in item[1].keys():
        if category in result.keys():
            if item[1][category] not in result[category]:
                result[category].append(item[1][category])
        else:
                result[category] = [item[1][category]]
print(result)