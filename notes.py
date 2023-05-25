import json
from datetime import datetime

class Note:
    # Конструктор, инициализирующий атрибуты объекта
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp

class NoteApp:
    # Конструктор, инициализирующий пустой список заметок
    def __init__(self):
        self.notes = []

    # Сохранение заметки в файл в формате JSON
    def save_notes_to_file(self):
        with open('notes.json', 'w') as file:
            json.dump([note.__dict__ for note in self.notes], file)

    # Загрузка заметки из файла в формате JSON
    def load_notes_from_file(self):
        try:
            with open('notes.json', 'r') as file:
                data = json.load(file)
                self.notes = [Note(**note_data) for note_data in data]
        except FileNotFoundError:
            self.notes = []

    # Добавление новую заметку в список заметок
    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(note_id, title, body, timestamp)
        self.notes.append(note)
        self.save_notes_to_file()

    # Редактирование существующей заметки по идентификатору
    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.body = new_body
                note.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes_to_file()
                return

    # Удаление заметки по идентификатору
    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]
        self.save_notes_to_file()

    # Фильтрование заметок по заданной дате
    def filter_notes_by_date(self, date):
        filtered_notes = [note for note in self.notes if note.timestamp.split()[0] == date]
        return filtered_notes

    # Отображение информации о заметке по идентификатору
    def display_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                print(f"ID: {note.note_id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело заметки: {note.body}")
                print(f"Дата: {note.timestamp}")
                return
        print("Заметка не найдена.")

    # Отображение информации о всех заметках
    def display_all_notes(self):
        for note in self.notes:
            print(f"ID: {note.note_id}")
            print(f"Заголовок: {note.title}")
            print(f"Тело заметки: {note.body}")
            print(f"Дата: {note.timestamp}")
            print("---")

app = NoteApp()
app.load_notes_from_file()

while True:
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Отфильтровать заметки по дате")
    print("5. Отобразить заметку")
    print("6. Отобразить все заметки")
    print("0. Выход")

    choice = input("Введите цифру операции, чтобы продолжить: ")

    if choice == "1":
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        app.add_note(title, body)
        print("Заметка успешно сохранена.")
    elif choice == "2":
        print("Список существующих заметок:")
        app.display_all_notes()
        note_id = int(input("Введите ID заметки из списка: "))
        new_title = input("Введите новый заголовок: ")
        new_body = input("Введите новое содержимое: ")
        app.edit_note(note_id, new_title, new_body)
        print("Заметка успешно отредактирована.")
    elif choice == "3":
        print("Список существующих заметок:")
        app.display_all_notes()
        note_id = int(input("Введите ID заметки из списка: "))
        app.delete_note(note_id)
        print("Заметка успешно удалена.")
    elif choice == "4":
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        filtered_notes = app.filter_notes_by_date(date)
        if filtered_notes:
            print("Отфильтрованные заметки:")
            for note in filtered_notes:
                print(f"ID: {note.note_id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело заметки: {note.body}")
                print(f"Дата: {note.timestamp}")
                print("---")
        else:
            print("Заметки не найдены.")
    elif choice == "5":
        print("Список существующих заметок:")
        app.display_all_notes()
        note_id = int(input("Введите ID заметки из списка: "))
        app.display_note(note_id)
    elif choice == "6":
        app.display_all_notes()
    elif choice == "0":
        app.save_notes_to_file()
        print("Выход...")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")