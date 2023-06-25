import model.notes_list as nl
import model.note as note


class Service:
    def __init__(self, notes_list: nl.NotesList = nl.NotesList()):
        self.notes_list = notes_list

    def add(self, header: str, body: str):
        new_note = note.Note(header, body)
        self.notes_list.add(new_note)
        print(self.notes_list.show())
        

    def show(self) -> str:
        return self.notes_list.show()






