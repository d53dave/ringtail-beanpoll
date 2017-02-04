from datetime import datetime
import sqlite3

class RingtailPersistence():
    def __init__(self):
        self.connection = sqlite3.connect('~/.ringtail/ringtail.db')

    def persist(self, obj):
        pass
