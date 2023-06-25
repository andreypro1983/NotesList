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
                    pass
                case 2:
                    pass
                case 3:
                    self.add()
                case 4:
                    self.show()
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    self.exit()

    def add(self):
        self.service.add(*self.view.input_note())
        self.view.print_message(self.text.add_note_success)

    def show(self):
        notes = self.service.show()
        if notes == '':
            notes = self.text.empty_notes_list
        self.view.print_message(notes)

    def exit(self):
        self.view.print_message(self.text.exit_message)
        self.is_work = False

