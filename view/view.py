from ast import Tuple
from view.text import Text


class View:

    def __init__(self, text: Text):
        self.text = text

    def menu(self) -> int:
        print('\n' + self.text.textmenu[0])
        for i, item in enumerate(self.text.textmenu[1:], 1):
            print(f'{i:>4}. {item}')
        while True:
            command = input('\n' + self.text.input_message)
            if command.isdigit() and 0 < int(command) < len(self.text.textmenu):
                return int(command)
            print(self.text.input_menu_error())

    def input_note(self) -> Tuple(str):
        return tuple([input(line) for line in self.text.input_note])

    def print_message(self, txt: str):
        print(txt)

   