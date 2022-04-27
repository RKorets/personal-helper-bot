from addressbook import AddressBook
from field import Name, Phone, Email, Address, Birthday, Note
from sort_files import sort_folder
from prettytable.colortable import ColorTable, Themes
from notes import NotesBook
from notes import RecordNote
from records import Record


class Menu:

    @property
    def main_menu(self):
        show_menu = ColorTable(theme=Themes.OCEAN)
        show_menu.field_names = [f"{18 * '-'}Меню{18 * '-'}"]
        show_menu.hrules = 1
        show_menu.align = "l"
        show_menu.add_rows([["1. Контакти"],
                            ["2. Нотатки"],
                            ["3. Іменниники"],
                            ["4. Сортувати папку"],
                            ["5. Вихід"],
                            ])
        return show_menu

    @property
    def main_contact(self):
        show_main_contact = ColorTable(theme=Themes.OCEAN)
        show_main_contact.field_names = [f"{18 * '-'}Контакти{18 * '-'}"]
        show_main_contact.hrules = 1
        show_main_contact.align = "l"
        show_main_contact.add_rows([["1. Створити контакт"],
                                    ["2. Добавити дані до існуючого контакту"],
                                    ["3. Редагувати дані контакту"],
                                    ["4. Видалити дані з контакту"],
                                    ["5. Пошук контакту"],
                                    ["6. Вивести всі контакти"],
                                    ["7. Повернутись в попереднє меню"]])

        return show_main_contact

    @property
    def add_menu(self):
        show_add_contact = ColorTable(theme=Themes.OCEAN)
        show_add_contact.field_names = [
            f"{18 * '-'}Що будем добавляти?{18 * '-'}"]
        show_add_contact.hrules = 1
        show_add_contact.align = "l"
        show_add_contact.add_rows([["1. Телефон"],
                                   ["2. Емейл"],
                                   ["3. Адресу"],
                                   ["4. День народження"],
                                   ["5. Повернутись в попереднє меню"]])
        return show_add_contact

    @property
    def edit_menu(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}За яким критерієм?{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. ФІО"],
                            ["2.Телефон"],
                            ["3. Емейл"],
                            ["4. Адресу"],
                            ["5. День народження"],
                            ["6. Повернутись в попереднє меню"]])
        return show_edit

    @property
    def notes_menu(self):
        show_notes_menu = ColorTable(theme=Themes.OCEAN)
        show_notes_menu.field_names = [f"{18 * '-'}Нотатки{18 * '-'}"]
        show_notes_menu.hrules = 1
        show_notes_menu.align = "l"
        show_notes_menu.add_rows([["1. Подивитись всі нотатки"],
                                  ["2. Додати нотатку"],
                                  ["3. Знайти нотатку"],
                                  ["4. Змінити нотатку"],
                                  ["5. Видалити нотатку"],
                                  ["6. Сортувати нотатки за тегами"],
                                  ["7. Повернутись в попереднє меню"]])
        return show_notes_menu


    @property
    def search_note(self):
        show_edit = ColorTable(theme=Themes.OCEAN)
        show_edit.field_names = [f"{18 * '-'}За яким критерієм?"
                                 f"{18 * '-'}"]
        show_edit.hrules = 1
        show_edit.align = "l"
        show_edit.add_rows([["1. По id замітки"],
                            ["2. По тегу замітки"],
                            ["3. По головному слову"],
                            ["4. Повернутись в попереднє меню"]])
        return show_edit


