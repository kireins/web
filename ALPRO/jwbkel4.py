# import numpy as np

# def Obe(matrix):
#     andi_matrix = np.copy(matrix)
#     num_rows, num_cols = andi_matrix.shape
#     lead = 0

#     for r in range(num_rows):
#         if lead >= num_cols:
#             break
#         i = r
#         while andi_matrix[i][lead] == 0:
#             i += 1
#             if i == num_rows:
#                 i = r
#                 lead += 1
#                 if num_cols == lead:
#                     return andi_matrix
#             andi_matrix[[r,i]] = andi_matrix[[i,r]]

#             lv = andi_matrix[r][lead]
#             andi_matrix[r] = andi_matrix[r] / lv
#             for i in range(num_rows):
#                 if i != r:
#                     lv = andi_matrix[i][lead]
#                     andi_matrix[i] -= lv * andi_matrix[r]
#                     lead += 1

#                 return andi_matrix
            
# matrix_andi = np.array([[1., 2., 3.],
#                         [4., 5., 6.,],
#                         [7., 8., 9.]])

# print("Matriks awal:")
# print(matrix_andi)

# obe_matrix = Obe(matrix_andi)

# print("\nMatriks dalam bentuk echelon:")
# print(matrix_andi)

# def inverse():
#     determinan = np.linalg.det(matrix_andi)
#     print("Determinan matriks Andi:", determinan)
    
#     if determinan != 0:
#         invers_matrix = np.linalg.inv(matrix_andi)
#         print("\nInvers matriks Andi:")
#         print(invers_matrix)
#     else:
#         print("\nMatriks tidak memiliki invers karena determinannya nol.")   


# # inverse()
# import numpy as np

# # Define the matrix
# A = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# # Function to perform row echelon form (REF)
# def ref(A):
#   """
#   Reduces a matrix to row echelon form (REF).

#   Args:
#       A: A numpy array representing the matrix.

#   Returns:
#       A numpy array representing the matrix in row echelon form.
#   """
#   n = A.shape[0]
#   for i in range(n):
#     # Find the first non-zero element in the current column (i)
#     if A[i, i] == 0:
#       # Swap rows if the diagonal element is zero
#       j = i + 1
#       while j < n and A[j, i] == 0:
#         j += 1
#       if j < n:
#         A[[i, j]] = A[[j, i]]
#     # Normalize the pivot row (i) to have a leading 1
#     if A[i, i] != 1:
#       A[i] /= A[i, i]
#     # Eliminate lower triangular elements
#     for j in range(i + 1, n):
#       if A[j, i] != 0:
#         factor = A[j, i]
#         A[j] -= factor * A[i]
#   return A

# # Get the row echelon form
# A_ref = ref(A.copy())
# print("Row echelon form:")
# print(A_ref)

# # Calculate the determinant using elementary row operations
# def det_ref(A):
#   """
#   Calculates the determinant of a matrix in row echelon form (REF).

#   Args:
#       A: A numpy array representing the matrix in REF.

#   Returns:
#       The determinant of the matrix.
#   """
#   n = A.shape[0]
#   det = 1
#   for i in range(n):
#     det *= A[i, i]
#   return det

# # Calculate the determinant
# det = det_ref(A_ref)
# print("Determinant:", det)

# # Calculate the inverse using elementary row operations
# def inv_ref(A):
#   """
#   Calculates the inverse of a matrix in row echelon form (REF).

#   Args:
#       A: A numpy array representing the matrix in REF.

#   Returns:
#       The inverse of the matrix.
#   """
#   n = A.shape[0]
#   # Create an identity matrix with the same size as A
#   i = np.eye(n)

#   # Perform the same row operations on I as on A to get A^-1
#   for i in range(n):
#     if A[i, i] != 1:
#       # Invert the pivot row in both A and I
#       factor = 1 / A[i, i]
#       A[i] *= factor
#       I[i] *= factor
#     for j in range(i + 1, n):
#       if A[j, i] != 0:
#         factor = A[j, i]
#         # Subtract a multiple of the pivot row from the current row in both A and I
#         A[j] -= factor * A[i]
#         I[j] -= factor * I[i]
#   return I

