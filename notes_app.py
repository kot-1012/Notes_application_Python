import notes
import notes_storage
import os

def main():
# Загрузка заметок из файла при запуске приложения
    notes_data = notes_storage.load_notes_from_json()

    while True:
# Вывод меню с доступными действиями
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Прочитать список заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти из программы")

# Запрос выбора действия от пользователя
        choice = input("Выберите действие: ")

        if choice == "1":
# Создание новой заметки
            title = input("Введите заголовок заметки: ")
            content = input("Введите текст заметки: ")
            notes_data = notes.create_note(notes_data, title, content)
            notes_storage.save_notes_to_json(notes_data)
            print("Заметка успешно создана.")
        elif choice == "2":
# Вывод списка всех заметок
            print("Список заметок:")
            for note in notes_data:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['date_created']}")
        elif choice == "3":
 # Чтение заметки по ID
            note_id = int(input("Введите ID заметки для чтения: "))
            note = notes.read_note(notes_data, note_id)
            if note:
                print(f"ID: {note['id']}, Заголовок: {note['title']}")
                print(f"Дата создания: {note['date_created']}")
                print("Текст заметки:")
                print(note['content'])
            else:
                print("Заметка с таким ID не найдена.")
        elif choice == "4":
# Редактирование заметки по ID
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_content = input("Введите новое содержимое заметки: ")
            if notes.edit_note(notes_data, note_id, new_content):
                notes_storage.save_notes_to_json(notes_data)
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка с таким ID не найдена.")
        elif choice == "5":
# Удаление заметки по ID
            note_id = int(input("Введите ID заметки для удаления: "))
            if notes.delete_note(notes_data, note_id):
                notes_storage.save_notes_to_json(notes_data)
                print("Заметка успешно удалена.")
            else:
                print("Заметка с таким ID не найдена.")
        elif choice == "6":
# Выход из программы
            print("Выход из программы.")
            break
        else:
 # Обработка неверного выбора
            print("Неверный выбор. Пожалуйста, выберите от 1 до 6.")

if __name__ == "__main__":
    main()
