from . import note
import datetime


class NotesList:

    def __init__(self):
        self.notes: list[note.Note] = []
        self.id: int = 1

    def add(self, add_note: note.Note):
        add_note.uid = self.id
        self.id += 1
        self.notes.append(add_note)

    def edit(self, id: int, header: str, body: str):
        edit_note = self.find_note_by_id(id)
        if header != '':
            edit_note.set_header(header)
        if body != '':
            edit_note.set_body(body)
        edit_note.set_note_date_now()

    def show(self) -> str:
        string = ''
        if len(self.notes) > 0:
            for item in self.notes:
                string += f'{item.for_print_short()} \n'
        return string

    def show_notes_by_date(self, input_date: datetime.datetime) -> str:
        # print(input_date) # принт
        string = ''
        if len(self.notes) > 0:
            is_found = False
            for item in self.notes:
                # print(item.note_date.date()) #  принт
                if item.note_date.date() == input_date.date():
                    is_found = True
                    string += f'{item.for_print_full()} \n'
            if not is_found:
                string = f'Заметки за {input_date.strftime("%d-%m-%Y")} не найдены'
        else:
            string = f'Список заметок пуст'
        return string

    def show_note_by_id(self, uid: int) -> str:
        for item in self.notes:
            if item.get_uid() == uid:
                return item
       
        
    def find(self, uid: int) -> bool:
        for item in self.notes:
            if item.get_uid() == uid:
                return True
        return False

    def find_note_by_id(self, uid: int) -> note.Note:
        for item in self.notes:
            if item.get_uid() == uid:
                return item

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

    # def set_notes(self, data):
    #     for item in data.values():
    #         item['note_date']
    #     print(data)
