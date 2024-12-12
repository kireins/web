import streamlit as st
import mysql.connector

# Menghubungkan ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # sesuaikan dengan password MySQL Anda
        database='test_db',
        port='3308'
    )
    return connection

# Fungsi untuk mengambil data dari database
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

# Menampilkan data di Streamlit
st.title('User Data from MySQL Database')
users = get_users()
if users:
    st.write(users)
else:
    st.write('No data found.')

# Menambahkan data ke database
def add_user(name, age):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, age))
    connection.commit()
    cursor.close()
    connection.close()

# Form untuk menambahkan user baru
st.header('Add New User')
name = st.text_input('Name')
age = st.number_input('Age', min_value=1, max_value=120)
if st.button('Add User'):
    add_user(name, age)
    st.success(f'User {name} added successfully!')
    users = get_users()
    st.write(users)