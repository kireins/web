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

    st.header("Daftar Restoran")
    st.dataframe(restaurants)

    selected_id = st.text_input("Masukkan ID Restoran untuk Edit/Hapus")
    action = st.selectbox("Aksi", ["Lihat", "Edit", "Hapus"])

    if st.button("Lanjutkan"):
        if selected_id:
            st.session_state.selected_id = selected_id
            st.session_state.action = action
            if action == "Lihat":
                view_restaurant(selected_id)
            elif action == "Edit":
                edit_restaurant(selected_id)
            elif action == "Hapus":
                delete_restaurant(selected_id)
                st.experimental_rerun()
        else:
            st.error("ID Restoran tidak boleh kosong.")

# Fungsi untuk melihat detail restoran
def view_restaurant(restaurant_id):
    restaurants, menus = get_data()
    restaurant = restaurants[restaurants['id'] == restaurant_id]
    if not restaurant.empty:
        st.write(restaurant)
        st.write(menus[menus['restaurant_id'] == restaurant_id])
    else:
        st.error("Restoran dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menambahkan restoran baru
def add_restaurant():
    st.header("Tambah Restoran")
    id = st.text_input("ID")
    name = st.text_input("Nama")
    description = st.text_area("Deskripsi")
    pictureId = st.text_input("URL Gambar")
    city = st.text_input("Kota")
    rating = st.slider("Rating", 0.0, 5.0, 0.1)

    if st.button("Tambah"):
        if id and name and city:  # Ensure required fields are not empty
            conn = sqlite3.connect('restaurants.db')
            c = conn.cursor()
            c.execute('''
            INSERT INTO restaurants (id, name, description, pictureId, city, rating)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (id, name, description, pictureId, city, rating))
            conn.commit()
            conn.close()
            st.success("Restoran berhasil ditambahkan!")
            st.experimental_rerun()
        else:
            st.error("ID, Nama, dan Kota harus diisi.")

# Fungsi untuk mengedit restoran
def edit_restaurant(restaurant_id):
    restaurants, menus = get_data()
    restaurant = restaurants[restaurants['id'] == restaurant_id]
    if not restaurant.empty:
        restaurant = restaurant.iloc[0]
        name = st.text_input("Nama", restaurant['name'])
        description = st.text_area("Deskripsi", restaurant['description'])
        pictureId = st.text_input("URL Gambar", restaurant['pictureId'])
        city = st.text_input("Kota", restaurant['city'])
        rating = st.slider("Rating", 0.0, 5.0, restaurant['rating'])

        # Debug: Print input values before saving
        st.write("Debug Info: Input Values Before Saving")
        st.write(f"Name: {name}, Description: {description}, Picture URL: {pictureId}, City: {city}, Rating: {rating}")

        if st.button("Simpan"):
            # Debug: Confirm button click
            st.write("Debug Info: Save Button Clicked")

            if name and city:  # Ensure required fields are not empty
                conn = sqlite3.connect('restaurants.db')
                c = conn.cursor()
                c.execute('''
                UPDATE restaurants
                SET name = ?, description = ?, pictureId = ?, city = ?, rating = ?
                WHERE id = ?
                ''', (name, description, pictureId, city, rating, restaurant_id))
                conn.commit()
                conn.close()

                # Debug: Confirm data saved
                st.write("Debug Info: Data Saved Successfully")
                st.success("Restoran berhasil diperbarui!")
                st.rerun()
            else:
                st.error("Nama dan Kota harus diisi.")
    else:
        st.error("Restoran dengan ID tersebut tidak ditemukan.")

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
    st.success("Restoran berhasil dihapus!")

st.sidebar.title("Panel Admin Restoran")
choice = st.sidebar.selectbox("Menu", ["Lihat Restoran", "Tambah Restoran"])

if choice == "Lihat Restoran":
    display_data()
elif choice == "Tambah Restoran":
    add_restaurant()
