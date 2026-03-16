from collections import UserDict

class Note:
    def __init__(self, text, tags):
        self.text = text
        self.tags = [t.strip().lower() for t in tags.split(",") if t.strip()]

    def __str__(self):
        tags_str = f" [#{' #'.join(self.tags)}]" if self.tags else ""
        return f"📝 {self.text}{tags_str}"

class NoteBook(UserDict):
    def add_note(self, text, tags):
        self.data[len(self.data) + 1] = Note(text, tags)

    def search_by_tag(self, tag):
        tag = tag.lower().strip()
        return [f"ID {idx}: {n}" for idx, n in self.data.items() if tag in n.tags]