#Q1
#Dictionary
name=input("Enter your name:")
cl=input("Enter your class:")
eng=input("Enter English marks:")
math=input("Enter Maths marks:")
sci=input("Enter Science marks:")
sst=input("Enter SST marks:")
comp=input("Enter computer marks:")
total=int(math)+int(sci)+int(eng)+int(sst)+int(comp)
perc=(int(total)/500)*100
print("Name:", name)
print("Class:", cl)
print("Total Marks:", total)
print("Percentage:", perc)
dict1={"name": name, "class": cl, "total_marks": total, "percentage": perc}
print(dict1)
print(dict1["class"])

#Tuples
tuple1=(name, cl, total, perc)
print(tuple1)
tuple2=("John", "10th", 450, 90.0)
print(tuple2)
tuple3=tuple1+tuple2
print(tuple3)
print(tuple3[::-1])
print(len(tuple3))

#Sets
s1={"apple", "banana", "cherry"}
s2={1,True,3.14}
s=s1.union(s2)
print(s)
s2.add("orange")
print(s2)

#Q2
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if(b==0):
        return "Not allowed"
    else:
        return a/b
    
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))

print("Addition:",add(num1,num2))
print("Subtraction:",sub(num1,num2))
print("Multiplication:",mult(num1,num2))
print("Division:",div(num1,num2))

#Q3
def palin(s):
    rev=s[-1::-1]
    if(s==rev):
        return "Palindrome"
    else:
        return "Not a palindrome"
    
num=input("Enter any string:")
palin(num)