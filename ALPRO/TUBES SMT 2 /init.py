import sqlite3

# Koneksi ke database SQLite
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Membuat tabel
c.execute('''
CREATE TABLE tasks (
    id TEXT PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    task TEXT,
    status TEXT,
    time DATETIME ,
    location TEXT
)
''')

c.execute('''
    INSERT OR IGNORE INTO tasks (id, name, task, status, time, location)
    VALUES (?, ?, ?, ?, ?, ?)
    ''')

conn.commit()
conn.close()
