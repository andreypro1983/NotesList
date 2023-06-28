import datetime


class Note:

    def __init__(self, header: str, body: str):
        self.uid = None
        self.header = header
        self.body = body
        self.note_date = datetime.datetime.now()

    def set_header(self, new_header: str):
        self.header = new_header

    def set_body(self, new_body: str):
        self.body = new_body

    def set_note_date_now(self):
        self.note_date = datetime.datetime.now()

    def get_uid(self):
        return self.uid

    def for_print_full(self) -> str:
        return f'ID: {self.uid:>3}   ДАТА СОЗДАНИЯ/ИЗМЕНЕНИЯ: {self.note_date}   ЗАГОЛОВОК: {self.header}'

    def to_json(self):
        return {'uid': self.uid, 'header': self.header, 'body': self.body, 'note_date': self.note_date.strftime("%Y-%m-%d %H:%M:%S.%f")}

    def __str__(self) -> str:
        return f'"uid": {self.uid}, "header": {self.header}, "body": {self.body}, "note_date": {self.note_date}'
