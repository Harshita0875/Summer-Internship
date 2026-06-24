#Q1
import csv
info=[["Name", "Address", "Mobile number","Email"]]
with open('info.csv','w') as file:
    writer=csv.writer(file)
    for i in range(3):
        name=input("Enter name:")
        address=input("Enter address:")
        mobile=input("Enter mobile number:")
        email=input("Enter email:")
        info.append([name, address, mobile, email])
    writer.writerows(info)

    #Q2
#1
import sqlite3

conn=sqlite3.connect('college.db')

#2
execute="""
CREATE TABLE students(
id integer PRIMARY KEY autoincrement,
name varchar(50),
age integer,
city varchar(50)
)
"""

t="""
CREATE TABLE teachers(
id integer PRIMARY KEY autoincrement,
name varchar(50),
subject varchar(50)
)
"""
# conn.execute(execute)
# conn.execute(t)

#3
insert_sql = """INSERT INTO students(name,age,city) 
VALUES('John Doe',20,'New York'),
('Jane Smith',22,'Los Angeles'),
('Alice Johnson',19,'Chicago')
"""
insert_sql2 = """INSERT INTO teachers(name,subject)
VALUES('Mr. Brown','Math'), 
('Ms. Green','English'), 
('Dr. White','Science')
"""

conn.execute(insert_sql)
conn.execute(insert_sql2)
conn.commit()
conn.close()

#4
import sqlite3
conn=sqlite3.connect('college.db')
print("\n All students:")
slct="""
Select * from students
"""
result=conn.execute(slct)
for row in result:
    print(row)

filt="""
Select * from students where age>20
"""
result=conn.execute(filt)
print("\n Students with age greater than 20:")  
for row in result:
    print(row)

#5
upd="""
Update students set city='San Francisco' where name='John Doe'
"""
conn.execute(upd)
conn.commit()
print("\n Updated students:")
result=conn.execute(slct)
for row in result:
    print(row)

#6
del_sql="""
Delete from students where id=2
"""
conn.execute(del_sql)
conn.commit()
print("\n After deletion:")
result=conn.execute(slct)
for row in result:
    print(row)