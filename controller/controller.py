import view.view as v
import view.text as txt
from model.service import Service as serv


class Controller:
    def __init__(self, service: serv, view: v.View, text: txt.Text):
        self.service = service
        self.view = view
        self.text = text

    def start(self):
        while True:
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
                    pass

    def add(self):
        print(self.view.input_note())
        serv.add(*self.view.input_note())
        self.view.print_note_add()

    def show(self):
        pass
