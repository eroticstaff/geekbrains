#task_6
a = int(input("a: "))
b = int(input("b: "))
i = 1
while True:
    print("{}-й день: {:.2f}".format(i, a))
    if a > b:
        print("Ответ: на {}-й день спортсмен достиг результата - не менее {} км.".format(i,b))
        break
    a = a*1.1
    i+=1