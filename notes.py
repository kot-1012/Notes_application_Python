from datetime import datetime

def create_note(notes, title, content):

# Создает новую заметку и добавляет ее в список заметок.
#     notes (list): Список существующих заметок.
#     title (str): Заголовок новой заметки.
#     content (str): Текст новой заметки.

    note_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {"id": len(notes) + 1, "title": title, "content": content, "date_created": note_date, "last_modified": note_date}
    notes.append(note)
    return notes

def read_notes(notes):

# Возвращает список заметок.
# notes (list): Список заметок.

    return notes

def read_note(notes, note_id):

# Возвращает заметку по ее ID.
#   notes (list): Список заметок.
#   note_id (int): ID заметки для чтения.
# 	если найдена, иначе None.

    for note in notes:
        if note['id'] == note_id:
            return note
    return None

def edit_note(notes, note_id, new_content):

# Редактирует содержимое заметки по ее ID.
#   notes (list): Список заметок.
#   note_id (int): ID заметки для редактирования.
#   new_content (str): Новое содержимое заметки.
# 	True, если заметка найдена и отредактирована, иначе False.

    for note in notes:
        if note['id'] == note_id:
            note['content'] = new_content
            note['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return True
    return False

def delete_note(notes, note_id):

# Удаляет заметку по ее ID.
#   notes (list): Список заметок.
#   note_id (int): ID заметки для удаления.
# 	True, если заметка найдена и удалена, иначе False.

    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            return True
    return False
