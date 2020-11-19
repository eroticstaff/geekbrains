with open("task6_text.txt", 'r', encoding='utf-8') as file:
    result = {}
    for line in file:
        split = line.split(" ")
        count = 0
        for i in range(1, len(split)):
            count += int(split[i].split("(")[0]) if split[i] != '—' else 0
        result[split[0].split(':')[0]] = count
    print(result)
