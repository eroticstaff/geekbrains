class ZeroDivision(Exception):
    def __int__(self, *args, **kwargs):
        self.text = args[0]


def division(a, b):
    if b == 0:
        raise ZeroDivision("На ноль делить нельзя")
    return a / b

try:
    print(division(11, 0))
except Exception as err:
    print(err)