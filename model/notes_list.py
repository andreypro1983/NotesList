from . import note


class NotesList:
    def __init__(self, path: str = 'data.json'):
        self.path = path
        self.notes: dict[int:note] = {}

    def add(self, add_note: note):
        self.notes[add_note.uid] = note
