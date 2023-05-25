import json
from datetime import datetime

class Note:
    # Конструктор, инициализирующий атрибуты объекта
    def __init__(self, note_id, title, body, timestamp):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp
