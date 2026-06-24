#Q1
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

#Q2
str1=input("Enter a string:")
str2=input("Enter another string:")
str3=str1+str2
print("Concatenated String:", str3)
print(str3.lower())
print(str3.upper())
print(str3.title()) 
print(str3.capitalize())
print(str3.casefold())
print(str3.center(50))
print(str3.count('a'))    
print(str3.find('a'))   
print(str3.replace('a', 'x'))
print(str3.swapcase())
print(str3.endswith('x'))
print(str3.isalnum())

#Q3
x=5
x+=10
print(x)
y=20
y-=5
print(y)
y*=2
print(y)
y/=3
print(y)    
x**=3
print(x)
y-=1
y//=2
print(y)

#Q4
if(perc>=60):
    print("Grade A")
elif(perc>=50):
    print("Grade B")    
elif(perc>=40):
    print("Grade C")
elif(perc>=33):
     print("Grade D")
else:
    print("Fail")