# # Calculate the inverse
# A_inv = inv_ref(A_ref.copy())
# print("Inverse:")
# print(A_inv)
# import numpy as np

# def Obe(matrix):
#     mat = np.copy(matrix)
#     num_rows, num_cols = mat.shape
#     lead = 0
#     steps = []
    
#     for r in range(num_rows):
#         if lead >= num_cols:
#             break
#         i = r
#         while mat[i][lead] == 0:
#             i += 1
#             if i == num_rows:
#                 i = r
#                 lead += 1
#                 if num_cols == lead:
#                     return mat, steps
#         mat[[r, i]] = mat[[i, r]]
#         steps.append(np.copy(mat))
        
#         lv = mat[r][lead]
#         mat[r] = mat[r] / lv
#         for i in range(num_rows):
#             if i != r:
#                 lv = mat[i][lead]
#                 mat[i] -= lv * mat[r]
#         lead += 1
#     return mat, steps

# def determinant(matrix):
#     mat, _ = Obe(matrix)
#     det = 1
#     num_rows = len(mat)
#     for i in range(num_rows):
#         det *= mat[i][i]
#     return det

# def inverse(matrix):
#     mat, steps = Obe(matrix)
#     num_rows = len(mat)
#     invers = np.zeros_like(mat, dtype=float)
#     for i in range(num_rows):
#         invers[i] = steps[-1][i][num_rows:]
#     return invers

# andi_matrix = np.array([[1, 2, 3],
#                         [4, 5, 6],
#                         [7, 8, 9]])


# hitung_obe, steps = Obe(andi_matrix)

# print("\nTahapan merubah matriks ke bentuk OBE:")
# print("Matriks awal:")
# print(andi_matrix)
# for i, step in enumerate(steps):
#     print(f"Langkah {i+1}:")
#     print(step)

# # determinan = determinant(andi_matrix)

# determinan = np.linalg.det(andi_matrix) 
# print("\nDeterminan matriks:", determinan)
# print(int(determinan))

# invers = np.linalg.inv(andi_matrix)
# print("\nInverse matriks:", invers)

# if determinan != 0:
#     invers = inverse(andi_matrix)
#     print("\nInvers matriks:")
#     print(invers)
# else:
#     print("\nMatriks tidak memiliki invers karena determinannya nol.")

# Toko Bunga XYZ
# Program Pengelola Data Harga Bunga

import numpy as np

# Membuat NumPy array untuk menyimpan data jenis bunga dan harganya
data_bunga = np.array([
    ["Mawar", 5],
    ["Lily", 4],
    ["Tulip", 3],
    ["Anggrek", 6],
    ["Melati", 4]
])

def tampilkan_data():
    print("Data bunga yang dijual di toko:")
    for bunga in data_bunga:
        print(f"{bunga[0]}: Rp {bunga[1]}")

def harga_rata_rata():
    rata_rata = np.mean(data_bunga[:, 1].astype(int))
    print(f"Harga rata-rata bunga di toko adalah: Rp {rata_rata}")

def harga_termurah():
    termurah = np.min(data_bunga[:, 1].astype(int))
    print(f"Harga bunga termurah di toko adalah: Rp {termurah}")

def harga_tertinggi():
    tertinggi = np.max(data_bunga[:, 1].astype(int))
    bunga_tertinggi = data_bunga[np.argmax(data_bunga[:, 1].astype(int)), 0]
    print(f"Harga bunga tertinggi di toko adalah: Rp {tertinggi} ({bunga_tertinggi})")

def main():
    while True:
        print("\n== Toko Bunga XYZ ==")
        print("Menu:")
        print("1. Tampilkan data bunga")
        print("2. Harga rata-rata bunga")
        print("3. Harga bunga termurah")
        print("4. Harga bunga tertinggi")
        print("5. Berhenti")
        
        pilihan = input("Masukkan nomor menu yang diinginkan: ")
        
        if pilihan == "1":
            tampilkan_data()
        elif pilihan == "2":
            harga_rata_rata()
        elif pilihan == "3":
            harga_termurah()
        elif pilihan == "4":
            harga_tertinggi()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan nomor menu yang sesuai.")

if __name__ == "__main__":
    main()