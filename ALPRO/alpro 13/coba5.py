import streamlit as st
import mysql.connector
from datetime import date

# Menghubungkan ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Sesuaikan dengan password MySQL Anda
        database='university_library_db',
        port='3308'
    )
    return connection

# Fungsi untuk menambahkan buku baru
def add_book(title, author, year_published):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books (title, author, year_published) VALUES (%s, %s, %s)', (title, author, year_published))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi untuk mendaftarkan mahasiswa baru
def add_student(nim, name, course):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO students (nim, name, course) VALUES (%s, %s, %s)', (nim, name, course))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi untuk menambah peminjaman baru
def add_loan(student_id, book_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO loans (student_id, book_id, loan_date) VALUES (%s, %s, %s)', (student_id, book_id, date.today()))
    cursor.execute('UPDATE books SET available = FALSE WHERE book_id = %s', (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi untuk mengembalikan buku
def return_loan(loan_id, book_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('UPDATE loans SET return_date = %s WHERE loan_id = %s', (date.today(), loan_id))
    cursor.execute('UPDATE books SET available = TRUE WHERE book_id = %s', (book_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Fungsi untuk mengambil semua buku
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    cursor.close()
    connection.close()
    return books

# Fungsi untuk mengambil semua mahasiswa
def get_students():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students

# Fungsi untuk mengambil semua peminjaman
def get_loans():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT loans.loan_id, loans.book_id, students.name AS student_name, books.title AS book_title, loans.loan_date, loans.return_date FROM loans JOIN students ON loans.student_id = students.student_id JOIN books ON loans.book_id = books.book_id')
    loans = cursor.fetchall()
    cursor.close()
    connection.close()
    return loans

# Header aplikasi
st.title('University Library Management System')

# Bagian untuk menambahkan buku baru
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

# Menampilkan daftar buku
st.header('Books List')
books = get_books()
st.write(books)

# Menampilkan daftar mahasiswa
st.header('Students List')
students = get_students()
st.write(students)

# Menampilkan daftar peminjaman
st.header('Loans List')
loans = get_loans()
st.write(loans)
