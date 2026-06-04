import pandas as pd
df1=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["A","B","C"],
    "Age":[19,24,21]
},index=[1,2,3])
df2=pd.DataFrame({
    "ID":[1,7,3],
    "Marks":[26,86,90]
},index=[1,2,3])
print("df1:\n",df1)
print("df2:\n",df2)

#Perform an inner merge on this common column and display the resulting DataFrame.
res=df1.merge(df2,on="ID",how="inner")
print("Inner join:\n",res)

#Perform a left join of df1 and df2 on the 'ID' column. Explain how missing values are handled in the resulting DataFrame. Right Join and Index-Based Join.
res1=df1.merge(df2,on="ID",how="left")
print("Left join\n",res1)
df1_index = df1.set_index("ID")
df2_index = df2.set_index("ID")

index_join = df1_index.join(df2_index, how="left")

print("\nIndex-Based Join:")
print(index_join)

#Perform a right join using pd.merge() on a common column, then perform a join using df.join() based on the index. Compare the results. Merging with Multiple Keys.
res2=pd.merge(df1,df2,on="ID",how="right")
print("\nRight Join using pd.merge():")
print(res2)