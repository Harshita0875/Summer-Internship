#Q1
t = (1, 2, 3)

result = t * 3

print("Repeated tuple:", result)

#Q2
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = (7, 8, 9)

new_tuple = t1 + t2 + t3

print("Joined tuple:", new_tuple)

#Q3
t = (10, 20, 30, 40, 50)

element = int(input("Enter element to search: "))

if element in t:
    print("Element exists in tuple")
else:
    print("Element does not exist in tuple")

#Q4
t = (12, 5, 30, 8, 25)

total = 0
highest = t[0]
lowest = t[0]

for i in t:
    total = total + i

    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

print("Total:", total)
print("Highest value:", highest)
print("Lowest value:", lowest)

#Q5
n = (3, 14, 7, 22, 9, 41, 18, 5)

result = ()

for i in n:
    if i > 10:
        result = result + (i,)

print("Filtered tuple:", result)

#Q6
s = {"cat", "dog", "bird", "fish"}

count = 0

for i in s:
    count = count + 1

print("Number of elements:", count)

#Q7
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

combined = s1.union(s2)

print("Combined set:", combined)

#Q8
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

common = s1.intersection(s2)

print("Common elements:", common)

#Q9
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

result = s1.union(s2)

print("Elements in either set:", result)