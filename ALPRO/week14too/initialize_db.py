import json
import sqlite3

# Memuat data JSON
with open('local_restaurant.json') as f:
    data = json.load(f)

conn = sqlite3.connect('restaurants.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS restaurants')
c.execute('DROP TABLE IF EXISTS menus')

# Membuat tabel
c.execute('''
CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    pictureId TEXT,
    city TEXT,
    rating REAL
)
''')

c.execute('''
CREATE TABLE menus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER,
    type TEXT,
    name TEXT,
    FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
)
''')

# Memasukkan data ke tabel
for restaurant in data['restaurants']:
    c.execute('''
    INSERT INTO restaurants (name, description, pictureId, city, rating)
    VALUES (?, ?, ?, ?, ?)
    ''', (restaurant['name'], restaurant['description'], restaurant['pictureId'], restaurant['city'], restaurant['rating']))

    restaurant_id = c.lastrowid

    for food in restaurant['menus']['foods']:
        c.execute('''
        INSERT INTO menus (restaurant_id, type, name)
        VALUES (?, ?, ?)
        ''', (restaurant_id, 'food', food['name']))

    for drink in restaurant['menus']['drinks']:
        c.execute('''
        INSERT INTO menus (restaurant_id, type, name)
        VALUES (?, ?, ?)
        ''', (restaurant_id, 'drink', drink['name']))

# Menyimpan dan menutup koneksi
conn.commit()
conn.close()
