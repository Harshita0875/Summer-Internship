import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Q1
a1=np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
a1[np.isnan(a1)]=0
print(a1)

#Q2
a2=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
a2_transposed=np.transpose(a2,(1,0,2))
print(a2)
print()
print(a2_transposed)

#Q3
#replace nan with avg
a3=np.array([[6, -8, 73, -110], [np.nan, -8, 0, 94]])
a3[np.isnan(a3)]=np.nanmean(a3)
print(a3)

#Q4
a4=np.array([[6,-8, 73, -110], [-23, -8, 0, 94]])
a4[a4<0]=0
print(a4)

#Q5
arr1 = np.array([
    [3, 3],
    [5, 6]
])

arr2 = np.array([
    [1, 0],
    [7, 2]
])

mean=np.mean([arr1,arr2],axis=0)
print("Mean of the 2d arrays:")
print(mean)
median=np.median([arr1,arr2],axis=0)
print("Median of the 2d arrays:")
print(median)
mode = stats.mode([arr1, arr2], axis=0)
print("Mode of the 2d arrays:")
print( mode.mode)

#Q6solve using linalg x - 2y + 3z = 9 -x + 3y - z = -6 2x - 5y + 5z = 17
A = np.array([[1, -2, 3], [-1, 3, -1], [2, -5, 5]])
B = np.array([9, -6, 17])
solution = np.linalg.solve(A, B)
print("Solution (x, y, z):", solution)

semesters = ["Sem 3", "Sem 4"]
marks = [1021, 980]

#Bar chart
plt.figure(figsize=(6,4))
plt.bar(semesters, marks, color=['blue', 'orange'])

plt.title("Semester Marks Comparison", fontsize=14, fontweight='bold')
plt.xlabel("Semester")
plt.ylabel("Marks (out of 1200)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

#pie chart
plt.pie(marks, labels=semesters, autopct='%1.1f%%', startangle=90)

plt.title("Marks Distribution by Semester")
plt.show()

