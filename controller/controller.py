import view.view as v
import view.text as txt
from model.service import Service as serv


class Controller:
    def __init__(self, service: serv, view: v.View, text: txt.Text):
        self.service = service
        self.view = view
        self.text = text
        self.is_work = True

    def start(self):

        while self.is_work:
            user_input = int(self.view.menu())
            match user_input:
                case 1:
                    self.save()
                case 2:
                    self.load()
                case 3:
                    self.add()
                case 4:
                    self.show()
                case 5:
                    pass
                case 6:
                    self.edit()
                case 7:
                    self.remove()
                case 8:
                    self.exit()

    def add(self):
        self.view.print_message(self.text.add_note.upper())
        self.service.add(*self.view.input_note())
        self.view.print_message(self.text.add_note_successful)

    def save(self):
        self.service.save()

    def load(self):
        self.service.load()

    def find(self) -> int:
        input_uid = self.view.input_uid()
        if input_uid.isdigit():
            uid = self.service.find(input_uid)
            if uid != -1:
                return uid
            else:
                self.view.print_message(self.text.input_uid_find_error(input_uid))
                return -1
        else:
            self.view.print_message(self.text.input_uid_digit_error)
            return -1

    def edit(self):
        self.view.print_message(self.text.edit_note.upper())
        uid = self.find()
        if uid != -1:
            edit_info = self.view.input_note()
            self.service.edit(uid, edit_info[0], edit_info[1])
            self.view.print_message(self.text.edit_note_successful)
            

    def show(self):
        notes = self.service.show()
        self.view.print_message(self.text.show_notes_list.upper())
        if notes == '':
            notes = self.text.empty_notes_list
        self.view.print_message('\n' + notes)

    def remove(self):
        self.view.print_message(self.text.remove_note.upper())
        uid = self.find()
        if uid != -1:
            self.service.remove(uid)
            self.view.print_message(self.text.remove_note_successful)

    def exit(self):
        self.view.print_message(self.text.exit_message.upper())
        self.is_work = False
