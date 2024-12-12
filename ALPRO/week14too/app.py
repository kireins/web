import streamlit as st
import sqlite3
import pandas as pd

# Fungsi untuk mengambil data dari SQLite
def get_data():
    conn = sqlite3.connect('restaurants.db')
    restaurants = pd.read_sql_query('SELECT * FROM restaurants', conn)
    menus = pd.read_sql_query('SELECT * FROM menus', conn)
    conn.close()
    return restaurants, menus

# Fungsi untuk menampilkan data restoran
def display_data():
    restaurants, menus = get_data()
    
    st.header("Pilih Restoran")
    restaurant_names = restaurants['name'].tolist()
    selected_name = st.selectbox("Nama Restoran", restaurant_names)
    selected_restaurant = restaurants[restaurants['name'] == selected_name].iloc[0]
    
    st.image(selected_restaurant['pictureId'])
    st.subheader(selected_restaurant['name'])
    st.write(f"Lokasi: {selected_restaurant['city']}")
    st.write(f"Rating: {selected_restaurant['rating']}")
    st.write(selected_restaurant['description'])
    
    st.subheader("Menu")
    st.write("Makanan:")
    foods = menus[(menus['restaurant_id'] == selected_restaurant['id']) & (menus['type'] == 'food')]
    for idx, row in foods.iterrows():
        st.write(f"- {row['name']}")
    
    st.write("Minuman:")
    drinks = menus[(menus['restaurant_id'] == selected_restaurant['id']) & (menus['type'] == 'drink')]
    for idx, row in drinks.iterrows():
        st.write(f"- {row['name']}")
    
    if st.button("Edit Restoran"):
        edit_restaurant(selected_restaurant['id'])
    
    if st.button("Hapus Restoran"):
        delete_restaurant(selected_restaurant['id'])

# Fungsi untuk menambahkan restoran baru
def add_restaurant():
    st.header("Tambah Restoran")
    name = st.text_input("Nama")
    description = st.text_area("Deskripsi")
    pictureId = st.text_input("URL Gambar")
    city = st.text_input("Kota")
    rating = st.slider("Rating", 0.0, 5.0, 0.1)
    
    st.subheader("Tambah Menu")
    food_menu = st.text_area("Menu Makanan (pisahkan dengan koma)", "Paket rosemary, Toastie salmon, Bebek crepes")
    drink_menu = st.text_area("Menu Minuman (pisahkan dengan koma)", "Es krim, Sirup, Jus apel")
    
    if st.button("Tambah"):
        conn = sqlite3.connect('restaurants.db')
        c = conn.cursor()
        c.execute('''
        INSERT INTO restaurants (name, description, pictureId, city, rating)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, description, pictureId, city, rating))
        restaurant_id = c.lastrowid
        
        foods = [food.strip() for food in food_menu.split(',')]
        for food in foods:
            c.execute('''
            INSERT INTO menus (restaurant_id, type, name)
            VALUES (?, ?, ?)
            ''', (restaurant_id, 'food', food))
        
        drinks = [drink.strip() for drink in drink_menu.split(',')]
        for drink in drinks:
            c.execute('''
            INSERT INTO menus (restaurant_id, type, name)
            VALUES (?, ?, ?)
            ''', (restaurant_id, 'drink', drink))
        
        conn.commit()
        conn.close()
        
        st.experimental_rerun()

# Fungsi untuk mengedit restoran
def edit_restaurant(restaurant_id):
    st.header("Edit Restoran")
    restaurants, menus = get_data()
    restaurant = restaurants[restaurants['id'] == restaurant_id]
    if not restaurant.empty:
        restaurant = restaurant.iloc[0]
        name = st.text_input("Nama", restaurant['name'])
        description = st.text_area("Deskripsi", restaurant['description'])
        pictureId = st.text_input("URL Gambar", restaurant['pictureId'])
        city = st.text_input("Kota", restaurant['city'])
        rating = st.slider("Rating", 0.0, 5.0, restaurant['rating'])
        
        if st.button("Simpan"):
            conn = sqlite3.connect('restaurants.db')
            c = conn.cursor()
            c.execute('''
            UPDATE restaurants
            SET name = ?, description = ?, pictureId = ?, city = ?, rating = ?
            WHERE id = ?
            ''', (name, description, pictureId, city, rating, restaurant_id))
            conn.commit()
            conn.close()
            st.experimental_rerun()

# Fungsi untuk menghapus restoran
def delete_restaurant(restaurant_id):
    conn = sqlite3.connect('restaurants.db')
    c = conn.cursor()
    c.execute('''
    DELETE FROM restaurants WHERE id = ?
    ''', (restaurant_id,))
    c.execute('''
    DELETE FROM menus WHERE restaurant_id = ?
    ''', (restaurant_id,))
    conn.commit()
    conn.close()
    st.experimental_rerun()

st.sidebar.title("Panel Admin Restoran")
choice = st.sidebar.selectbox("Menu", ["Lihat Restoran", "Tambah Restoran"])

if choice == "Lihat Restoran":
    display_data()

    if 'selected_id' in st.session_state and 'action' in st.session_state:
        if st.session_state.action == "Edit":
            edit_restaurant(st.session_state.selected_id)
        elif st.session_state.action == "Hapus":
            delete_restaurant(st.session_state.selected_id)
            st.experimental_rerun()



elif choice == "Tambah Restoran":
    add_restaurant()