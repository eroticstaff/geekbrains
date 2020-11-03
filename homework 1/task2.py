#task_2
time = int(input("Input time: "))
hours = time // 60 // 60
minutes = time // 60 % 60
seconds = time % 60
print("{:02}:{:02}:{:02}".format(hours, minutes, seconds))