class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date_int(cls, date):
        date_split = date.split('-')
        day = int(date_split[0])
        month = int(date_split[1])
        year = int(date_split[2])
        return day, month, year

    @staticmethod
    def validate(date):
        day, month, year = Date.get_date_int(date)
        if month > 12 or month < 1:
            raise ValueError("Номер месяца выходит за границы возможных значений")
        print("Всё ок!")

date = Date("12-11-2020")
date.validate(date.date)