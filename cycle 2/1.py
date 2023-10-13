
print("JAYAMOL REMESAN")
print("--SJC22MCA-2031--")
print("--20MCA241--DATA SCIENCE LAB--")

import numpy as np
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))
num_depth = int(input("Enter the depth: "))
dtype = np.float32
my_3d_array = np.zeros((num_rows, num_columns, num_depth), dtype=dtype)
for i in range(num_rows):
    for j in range(num_columns):
        for k in range(num_depth):
            value = float(input(f"Enter value for element ({i}, {j}, {k}): "))
            my_3d_array[i, j, k] = value
print("Your 3D array:")
print(my_3d_array)