class Handler:

    def __init__(self, notes_book: NotesBook, address_book: AddressBook):
        self.menu = Menu()
        self.notes_book = notes_book
        self.address_book = address_book
        self.main_action()

    def main_action_note(self):
        while True:
            print(self.menu.notes_menu)
            action = input("\033[34m" + "Обери потрібну команду(1-7), "
                                        "або я спробую вгадати: ").lower()
            if action in ["1", "check", "подивитись"]:
                self.notes_book.print_note_book()
            elif action in ["2", "create", "створити", "создать"]:
                record_note = RecordNote()
                record_note.add_note(Note(input('Введіть нонатку: '
                                                           '')))
                flag_tag = input("Чи хочете ви додати тег до замітки? Введіть "
                                 "так, якщо бажаєте, інакше ні: ").lower()
                if flag_tag in ["так", "yes", "да", "хочу"]:
                    record_note.add_tag(input('Введіть тег: '))
                self.notes_book.add_record_note(record_note)
            elif action in ["3", "знайти", "search", "пошук", "найти"]:
                self.notes_book.print_note_book(self.action_search_note())
            elif action in ["4", "edit", "редагувати", "змінити",
                                    "изменить"]:
                pass
            elif action in ["5", "delete", "remove", "видалити",
                                    "удалить", "стерти"]:
                del_notes = self.action_search_note(self.notes_book)
                print(f"Ви намагаєтесь видалити замітки:\n ")
                self.notes_book.print_note_book.del_notes
                flag_notes_delete = input("Якщо хочете видалити, напишіть"
                                          " + або так, для безпеки видаляйте "
                                          "за id: ").lower()
                if flag_notes_delete in ["+", "так", "хочу", "го",
                                                 "yes"]:
                    self.notes_book.delete_note(del_notes)
                    print("Успішно видалено!")
            elif action in ["сортувати", "sort", "сортування", "6",
                                    "сортировка"]:
                self.notes_book.sort_note()
            elif action in ["exit", "close", "good bye", "7", "вихід",
                                    "выход", "повернутись"]:
              
                break
            else:
                print("Ви помилились або нотаток немає")

    def action_search_note(self):
        while True:
            print(self.menu.search_note)

            command = input("\033[34m" + "Обери потрібну команду(1-4), "
                                         "або я спробую вгадати: ").lower()
            if command in ["id", "ид", "ід", "1"]:
                id_parametr = input('Введіть id нотатки: ').lower()
                return self.notes_book.search_parametr_note("id", id_parametr)
            elif command in ["tag", "тег", "notes", "2"]:
                tag_parametr = input('Введіть tag нотатки: ').lower()
                return self.notes_book.search_parametr_note("tag", tag_parametr)
            elif command in ["головне", "main", "слово", "3"]:
                word_parametr = input('Введіть головне слово нотатки: ')
                return self.notes_book.search_word_note(word_parametr)
            elif command in ["exit", "close", "good bye", "4",
                                     "вихід", "выход", "повернутись"]:
                print("Good bye!")
                break

    def action_phone(self):
        while True:
            print(self.menu.main_contact)
            action = input("\033[34m" + "Обери потрібну команду(1-7), "
                                        "або я спробую вгадати: ").lower()
            if action in ["1", "create", "створити", "создать"]:
                record_contact = Record(Name(input("Введіть ФІО контакту: ")))
                self.address_book.add_record(self.action_add_contact(record_contact))
            elif action in ["2", "add", "добавить", "додати"]:
                pass
            elif action in ["3", "edit", "редактировать", "редагувати"]:
                pass
            elif action in ["4", "delete", "удалить", "видалити"]:
                pass
            elif action in ["search", "пошук", "найти", "5"]:
                self.action_search_phone()
            elif action in ["всі", "вивести", "все", "6"]:
                print(self.address_book)
            elif action in ["exit", "close", "good bye", "7",
                            "вихід", "выход", "повернутись"]:
                break

    def action_add_contact(self, record_contact: Record):
        while True:
            print(self.menu.add_menu)
            action = input("\033[34m" + "Обери потрібну команду(1-5), "
                                        "або я спробую вгадати: ").lower()
            if action in ["1", "телефон", "phone"]:
                record_contact.add_phone(Phone(input("Введіть номер телефону: ")))
            elif action in ["2", "email", "емаил"]:
                record_contact.add_mail(Email(input("Введіть номер почту: ")))
            elif action in ["3", "email", "емаил"]:
                record_contact.add_address(Address(input("Введіть адресу: ")))
            elif action in ["4", "дата", "рождение"]:
                record_contact.add_address(Birthday(input("Введіть дату "
                                                 "народження в форматі "
                                                          "yyyy-mm-dd: ")))
            elif action in ["exit", "close", "good bye", "5",
                            "вихід", "выход", "повернутись"]:
                break

    def action_search_phone(self):
        while True:
            print(self.menu.edit_menu)

            command = input("\033[34m" + "Обери потрібну команду(1-4), "
                                         "або я спробую вгадати: ").lower()
            if command in ["телефон", "phone", "1"]:
                name_parametr = input('Введіть ФІО контакту: ').lower()
                print(self.address_book.search_by_name(name_parametr))
                return self.address_book.search_by_name(name_parametr)
            elif command in ["exit", "close", "good bye", "4",
                                     "вихід", "выход", "повернутись"]:
                print("Good bye!")
                break

    def main_action(self):
        while True:
            print(self.menu.main_menu)

            command = input("\033[34m" + "Обери потрібну команду(1-5), "
                                         "або я спробую вгадати: ")
            user_text = set()
            for el in command.split(' '):
                user_text.add(el.lower())

            contact = {"1", "1.", "контакт", "контакты", "контакти", "contact"}
            notes = {"2", "2.", "нотатки", "нотаткы", "notes", "нотатку", "замітки", "заметки"}
            birthday = {"3", "3.", "іменниники", "імениники", "birthday", "народження", "рождения"}
            sort = {"4", "4.", "сортувати", "sorted", "відсортувати", "посортувати", "сортировка", "sort"}
            close = {"5", "5.", "закрити", "вийти", "exit", "close", "good bye", "вихід", "выход", "завершити"}

            if len(user_text & contact) >= 1:
                self.action_phone()
            elif len(user_text & notes) >= 1:
                self.main_action_note()
            elif len(user_text & birthday) >= 1:
                self.address_book.get_bd(input("Введіть клількість днів за "
                                               "яких показати іменинників? "))
            elif len(user_text & sort) >= 1:
                # Dasha this need changes
                file_path = input('Введіть шлях до файлу')
                sort_folder(file_path)

            elif len(user_text & close) >= 1:
                print("Good bye!")
                break
            else:
                print("Я Вас не зрозумів:(\nСпробуйте ще раз!")


class Bot:

    def __init__(self):
        self.menu = Menu()
        self.notes_book = NotesBook()
        self.address_book = AddressBook()
        self.handler = Handler(self.notes_book, self.address_book)


if __name__ == "__main__":

    my_bot = Bot()
