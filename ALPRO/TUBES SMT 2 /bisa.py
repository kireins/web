import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie 
import requests 


# Fungsi untuk mengambil data dari SQLite
def get_data():
    conn = sqlite3.connect('tasks.db')
    tasks = pd.read_sql_query('SELECT * FROM tasks', conn)
    conn.close()
    return tasks

# Fungsi untuk menampilkan data tugas
def display_data():
    tasks = get_data()

    col1,col2 = st.columns(2,gap="small")

    with col1:
        st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=150,
        width=150,
        key=None,
        )

    with col2:
        st.title("Taskie",)
        st.write("Welcome to :violet[_Taskie!_] track your team!")
    st.header('', divider='blue')
    st.dataframe(tasks)

    # Visualisasi data
    st.header("Visualisasi Status Tugas")
    visualize_status(tasks)

    selected_id = st.text_input("Masukkan ID Tugas untuk Edit/Hapus")
    action = st.selectbox("Aksi", ["Lihat", "Edit", "Hapus"])

    if st.button("Lanjutkan"):
        if selected_id:
            st.session_state.selected_id = selected_id
            st.session_state.action = action
            if action == "Lihat":
                view_task(selected_id)
            elif action == "Edit":
                edit_task(selected_id)
            elif action == "Hapus":
                delete_task(selected_id)
                st.experimental_rerun()
        else:
            st.error("ID Tugas tidak boleh kosong.")

# Fungsi untuk visualisasi status tugas
def visualize_status(tasks):
    status_counts = tasks['status'].value_counts().reset_index()
    status_counts.columns = ['status', 'count']
    fig = px.bar(status_counts, x='status', y='count', title="Distribusi Status Tugas", labels={'count': 'Jumlah'}, color='status',
                 color_discrete_map={
                     "Pending": "#911c65",
                     "In Progress": "#f37fa3",
                     "Completed": "#ebecb1"
                 })    
    st.plotly_chart(fig)
 

# Fungsi untuk melihat detail tugas
def view_task(task_id):
    tasks = get_data()
    task = tasks[tasks['id'] == task_id]
    if not task.empty:
        st.write(task)
    else:
        st.error("Tugas dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menambahkan tugas baru
def add_task():
    st.header("Tambah Tugas")
    id = st.text_input("ID Siswa")
    name = st.text_input("Nama Siswa")
    task = st.text_area("Tugas")
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    time = st.text_input("Waktu")
    location = st.text_input("Lokasi")

    if st.button("Tambah"):
        if id and name and task and time and location:
            # st.session_state.id = id
            # st.session_state.task = task
            # st.session_state.time = time
            # st.session_state.location = location  # Ensure required fields are not empty
            conn = sqlite3.connect('tasks.db')
            c = conn.cursor()
            c.execute('''
            INSERT INTO tasks (id, name, task, status, time, location)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (id, name, task, status, time, location))
            conn.commit()
            conn.close()
            st.write("Debug Info: Data Saved Successfully")
            st.success("Tugas berhasil ditambahkan!")
            st.rerun()
        else:
            st.error("Semua kolom harus diisi.")

# Fungsi untuk mengedit tugas
def edit_task(task_id):
    tasks = get_data()
    task = tasks[tasks['id'] == task_id]
    if not task.empty:
        task = task.iloc[0]
        name = st.text_input("Nama Siswa", task['name'])
        task_text = st.text_input("Tugas", task['task'])
        status = st.selectbox("Status", ["Pending", "In Progress", "Completed"], index=["Pending", "In Progress", "Completed"].index(task['status']))
        time = st.text_input("Waktu", task['time'])
        location = st.text_input("Lokasi", task['location'])

         # Debug: Print input values before saving
        st.write("Debug Info: Input Values Before Saving")
        st.write(f"Name: {name}, task: {name}, status: {status}, time: {time}, location: {location}")


        if st.button("Simpan"):
            st.write("Debug Info: Save Button Clicked")

            if name and task_text and time and location:
                # st.session_state.id = id
                # st.session_state.task = task
                # st.session_state.time = time
                # st.session_state.location = location   # Ensure required fields are not empty
                conn = sqlite3.connect('tasks.db')
                c = conn.cursor()
                c.execute('''
                UPDATE tasks
                SET name = ?, task = ?, status = ?, time = ?, location = ?
                WHERE id = ?
                ''', (name, task_text, status, time, location, task_id))
                conn.commit()
                conn.close()
                st.write("Debug Info: Data Saved Successfully")
                st.success("Tugas berhasil diperbarui!")
                st.rerun()
            else:
                st.error("Semua kolom harus diisi.")
    else:
        st.error("Tugas dengan ID tersebut tidak ditemukan.")

# Fungsi untuk menghapus tugas
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''
    DELETE FROM tasks WHERE id = ?
    ''', (task_id,))
    conn.commit()
    conn.close()
    st.success("Tugas berhasil dihapus!")
    st.experimental_rerun()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://lottie.host/08c09993-acce-4c7c-89df-21477531f2ab/gFIcYGIc8b.json")


st.sidebar.title("Task Manager Web")
choice = st.sidebar.selectbox("Menu", ["Lihat Tugas", "Tambah Tugas"])

if choice == "Lihat Tugas":
    display_data()
elif choice == "Tambah Tugas":
    add_task()
