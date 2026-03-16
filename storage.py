import pickle
import os


DATA_DIR = "data"
CONTACTS_PATH = os.path.join(DATA_DIR, "contacts.pkl")
NOTES_PATH = os.path.join(DATA_DIR, "notes.pkl")

def save_all(contacts, notes):
    """Функція створює папку data та зберігає туди файли .pkl"""
    # Якщо папки data немає — створюємо її
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    with open(CONTACTS_PATH, "wb") as f:
        pickle.dump(contacts, f)
        
    with open(NOTES_PATH, "wb") as f:
        pickle.dump(notes, f)

def load_all():
    """Функція завантажує дані з папки data"""
    from address_book import AddressBook
    from notes import NoteBook
    
    contacts = AddressBook()
    notes = NoteBook()
    
    # Перевіряємо чи існують файли перед завантаженням
    if os.path.exists(CONTACTS_PATH):
        with open(CONTACTS_PATH, "rb") as f:
            contacts = pickle.load(f)
            
    if os.path.exists(NOTES_PATH):
        with open(NOTES_PATH, "rb") as f:
            notes = pickle.load(f)
            
    return contacts, notes