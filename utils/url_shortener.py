# utils/url_shortener.py

import sqlite3
import string
import random

class UrlShortener:
    def __init__(self, db_path='urls.db'):
        self.db_path = db_path
        self.chars = string.ascii_letters + string.digits

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def generate_short_code(self, length=6):
        return ''.join(random.choice(self.chars) for _ in range(length))

    def shorten(self, original_url):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Check if already shortened
        cursor.execute('SELECT short_code FROM urls WHERE original_url = ?', (original_url,))
        existing = cursor.fetchone()
        if existing:
            return existing[0]

        # Create new short code
        while True:
            short_code = self.generate_short_code()
            cursor.execute('SELECT id FROM urls WHERE short_code = ?', (short_code,))
            if not cursor.fetchone():
                break

        cursor.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
        conn.commit()
        conn.close()
        return short_code

    def get_original_url(self, short_code):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT original_url FROM urls WHERE short_code = ?', (short_code,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return result[0]
        return None
