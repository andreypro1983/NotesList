import model.notes_list as nl
import model.note as note


class Service:
    def __init__(self, notes_list: nl.NotesList = nl.NotesList()):
        self.notes_list = notes_list

    def add(self, header: str, body: str):
        new_note = note.Note(header, body)
        self.notes_list.add(new_note)

    def edit(self, uid: int, header: str, body: str):
        self.notes_list.edit(uid, header, body)    

    def find(self, uid: str) -> int:
        if self.notes_list.find(int(uid)):
            return int(uid)
        else:
            return -1

    def show(self) -> str:
        return self.notes_list.show()

    def remove(self, uid: int):
        self.notes_list.remove(self.notes_list.notes[uid])
