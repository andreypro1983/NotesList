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
    
    def find(self, uid: int) -> bool:
        if uid in self.notes:
            return True
        else:
            return False

    
    def remove(self, remove_note: note.Note):
        if remove_note.get_uid() in self.notes:
            del self.notes[remove_note.get_uid()]
   
