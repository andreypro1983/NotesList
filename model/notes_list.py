from . import note


class NotesList:

    def __init__(self):
        self.notes = []
        self.id = 1

    def add(self, add_note: note.Note):
        add_note.uid = self.id
        self.id += 1
        self.notes.append(add_note)

    def edit(self, uid: int, header: str, body: str):
        edit_note = self.notes[uid]
        if header != '':
            edit_note.set_header(header)
        if body != '':
            edit_note.set_body(body)
        edit_note.set_note_date_now()

    def show(self) -> str:
        string = ''
        if len(self.notes) > 0:
            for item in self.notes:
                string += f'{item.for_print_full()} \n'
        return string

    def find(self, uid: int) -> bool:
        for item in self.notes:
            if item.get_uid() == uid:
                return True
        return False

    def remove(self, uid: int):
        for item in self.notes:
            if item.get_uid() == uid:
                self.notes.remove(item)

    def max_uid(self) -> int:
        max = 0
        for item in self.notes:
            if item.get_uid() > max:
                max = item.get_uid()
        return max

    def get_notes(self):
        return self.notes

    def set_notes(self, data):
        for item in data.values():
            item['note_date']
        print(data)
