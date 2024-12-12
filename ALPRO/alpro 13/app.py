import streamlit as st
import mysql.connector
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menghubungkan ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='streamlitcontoh',  # Sesuaikan dengan password MySQL Anda
        database='university_library_db',
        port = 3306  # Sesuaikan dengan port MySQL Anda
    )
    return connection

# Fungsi CRUD untuk tabel books
def add_book(title, author, year_published):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books (title, author, year_published) VALUES (%s, %s, %s)', (title, author, year_published))
    connection.commit()
    cursor.close()
    connection.close()

def update_book(book_id, title, author, year_published):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET title = %s, author = %s, year_published = %s WHERE book_id = %s', (title, author, year_published, book_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_book(book_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE book_id = %s', (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi CRUD untuk tabel students
def add_student(nim, name, course):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO students (nim, name, course) VALUES (%s, %s, %s)', (nim, name, course))
    connection.commit()
    cursor.close()
    connection.close()

def update_student(student_id, nim, name, course):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE students SET nim = %s, name = %s, course = %s WHERE student_id = %s', (nim, name, course, student_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_student(student_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi CRUD untuk tabel loans
def add_loan(student_id, book_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO loans (student_id, book_id, loan_date) VALUES (%s, %s, %s)', (student_id, book_id, date.today()))
    cursor.execute('UPDATE books SET available = FALSE WHERE book_id = %s', (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

def return_loan(loan_id, book_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE loans SET return_date = %s WHERE loan_id = %s', (date.today(), loan_id))
    cursor.execute('UPDATE books SET available = TRUE WHERE book_id = %s', (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi untuk mengambil data dari tabel
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students

def get_loans():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('''
        SELECT loans.loan_id, loans.book_id, students.name AS student_name, books.title AS book_title, loans.loan_date, loans.return_date 
        FROM loans 
        JOIN students ON loans.student_id = students.student_id 
        JOIN books ON loans.book_id = books.book_id
    ''')
    loans = cursor.fetchall()
    cursor.close()
    connection.close()
    return loans

# Fungsi untuk pencarian dan filter
def search_books(keyword):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM books WHERE title LIKE %s OR author LIKE %s"
    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

def filter_books_by_year(year):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM books WHERE year_published = %s"
    cursor.execute(query, (year,))
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

# Header aplikasi
st.title('University Library Management System')

# Bagian untuk menambahkan buku baru
with st.container():
    st.header('Add New Book')
    book_title = st.text_input('Book Title')
    book_author = st.text_input('Book Author')
    book_year = st.number_input('Year Published', min_value=1000, max_value=date.today().year)
    if st.button('Add Book'):
        if book_title and book_author and book_year:
            add_book(book_title, book_author, book_year)
            st.success(f'Book "{book_title}" added successfully!')
        else:
            st.error('Please enter book title, author, and year published.')

# Bagian untuk mendaftarkan mahasiswa baru
with st.container():
    st.header('Register New Student')
    student_nim = st.text_input('NIM')
    student_name = st.text_input('Student Name')
    student_course = st.text_input('Course')
    if st.button('Register Student'):
        if student_nim and student_name and student_course:
            add_student(student_nim, student_name, student_course)
            st.success(f'Student "{student_name}" registered successfully!')
        else:
            st.error('Please enter NIM, name, and course.')

# Bagian untuk peminjaman buku
with st.container():
    st.header('Loan Book')
    students = get_students()
    books = get_books()
    student_options = {student['name']: student['student_id'] for student in students}
    book_options = {book['title']: book['book_id'] for book in books if book['available']}
    selected_student = st.selectbox('Select Student', list(student_options.keys()))
    selected_book = st.selectbox('Select Book', list(book_options.keys()))
    if st.button('Loan Book'):
        if selected_student and selected_book:
            add_loan(student_options[selected_student], book_options[selected_book])
            st.success(f'Book "{selected_book}" loaned to "{selected_student}" successfully!')
        else:
            st.error('Please select a student and a book.')

# Bagian untuk pengembalian buku
with st.container():
    st.header('Return Book')
    loans = get_loans()
    loan_options = {f"{loan['student_name']} - {loan['book_title']} (Loaned on {loan['loan_date']})": loan['loan_id'] for loan in loans if loan['return_date'] is None}
    selected_loan = st.selectbox('Select Loan to Return', list(loan_options.keys()))
    if st.button('Return Book'):
        if selected_loan:
            loan_id = loan_options[selected_loan]
            book_id = next(loan['book_id'] for loan in loans if loan['loan_id'] == loan_id)
            return_loan(loan_id, book_id)
            st.success(f'Book returned successfully!')
        else:
            st.error('Please select a loan to return.')

# Bagian untuk pencarian buku
with st.container():
    st.header('Search Books')
    keyword = st.text_input('Enter keyword to search by title or author')
    if keyword:
        search_result = search_books(keyword)
        st.write(search_result)

# Bagian untuk memfilter buku berdasarkan tahun terbit
with st.container():
    st.header('Filter Books by Year')
    year_filter = st.number_input('Enter year to filter books', min_value=1000, max_value=date.today().year, step=1)
    if st.button('Filter Books'):
        if year_filter:
            filter_result = filter_books_by_year(year_filter)
            st.write(filter_result)

# Menampilkan daftar buku
with st.container():
    st.header('Books List')
    books = get_books()
    books_df = pd.DataFrame(books)  # Mengonversi hasil menjadi DataFrame
    st.dataframe(books_df)  # Menampilkan DataFrame dalam tabel interaktif
    
# Menampilkan daftar mahasiswa
with st.container():
    st.header('Students List')
    students = get_students()
    students_df = pd.DataFrame(students)
    st.dataframe(students_df)
# Menampilkan daftar peminjaman
with st.container():
    st.header('Loans List')
    loans = get_loans()
    loans_df = pd.DataFrame(loans)
    st.dataframe(loans_df)
# Visualisasi data buku berdasarkan tahun terbit
with st.container():
    st.header('Books Published per Year')
    books_df = pd.DataFrame(books)
    books_per_year = books_df['year_published'].value_counts().sort_index()

    fig, ax = plt.subplots()
    books_per_year.plot(kind='bar', ax=ax)
    ax.set_xlabel("Year Published")
    ax.set_ylabel("Number of Books")
    ax.set_title("Number of Books Published per Year")
    st.pyplot(fig)
