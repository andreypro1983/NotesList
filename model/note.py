import datetime


class Note:
    count = 1

    def __init__(self, header: str, body: str):
        self.header = header
        self.body = body
        self.note_date = datetime.datetime.now()
        self.uid = Note.count
        Note.count += 1

    def get_uid(self):
        return self.uid

    def for_print(self) -> str:
        return f'id: {self.uid} Заголовок: {self.header} Тело заметки: {self.body} Дата создания/изменения: {self.note_date}'

   # def __str__(self) -> str:
    #     return f'{self.uid} {self.header} {self.body} {self.note_date}'
