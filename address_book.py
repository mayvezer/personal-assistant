from collections import UserDict
from datetime import datetime

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find_records(self, query):
        results = []
        for rec in self.data.values():
            if query.lower() in rec.name.value.lower():
                results.append(rec)
            elif any(query in p.value for p in rec.phones):
                results.append(rec)
        return results

    def get_upcoming_birthdays(self, days):
        today = datetime.now().date()
        upcoming = []
        for rec in self.data.values():
            if not rec.birthday: continue
            bday = rec.birthday.value.replace(year=today.year)
            if bday < today: bday = bday.replace(year=today.year + 1)
            if 0 <= (bday - today).days <= int(days):
                upcoming.append(f"🎉 {rec.name.value} ({bday.strftime('%d.%m.%Y')})")
        return upcoming