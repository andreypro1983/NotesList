import datetime
import model.notes_list as nl
import model.note as note
import json


class Service:
    def __init__(self, notes_list: nl.NotesList = nl.NotesList(), path: str = 'data.json'):
        self.notes_list = notes_list
        self.path = path

    def add(self, header: str, body: str):
        new_note = note.Note(header, body)
        self.notes_list.add(new_note)

    def load(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.notes_list.notes = []
                for item in data:
                    header = item['header']
                    body = item['body']
                    load_note = note.Note(header, body)
                    load_note.uid = item['uid']
                    load_note.note_date = datetime.datetime.strptime(
                        item['note_date'], '%Y-%m-%d %H:%M:%S.%f')
                    self.notes_list.get_notes().append(load_note)
                self.notes_list.id = self.notes_list.max_uid()+1
        except FileNotFoundError:
            print('\nФайл для загрузки не найден')
        except Exception as e:
            print('\n')
            print(e)

    def save(self):
        data = []
        for save_note in self.notes_list.get_notes():
            data.append(save_note.to_json())

        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def edit(self, uid: int, header: str, body: str):
        self.notes_list.edit(uid, header, body)

    def show_notes_by_date(self, input_date: str) -> str:
        if self.is_valid_date(input_date):
            # print(datetime.datetime.strptime(input_date, '%d-%m-%Y'))  # принт
            return self.notes_list.show_notes_by_date(datetime.datetime.strptime(input_date, '%d-%m-%Y'))
        else:
            return '\nВведена некорректная дата'

    def show_note_by_id(self, id: int) -> str:
        return self.notes_list.show_note_by_id(id)

    def is_valid_date(self, input_date: str) -> bool:
        try:
            datetime.datetime.strptime(input_date, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def find(self, uid: str) -> int:
        if self.notes_list.find(int(uid)):
            return int(uid)
        else:
            return -1

    def show(self) -> str:
        return self.notes_list.show()

    def remove(self, uid: int):
        self.notes_list.remove(uid)
