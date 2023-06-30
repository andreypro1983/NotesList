
class Text:
    def __init__(self):
        self.textmenu = ['Главное меню:',
                         'Сохранить заметки',
                         'Загрузить заметки',
                         'Добавить заметку',
                         'Вывести краткий список заметок',
                         'Вывести заметки на дату',
                         'Вывести подробную информацию по заметке',
                         'Редактировать заметку',
                         'Удалить заметку',
                         'Выход']
        self.input_message = 'Выберите пункт меню: '
        self.find_note_by_date = '\nВывод списка заметок по дате: '
        self.find_note_by_id = '\nВывод подробной информации заметки по id: '
        self.show_note_info = '\nПодробная информация по заметке:\n'
        self.input_date = '\nВведите дату в формате [dd-mm-yyyy]: '
        self.input_note = ['\nВведите заголовок заметки: ',
                           'Введите тело заметки: ']
        self.input_uid = '\nВведите id заметки: '
        self.exit_message = '\n!!!До свидания!!!'
        self.empty_notes_list = 'Список заметок пуст'
        self.show_notes_list_short = '\n!!!Полный список заметок!!!'
        self.show_notes_list = '\n!!!Список заметок!!!'
        self.add_note = '\n!!!Добавление заметки!!!'
        self.remove_note = '\n!!!Удаление заметки!!!'
        self.edit_note = '\n!!!Редактирование заметки!!!'
        self.input_uid_digit_error = '\nВведенное значение не является числом'
        self.add_note_successful = '\nЗаметка успешно добавлена'
        self.remove_note_successful = '\nЗаметка успешно удалена'
        self.edit_note_successful = '\nЗаметка успешно изменена'
        self.notes_save_successful = '\nЗаметки успешно сохранены'
        

 

    def input_uid_find_error(self, uid: int) -> str:
        return f'\nЗаметка с id = {(uid)} не найдена. Проверьте id заметки и повторите действие'

    def input_menu_error(self) -> str:
        return f'Введено недопустимое значение: выберите пункт от 1 до {len(self.textmenu)-1}'
    

