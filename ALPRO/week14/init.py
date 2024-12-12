import json
import sqlite3

# Memuat data JSON
with open('local_restaurant.json') as f:
    data = json.load(f)

# Koneksi ke database SQLite
conn = sqlite3.connect('restaurants.db')
c = conn.cursor()

# Membuat tabel
c.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    id TEXT PRIMARY KEY,
    name TEXT,
    description TEXT,
    pictureId TEXT,
    city TEXT,
    rating REAL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS menus (
    restaurant_id TEXT,
    type TEXT,
    name TEXT,
    FOREIGN KEY(restaurant_id) REFERENCES restaurants(id)
)
''')

# Memasukkan data ke tabel
for restaurant in data['restaurants']:
    c.execute('''
    INSERT OR IGNORE INTO restaurants (id, name, description, pictureId, city, rating)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (restaurant['id'], restaurant['name'], restaurant['description'], restaurant['pictureId'], restaurant['city'], restaurant['rating']))

    for food in restaurant['menus']['foods']:
        c.execute('''
        INSERT INTO menus (restaurant_id, type, name)
        VALUES (?, ?, ?)
        ''', (restaurant['id'], 'food', food['name']))

    for drink in restaurant['menus']['drinks']:
        c.execute('''
        INSERT INTO menus (restaurant_id, type, name)
        VALUES (?, ?, ?)
        ''', (restaurant['id'], 'drink', drink['name']))

# Menyimpan dan menutup koneksi
conn.commit()
conn.close()

