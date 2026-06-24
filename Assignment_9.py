import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Q1
#Email Validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "john123@gmail.com"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

#Phone Number Validation
pattern = r'^[6-9]\d{9}$'
mobile = "9876543210"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

#Name /String Validation
pattern = r'^[A-Za-z ]+$'
name = "Rahul Sharma"

if re.match(pattern, name):
    print("Valid Name")
else:
    print("Invalid Name")

#Password Validation
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$'
password = "Rahul@123"

if re.match(pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

#Q2
data = {'Date': ['2026-06-01', '2026-06-02']}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

print(df)

df['Date'] = pd.to_datetime(df['Date'])
data = {'Date': ['2026-06-01', '2026-06-02']}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

print(df)
df['Weekday'] = df['Date'].dt.day_name()
print(df)

df['Month_Name'] = df['Date'].dt.month_name()
print(df)

#Q3
df = pd.read_csv("sales_data.csv")
print(df.head())
print(df.info())

#check for missing values
print(df.isnull().sum())

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])

#Check duplicate records and drop them
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

#category wise sale
category_sales = df.groupby(
    'Product_Category'
)['Sales_Amount'].sum()

print(category_sales)
category_sales.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Sales by Category")
plt.ylabel("")
plt.show()

#Region wise sale
region_sales = df.groupby('Region')['Sales_Amount'].sum()
print(region_sales)


region_sales.plot(kind='bar')
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales Amount")
plt.show()