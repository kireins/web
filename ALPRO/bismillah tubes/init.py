import sqlite3

conn_08 = sqlite3.connect('tasks.db')
c_08= conn_08.cursor()

# Membuat tabel
c_08.execute('''
          CREATE TABLE IF NOT EXISTS tasks
          (id INTEGER PRIMARY KEY,
          student_id INTEGER,
          student_name TEXT,
          task TEXT,
          time TEXT,
          location TEXT,
          status TEXT)
          ''')

conn_08.commit()
conn_08.close()
