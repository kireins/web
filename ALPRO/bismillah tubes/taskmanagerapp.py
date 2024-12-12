# Kelas: SI-47-08
# Kelompok: 04
# Anggota Kelompok:
# 1. Rafi Akbar  Frdaus - 1202213165 
# 2. Muhamad Alvaro Shidiq Faozan - 1202213165 
# 3. Kirei Nazwa Syafira - 1202213165 
# 4. Anisa Fatiimatus Zahro - 1202213165 
 


# Step 1 - Import package yang akan di gunakan
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie 
import requests 

# Step 2 - Hubungkan ke database SQLite3
conn_0804 = sqlite3.connect('tasks.db')
c_0804 = conn_0804.cursor()

# Step 3 - Buat fungsi untuk pull request animasi menggunakan lottie
def load_lottieurl(url: str):
    r_0804 = requests.get(url)
    if r_0804.status_code != 200:
        return None
    return r_0804.json()

lottie_hello_0804 = load_lottieurl("https://lottie.host/72c86b6a-19aa-4613-b29d-21baa560210b/ZxDh53yN1C.json")


# Step 4 - Membuat fungsi untuk mengambil Tasks dari database, menggunakan fetch
def fetch_tasks():
    c_0804.execute('SELECT * FROM tasks')
    return c_0804.fetchall()

#Step 5 - Membuat fungsi untuk mengambil jumlah task student, menggunakan fetch
def fetch_student_task_counts():
    c_0804.execute('''
              SELECT student_name, COUNT(*) as task_count
              FROM tasks
              GROUP BY student_name
              ''')
    return c_0804.fetchall()

#Step 6 - Membuat fungsi untuk mengambil tugas untuk ID siswa tertentu
def fetch_tasks_by_student(student_id):
    c_0804.execute('SELECT * FROM tasks WHERE student_id = ?', (student_id,))
    return c_0804.fetchall()

#Step 7 - Membuat fungsi untuk menambahkan tugas ke database
def add_task(student_id, student_name, task, time, location, status):
    c_0804.execute('''
              INSERT INTO tasks (student_id, student_name, task, time, location, status)
              VALUES (?, ?, ?, ?, ?, ?)
              ''', (student_id, student_name, task, time, location, status))
    conn_0804.commit()

#Step 8 - Membuat fungsi untuk memperbarui tugas dalam database
def update_task(id, student_id, student_name, task, time, location, status):
    c_0804.execute('''
              UPDATE tasks
              SET student_id = ?, student_name = ?, task = ?, time = ?, location = ?, status = ?
              WHERE id = ?
              ''', (student_id, student_name, task, time, location, status, id))
    conn_0804.commit()

# Step 9 - Membuat fungsi untuk menghapus tugas dari database
def delete_task(id):
    c_0804.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn_0804.commit()

# Step 10 - Membuat navigasi di sidebar 
page_0804 = st.sidebar.selectbox('Select Page', ['Welcome', 'Task Overview', 'Edit Task'])

# Step 11 - Membuat navigasi halaman menggunakan perulangan

if page_0804 == 'Welcome':
    col1_0804,col2_0804 = st.columns(2,gap="small")
    with col1_0804:
        st_lottie(
        lottie_hello_0804,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        height=300,
        width=300,
        key=None,
        )

    with col2_0804:
        st.title('Welcome to the Task Manager App!')
    st.header("", divider='violet')
    st.subheader("""
        This application allows you to manage tasks for students.
        :rotating_light: please read the navigation first to help 
        - Use the **Task Overview** page to view and add tasks.
        - Use the **Edit Task** page to update or delete existing tasks.
        - Use the **View Student Record** section in the **Task Overview** page to see tasks of a specific student.
    """)
    st.caption("Navigate to the desired page using the :blue[_sidebar_].")
    

