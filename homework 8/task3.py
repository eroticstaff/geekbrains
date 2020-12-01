class NotIntError(Exception):
    def __init__(self, *args, **kwargs):
        self.text = args[0]

array = []
text = input(">> ")
while text != "stop":
    try:
        for j in text:
            if j < '0' or j > '9':
                raise NotIntError("Введено не число!")
        array.append(int(text))
    except Exception as err:
        print(err, "Попробуйте еще раз...")

    text = input(">> ")
print(array)

