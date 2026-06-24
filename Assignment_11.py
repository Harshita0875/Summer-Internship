#Q1
import numpy as np
import pandas as pd
from scipy import stats

arr1 = np.array([1, 2, 3])

arr2 = np.array([
    [4, 5, 6],
    [7, 8, 9]
])

result = np.vstack((arr1, arr2))

print(result)

#Q2
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

flat = arr.flatten()

print(flat)

#Q3
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[::-1])

#Q4
#Q4
arr = np.array([[10, 25, 5, 40, 15],[20,30,45,69,67]])

print("Maximum value:", arr.max())
print("Minimum value:", arr.min())

rows, cols = arr.shape

print("Rows:", rows)
print("Columns:", cols)

for row in arr:
    for element in row:
        print(element, end=" ")

print("\nSpecific element:", arr[0, 1])

#Sum in 2D array
total = 0

for row in arr:
    for element in row:
        total += element

print("Sum =", total)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#Q5
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

for i in arr:
    for j in i:
        for k in j:
            print(k, end=" ")
print("\n")
#using nditer
for x in np.nditer(arr):
    print(x, end=" ")

#Q6
#Q6
arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7, 8, 9],
                 [1, 2, 3]])

# Combine arrays
combined = np.concatenate((arr1, arr2))

print("Combined Array:")
print(combined)

# Mean
mean_value = np.mean(combined)

# Median
median_value = np.median(combined)

# Mode
mode_value = stats.mode(combined, axis=None, keepdims=False)

print("\nMean =", mean_value)
print("Median =", median_value)
print("Mode =", mode_value.mode)

avg = (arr1 + arr2) / 2

print("Average Array:")
print(avg)
