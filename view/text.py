
class Text:
    def __init__(self):
        self.textmenu = ['Главное меню:',
                         'Сохранить файл',
                         'Загрузить файл',
                         'Добавить заметку',
                         'Вывести список заметок',
                         'Вывести заметки на дату',
                         'Редактировать заметку',
                         'Удалить заметку',
                         'Выход']
        self.input_message = 'Выберите пункт меню: '
        self.input_note = ['Введите заголовок заметки: ',
                           'Введите тело заметки: ']
        self.input_uid = 'Введите id заметки: '
        self.add_note_successful = '\nЗаметка успешно добавлена'
        self.exit_message = '\nДо свидания!!!'
        self.empty_notes_list = '\nСписок заметок пуст'
        self.show_notes_list = '\nCписок заметок:'
        self.add_note = '\nДобавление заметки\n'
        self.remove_note = '\nУдаление заметки\n'
        self.edit_note = '\nРедактирование заметки\n'
        self.input_uid_digit_error = '\nВведенное значение не является числом'
        self.remove_note_successful = '\nЗаметка успешно удалена'
        self.edit_note_successful = '\nЗаметка успешно изменена'


    def input_uid_find_error(self, uid: int) -> str:
        return f'\nЗаметка с id = {(uid)} не найдена. Проверьте id заметки и повторите действие'

    def input_menu_error(self) -> str:
        return f'Введено недопустимое значение: выберите пункт от 1 до {len(self.textmenu)-1}'
    

