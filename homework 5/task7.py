import json

with open("task7_text.txt", 'r', encoding='utf-8') as file:
    result = []
    companies = {}
    average = {}
    average_profit = 0
    n = 0
    for line in file:
        split = line.split(" ")
        income = int(split[2]) - int(split[3])
        if income > 0:
            companies[split[0]] = income
            average_profit += income
            n += 1
    average_profit /= n
    average["average_profit"] = average_profit
    result.append(companies)
    result.append(average)
json_text = json.dumps(result)
with open("task7_json.txt", 'w', encoding='utf-8') as file:
    file.write(json_text)
