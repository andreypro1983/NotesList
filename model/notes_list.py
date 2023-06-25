from . import note


class NotesList:
    def __init__(self, path: str = 'data.json'):
        self.path = path
        self.notes: dict[int:note.Note] = {}

    def add(self, add_note: note.Note):
        self.notes[add_note.uid] = add_note

    def show(self) -> str:
        string = ''
        if len(self.notes) > 0:
            for value in self.notes.values():
                string += f'{value.for_print()} \n'
        return string
