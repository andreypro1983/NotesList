import datetime


class Note:
    count = 1

    def __init__(self, header: str, body: str, note_date: datetime):
        self.header = header
        self.body = body
        self.note_date = note_date
        self.uid = Note.count
        Note.count += 1

    def get_uid(self):
        return self.uid

    def __str__(self) -> str:
        return f'{self.uid} {self.header} {self.body} {self.note_date}'