# Step 12 - Membuat Halaman Task Overview Page
elif page_0804 == 'Task Overview':
    st.header('Task Manager - Overview', divider='orange')

    # Step 13 - Membuat Sidebar untuk menambahkan tugas
    st.sidebar.header('Add Task')
    student_id_0804 = st.sidebar.number_input('Student ID', min_value=1)
    student_name_0804 = st.sidebar.text_input('Student Name')
    task_0804 = st.sidebar.text_input('Task')
    time_0804 = st.sidebar.text_input('Time')
    location_0804 = st.sidebar.text_input('Location')
    status_0804 = st.sidebar.selectbox('Status', ['Not Started', 'In Progress', 'Completed'])

    if st.sidebar.button('Add Task'):
        add_task(student_id_0804, student_name_0804, task_0804, time_0804, location_0804, status_0804)
        st.sidebar.success('Task added successfully')

    # Step 14 - Menampilkan tabel tugas
    tasks_0804 = fetch_tasks()
    df_tasks_0804 = pd.DataFrame(tasks_0804, columns=['ID', 'Student ID', 'Student Name', 'Task', 'Time', 'Location', 'Status'])
    st.header('Tasks')
    st.table(df_tasks_0804)

    # Step 15 - Menampilkan tabel jumlah tugas siswa
    student_task_counts_0804 = fetch_student_task_counts()
    df_task_counts_0804 = pd.DataFrame(student_task_counts_0804, columns=['Student Name', 'Task Count'])
    st.header('Student Task Counts')
    st.table(df_task_counts_0804)

    # Step 16 - Menampilkan data visualisasi menggunakan Plotly
    if not df_tasks_0804.empty:          
        fig_0804 = px.bar(df_tasks_0804, x='Student Name', y='ID', color='Status', title='Tasks Status',
                     color_discrete_map={
                     "Not Started": "#FC4100",
                     "In Progress": "#00215E",
                     "Completed": "#FFC55A"
                 })
        st.plotly_chart(fig_0804)

    # Step 17 - Membuat opsi lihat record siswa tertentu
    st.header('View Student Record')
    selected_student_id_0804 = st.number_input('Enter Student ID to view their tasks', min_value=1, step=1)
    if st.button('View Tasks'):
        student_tasks_0804 = fetch_tasks_by_student(selected_student_id_0804)
        if student_tasks_0804:
            df_student_tasks_0804 = pd.DataFrame(student_tasks_0804, columns=['ID', 'Student ID', 'Student Name', 'Task', 'Time', 'Location', 'Status'])
            st.subheader(f'Tasks for Student ID {selected_student_id_0804}')
            st.table(df_student_tasks_0804)
        else:
            st.write(f'No tasks found for Student ID {selected_student_id_0804}')

# Step 18 - Membuat halaman Edit Task untuk mengubah data yang telah ada 
elif page_0804 == 'Edit Task':
    st.title('Task Manager - Edit Task')

    task_id_0804 = st.number_input('Task ID (for Edit/Delete)', min_value=1)
    if task_id_0804:
        c_0804.execute('SELECT * FROM tasks WHERE id = ?', (task_id_0804,))
        task_0804 = c_0804.fetchone()
        if task_0804:
            student_id_0804 = st.number_input('Student ID', min_value=1, value=task_0804[1])
            student_name_0804 = st.text_input('Student Name', value=task_0804[2])
            task_desc_0804 = st.text_input('Task', value=task_0804[3])
            time_0804 = st.text_input('Time', value=task_0804[4])
            location_0804 = st.text_input('Location', value=task_0804[5])
            status_0804 = st.selectbox('Status', ['Not Started', 'In Progress', 'Completed'], index=['Not Started', 'In Progress', 'Completed'].index(task_0804[6]))

            if st.button('Update Task'):
                update_task(task_id_0804, student_id_0804, student_name_0804, task_desc_0804, time_0804, location_0804, status_0804)
                st.success('Task updated successfully')

            if st.button('Delete Task'):
                delete_task(task_id_0804)
                st.success('Task deleted successfully')
        else:
            st.warning('No task found with this ID')
conn_0804.close()
