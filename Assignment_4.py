#Q1
def maximum(*num):
     max=num[0]
     for n in num:
          if n>max:
               max=n
     return max
 
print("Maximum:",maximum(25,26,19,402,93,200))

#Q2
def distinct(l):
    new_l=[]
    for item in l:
        if item not in new_l:
            new_l.append(item)
    return new_l
    
numbers=[1,45,1,45,38,54]
print(distinct(numbers))

#Q3
def mult_list(l1):
    result=1
    for num in l1:
        result*=num
    return result
lst=[2,3,4]
print(mult_list(lst))
    
#Q4
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(6))

#Q5
def reverse(s):
    rev=s[-1::-1]
    return rev
str1=input("Enter a string:")
print(reverse(str1))

#Q6
def check_range(n,a,b):
    if n>=a and n<=b:
        return "In range"
    else:        return "Out of range"

lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
num=int(input("Enter a number:"))

print(check_range(num, lower, upper))

#Q7
def even(l):
    even_num=[]
    for num in l:
        if num%2==0:
            even_num.append(num)
    return even_num

numbers=[1,2,3,4,5,6,7,8,9]
print(even(numbers))

#Q8
def check_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return "Not a prime number"
        return "Prime number"
    else:
        return "Not a prime number"
    
num=int(input("Enter a number:"))
print(check_prime(num))

#Q9
def count(s):
    upper=0
    lower=0
    for char in s:
        if char.isupper():
            upper+=1
        elif char.islower():
            lower+=1
    return upper, lower
str1=input("Enter a string:")
upper_count, lower_count=count(str1)
print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)

#Q10
import csv
data=[["Name", "Age", "City"], ["Alice", 30, "New York"], ["Bob", 25, "Los Angeles"]]
with open('data.csv','w') as file:
    writer=csv.writer(file)
    for row in data:
        writer.writerow(row)

with open('data.csv','a') as file:
    writer=csv.writer(file)
    writer.writerow(["Charlie", 35, "Chicago"])

with open('data.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
