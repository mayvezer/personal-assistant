from storage import save_all, load_all
from record import Record, Email, Birthday
from utils import get_suggestion

def main():
    contacts, notes = load_all()
    cmd_list = ["add-contact", "find-contact", "all-contacts", "birthdays", "add-note", "search-tag", "exit"]

    print("🚀 Персональний Помічник v1.0 запущено!")
    print(f"Завантажено контактів: {len(contacts)}, заміток: {len(notes)}")

    while True:
        choice = input("\n>> ").strip().lower()

        if choice in ["exit", "quit", "вихід"]:
            save_all(contacts, notes)
            print("👋 Дані збережено. До зустрічі!")
            break

        if choice not in cmd_list:
            sug = get_suggestion(choice, cmd_list)
            if sug and input(f"🤔 Команда не зрозуміла. Мали на увазі '{sug}'? (y/n): ").lower() == 'y':
                choice = sug
            else:
                print("⚠️  Невідома команда. Введіть 'exit' для виходу.")
                continue

        if choice == "add-contact":
            name = input("Введіть ім'я: ")
            rec = Record(name)
            try:
                phone = input("Телефон (10 цифр): ")
                rec.add_phone(phone)
                email = input("Email (або Enter): ")
                if email: rec.email = Email(email)
                bd = input("Дата народження (ДД.ММ.РРРР або Enter): ")
                if bd: rec.birthday = Birthday(bd)
                contacts.add_record(rec)
                print("✅ Контакт успішно збережено!")
            except ValueError as e: print(e)

        elif choice == "all-contacts":
            if not contacts: print("Список порожній.")
            for r in contacts.data.values(): print(r)

        elif choice == "find-contact":
            q = input("Що шукаємо (ім'я або номер)?: ")
            res = contacts.find_records(q)
            for r in res: print(r)

        elif choice == "birthdays":
            days = input("Прогноз у днях: ")
            res = contacts.get_upcoming_birthdays(days)
            print("\n".join(res) if res else "Найближчих свят немає.")

        elif choice == "add-note":
            text = input("Текст замітки: ")
            tags = input("Теги (через кому): ")
            notes.add_note(text, tags)
            print("✅ Замітка додана.")

        elif choice == "search-tag":
            tag = input("Введіть тег для пошуку: ")
            res = notes.search_by_tag(tag)
            print("\n".join(res) if res else "Нічого не знайдено.")

if __name__ == "__main__":
    main()