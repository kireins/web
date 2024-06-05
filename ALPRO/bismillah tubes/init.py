import sqlite3

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# Create table
c.execute('''
          CREATE TABLE IF NOT EXISTS tasks
          (id INTEGER PRIMARY KEY,
          student_id INTEGER,
          student_name TEXT,
          task TEXT,
          time TEXT,
          location TEXT,
          status TEXT)
          ''')

conn.commit()
conn.close()
