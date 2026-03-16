import re
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value
    def __str__(self): return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    @property
    def value(self): return self._value
    @value.setter
    def value(self, val):
        if not re.fullmatch(r'\d{10}', val):
            raise ValueError("❌ Номер повинен містити 10 цифр (наприклад, 0501234567).")
        self._value = val

class Email(Field):
    @property
    def value(self): return self._value
    @value.setter
    def value(self, val):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not re.match(pattern, val):
            raise ValueError("❌ Некоректний формат Email.")
        self._value = val

class Birthday(Field):
    @property
    def value(self): return self._value
    @value.setter
    def value(self, val):
        try:
            self._value = datetime.strptime(val, "%d.%m.%Y").date()
        except:
            raise ValueError("❌ Формат дати: ДД.ММ.РРРР")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.email = None
        self.birthday = None

    def add_phone(self, phone_str):
        self.phones.append(Phone(phone_str))

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones) if self.phones else "немає"
        email = self.email.value if self.email else "немає"
        bday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "не вказано"
        return f"👤 {self.name.value:12} | 📞: {phones:12} | 📧: {email:15} | 🎂: {bday}"