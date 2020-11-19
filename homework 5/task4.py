words = {"One":"Один", "Two": "Два", "Three":"Три","Four":"Четыре"}
with open("task4_text.txt", 'r', encoding="utf-8") as file:
    result = []
    for line in file:
        split = line.split(" ")
        split[0] = words[split[0]]
        result.append(" ".join(split))
    with open("task4_result.txt", 'w', encoding='utf-8') as file_write:
        file_write.writelines(result)