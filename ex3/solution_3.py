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

    
    @property
    def date(self):
        if self.__date is not None:
            d = self.__date.split('.')
            mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
            return f'{int(d[0])} {mnth[int(d[1]) - 1]} {int(d[2])} г.'
        return str(self.__date)

    @date.setter
    def date(self, value):
        if self.is_date(value):
            self.__date = value
        else:
            print('Ошибка')
            self.__date = None
  
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

class Meeting:

    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = id
        self.date = Date(date)
        self.title = title
        self.employees = []

    def add_person(self, person):
        self.employees.append(person)

    def count(self):
        return len(self.employees)

    @classmethod
    def count_meeting(cls, date):
        count = 0
        for meet in cls.lst_meeting:
            if str(meet.date) == str(date):
                count += 1
        return count

    @classmethod
    def total(cls):
        count = 0
        for meet in cls.lst_meeting:
            count += meet.count()
        return count

    def __str__(self):
        strng = f'Рабочая встреча {self.id}\n{self.date} {self.title}\n'
        for pers in self.employees:
            strng += f'{pers}\n'
        return strng
    
class User:
    lst_person = []

    def __init__(self, id, nick_name, first_name, 
                 last_name, middle_name, gender):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        User.lst_person.append(self)

    def __str__(self):
        strng = ''

        if self.id:
            strng += f'ID: {self.id} '

        if self.nick_name:
            strng += f'LOGIN: {self.nick_name} '

        name_parts = [self.last_name, self.first_name, self.middle_name]
        name = ' '.join(filter(None, name_parts))
        if name:
            strng += f'NAME: {name} '

        if self.gender:
            strng += f'GENDER: {self.gender} '

        return strng

    def __repr__(self):
        return f'{self.id}' 

class Load:

    @staticmethod
    def write(meet_text, pers_text, pers_meet_text):
        
        with open(pers_text, 'r', encoding="utf8") as f:
            attributes = f.readline().strip().split(';')
            for line in f:
                values = line.strip().split(';')
                user_data = dict(zip(attributes, values))
                User.lst_person.append(User(user_data['id'], user_data['nick_name'],
                                            user_data['first_name'], user_data['last_name'],
                                            user_data['middle_name'], user_data.get('gender', '')))

        with open(meet_text, 'r', encoding="utf8") as f:
            attributes = f.readline().strip().split(';')
            for line in f:
                values = line.strip().split(';')
                meeting_data = dict(zip(attributes, values))
                Meeting.lst_meeting.append(Meeting(meeting_data['id'], meeting_data['date'], meeting_data['title']))

        with open(pers_meet_text, 'r', encoding="utf8") as f:
            f.readline()
            for line in f:
                meeting_id, user_id = line.strip().split(';')[:-1]
                for meet in Meeting.lst_meeting:
                    if meet.id == meeting_id:
                        for pers in User.lst_person:
                            if pers.id == user_id:
                                meet.add_person(pers)
                                break

