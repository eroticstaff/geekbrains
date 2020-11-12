from sys import argv

file_path, hours, stavka, premiya = argv

payment = int(hours) * int(stavka) + int(premiya)
print(payment)