# PySpark Employee Analysis Using RDD

This project demonstrates PySpark RDD operations on an employee dataset.

## Operations Performed

1. Read CSV into RDD
2. Sort employees by salary (descending)
3. Calculate department-wise total salary
4. Save top 3 highest-paid employees to a file

---

## Dataset

employee_data.csv


id,name,department,salary
1,Amit,IT,55000
2,Rahul,HR,40000
3,Neha,IT,65000
4,Priya,Finance,70000
5,Karan,IT,50000
6,Simran,HR,45000
7,Rohit,Finance,60000


---

## Build Docker Image


docker build -t employee-rdd .

---

## Run Container


docker run --rm employee-rdd


---

## Output

Department Salary Totals


IT: 170000
HR: 85000
Finance: 130000


Top 3 Employees


4,Priya,Finance,70000
3,Neha,IT,65000
7,Rohit,Finance,60000


## GitHub Repository


git init
git add .
git commit -m "Initial Commit"

git branch -M main

git remote add origin https://github.com/<username>/pyspark-rdd-employee.git

git push -u origin main

