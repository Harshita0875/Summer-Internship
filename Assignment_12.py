import pandas as pd
import numpy as np

#Q1
arr= np.array([1,2,3,4,5,6,7,8])
#1D to 2D
arr2d=arr.reshape(2,4)
print(arr2d)

#Array attributes
print("Shape: ",arr2d.shape)
print("Size:",arr2d.size)
print("Data type:",arr2d.dtype)
print("Dimension:",arr2d.ndim)
print("Item size:",arr2d.itemsize)

#3X3 array of all 9
arr3=np.full((3,3),9)
print("3X3 array of all 9: ", arr3)

#evenly spaced between 25-125
arr4=np.linspace(25,125,10)
print("Evenly spaced array: \n", arr4)

#list to array
list=[1,2,3,4,5]
arr5=np.array(list)
print("Array from list: ", arr5)

#Reverse array
arr6=np.array([1,2,3,4,5,6])
print("Reversed array:-", arr6[::-1])

#4x4x3
arr7=np.random.randint(0,10,(4,4,3))
print("4x4x3 array: \n", arr7)
print("Value at index at second set first row last column:",arr7[1,0,2])

#4X4 array and extract odd rows and even columns
arr8= np.random.randint(0,10,(4,4))
print("4X4 array: \n",arr8)
print("Odd rows and even columns:\n",arr8[::2,1::2])

#Slice firse 2 rows and first 2 columns of second set of a 4x4x3
print("First 2 rows and first 2 columns of second set of a 4x4x3:\n",arr7[1,:2,:2])

#replace odd numbers with -1 using iteration
arr9=np.array([[23,56,78,93],[71,81,13,24]])
for i in range(arr9.shape[0]):
    for j in range(arr9.shape[1]):
        if arr9[i,j]%2!=0:
            arr9[i,j]=-1

print("Array with odd numbers replaced by -1:\n",arr9)

#indeces of non zero elements
import numpy as np

arr10 = np.array([1, 0, 2, 0, 3, 0, 4])

print("Indices of non-zero elements:", np.nonzero(arr10)[0])

#Addition of two arrays
print()
arr11=np.array([15,20,25])
arr12=np.array([10,40,37])
arr13=arr11+arr12
print("Addition of two arrays:", arr13)
arr14=np.multiply(arr11,arr12)
print("Multiplication of two arrays:", arr14)
arr15=arr11-arr12
print("Subtraction of two arrays:", arr15)
arr16=np.dot(arr11,arr12)
print("Dot product of two arrays:",arr16)

