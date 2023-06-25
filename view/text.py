
class Text:
    def __init__(self):
        self.textmenu = ['Главное меню:',
                         'Сохранить файл',
                         'Загрузить файл',
                         'Добавить заметку',
                         'Вывести весь список заметок',
                         'Вывести заметки на дату',
                         'Редактировать заметку',
                         'Удалить заметку',
                         'Выход']
        self.input_message = 'Выберите пункт меню: '
        self.input_note = ['Введите заголовок заметки: ',
                           'Введите тело заметки: ']
        self.add_note_success = '\n Заметка успешно добавлена'
        self.exit_message = '\n До свидания!!!'
        self.empty_notes_list = '\n Список заметок пуст'

    def input_menu_error(self) -> str:
        return f'Введено недопустимое значение: выберите пункт от 1 до {len(self.textmenu)-1}'
    

