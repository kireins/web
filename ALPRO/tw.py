import numpy as np

# Create a 1D NumPy array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Create a 2D NumPy array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(array_2d)

# Accessing elements
print("\nAccessing elements:")
print("Element at index (0, 1) in 2D array:", array_2d[0, 1])

# Array operations
print("\nArray operations:")
# Element-wise addition
addition_result = array_1d + 10
print("Adding 10 to each element in the 1D array:", addition_result)

# Element-wise multiplication
multiplication_result = array_1d * 2
print("Multiplying each element in the 1D array by 2:", multiplication_result)

# Dot product
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])
dot_product = np.dot(array_1, array_2)
print("Dot product of arrays:", dot_product)

# Matrix multiplication
matrix_1 = np.array([[1, 2], [3, 4]])
matrix_2 = np.array([[5, 6], [7, 8]])
matrix_multiplication = np.matmul(matrix_1, matrix_2)
print("\nMatrix multiplication:")
print(matrix_multiplication)
