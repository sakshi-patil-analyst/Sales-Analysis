import pandas as pd
import mysql.connector

df = pd.read_csv("Superstore Sales.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.columns)

df['Order Date'] = pd.to_datetime(df['Order Date'],format='mixed')
df['Ship Date'] = pd.to_datetime(df['Ship Date'],format='mixed')

print(df.isnull().sum())

df = df.drop_duplicates()

df['Postal Code'] = df['Postal Code'].fillna('0')

print(df.isnull().sum())

total_sales = df['Sales'].sum()
print("Total Sales :",total_sales)

'''df.to_csv("New_Sales.csv",index=False)'''

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sakshi",
    database = "sales_db")

cursor = conn.cursor()

for i , row in df.iterrows():
    sql = """INSERT INTO sales VALUES(%s, %s, %s, %s, %s, %s, %s, %s,
%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values =  tuple(row)
    cursor.execute(sql,values)

conn.commit()
print("Data Inserted Successfully!")

cursor.close()
conn.close()

print("Done!")















































