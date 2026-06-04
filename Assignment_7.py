import pandas as pd
#1
#Series from dictionary
data={"day1":420,"day2":350}
qmarks=pd.Series(data)
print(qmarks)
print(type(qmarks))
#Series from list
dt=[1,2,3]
s_dt=pd.Series(dt)
print(s_dt)
#Access elements of series
print(s_dt[1])
print(qmarks["day2"])

#2
#Create dataframe from lists
data=[
    [1,"Harshita",20],
    [2,"Shreya",19],
    [3,"Rekha",22]
]
df=pd.DataFrame(data,columns=["ID","Name","Age"])
print(df)

#Create dataframe from dictionary
dict={
    "Name":["a","b"],
    "Age":[19,21]
}
df1=pd.DataFrame(dict)
print(df1)

#From list of lists
list_data=[
    ["Mango",100],
    ["Apple",150]
]
df2=pd.DataFrame(list_data,columns=["Fruit","Price"],index=[1,2])
print("\n",df2)

#From list of tuples
list_tuple=[
    ("Meera",19),
    ("Siya",20)
]
df3=pd.DataFrame(list_tuple,columns=["Name","Age"])
print("\n",df3)

#From list of dicts
list_dict=[
    {"Name":"Meera","age":20},
    {"Name":"ABC","age":25}
]
df4=pd.DataFrame(list_dict,index=[1,2])
print("\n",df4)

#3
df=pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[19,35,24],
    "Marks":[98,67,84]
},index=[1,2,3])
print(df)

#Different ways to iterate over rows in Pandas Dataframe 	


#select rows based on condition
print("\nStudents whose age>20:\n",df[df["Age"]>20])

#Select row using iloc
print("\n",df.loc[3])

#Limited rows selection with given column
print("\n",df.loc[0:2,["Name","Marks"]])

#Drop rows from the dataframe based on certain condition applied on a column 
res=df[df["Age"]>20]
print(res)

#Insert row at given position in Pandas Dataframe 

#Create a list from rows in Pandas dataframe 
print("List from Name column:")
lst=df["Name"].tolist()
print(lst)

print("List of all rows:")
row_list=df.values.tolist()
print(row_list)