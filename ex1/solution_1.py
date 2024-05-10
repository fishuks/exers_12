class Date:
    
    def __init__(self, date):
        
        if self.is_date(date):
            self.__date = date
        else:
            print('Ошибка')
            self.__date = None
    
    @staticmethod
    def leap_year(year):
        if year % 4 != 0:
            return False
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True

    def is_date(self, date):
        try:
            day, month, year = map(int, date.split('.'))
            if month < 1 or month > 12:
                return False
            if day < 1:
                return False
            if month == 2:
                if self.leap_year(year):
                    return day <= 29
                else:
                    return day <= 28
            elif month in [4, 6, 9, 11]:
                return day <= 30
            else:
                return day <= 31
        except (ValueError, IndexError):
            return False

    date = property()

    @date.setter
    def date(self, value):
        if self.is_date(value):
            self.__date = value
        else:
            print('Ошибка')
            self.__date = None

    @date.getter
    def date(self):
        if self.__date is not None:
            d = self.__date.split('.')
            mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
            return f'{int(d[0])} {mnth[int(d[1]) - 1]} {int(d[2])} г.'
        return str(self.__date)
    
    def to_timestamp(self):
        day, month, year = map(int, self.__date.split('.'))
        days_in_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        
        total_days = (year - 1970) * 365 + days_in_month[month - 1] + day - 1
        leap_years = (year - 1968) // 4 - (year - 1900) // 100 + (year - 1600) // 400
        
        if self.leap_year(year) and month > 2:
            total_days += 1
        
        timestamp = (total_days + leap_years) * 24 * 60 * 60
        return timestamp

    def __eq__(self, other):
        return Date.to_timestamp(self) == Date.to_timestamp(other)

    def __ne__(self, other):
        return Date.to_timestamp(self) != Date.to_timestamp(other)
    
    def __lt__(self, other):
        return Date.to_timestamp(self) < Date.to_timestamp(other)
    
    def __le__(self, other):
        return Date.to_timestamp(self) <= Date.to_timestamp(other)

                
    def __gt__(self, other):
        return Date.to_timestamp(self) > Date.to_timestamp(other)
    
    def __ge__(self, other):
        return Date.to_timestamp(self) >= Date.to_timestamp(other)

    def __str__(self):
        if self.__date is not None:
            d = self.__date.split('.')
            mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг','сен', 'окт', 'ноя', 'дек']
            return f'{int(d[0])} {mnth[int(d[1]) - 1]} {int(d[2])} г.'
        return str(self.__date)
    
    def __repr__(self):
        return self.__str__()
