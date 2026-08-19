# Databricks notebook source

# SELECT / COLUMN OPERATIONS
# Display all columns from the DataFrame.
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/employee_data_500.csv',header=True,inferSchema=True)
df.display()
df.select('*').display()
# Display only emp_id, emp_name, and salary.
df.select('EmpID','FirstName','LastName','salary').show()
from pyspark.sql.functions import col
# Display emp_name and salary with salary increased by 10%.
df.select('FirstName','LastName', (col('salary') * 1.1).alias('UpdatedSalary')).display()

# Create a new column annual_salary.
df.select('annual_salary',col("salary")*12)
# Display employee name and annual salary.
df.select('FirstName','LastName',(col("salary")*12).alias('annual_salary')).display()
# Rename emp_name as employee_name.
df.select('FirstName','LastName').withColumnRenamed('FirstName','employee_name').display()
# Display all rows where the salary is greater than ₹70)
df.select('*').filter(col('salary')>70000).display()
# Drop the manager_id column.
# df.drop(col('manager_id')).display()
# Select employees whose salary is greater than ₹70,000.
df.select('FirstName','LastName','salary').filter(col('salary')>70000).display()
# Select employees whose salary is between ₹60,000 and ₹90,000.
df.select('FirstName','LastName','salary').filter((col('salary')>60000) & (col('salary')<90000)).display()


# COMMAND ----------

# 2. RELATIONAL OPERATORS

# Practice:

# >, <, >=, <=, ==, !=

# Find employees whose salary is greater than 80,000.
df.filter(col('salary')>80000).select('EmpID','salary').display()
# Find employees whose salary is less than or equal to 60,000.
df.filter(col('salary')<60000).select('EmpID','salary').display()
# Find employees whose age is greater than 30.
# df.filter(col("age")>30).select('EmpID','age').display()
# Find employees whose age is exactly 30.
# df.filter(col("age")=30).select('EmpID','age').display()
# Find employees whose department is not IT.
df.filter(col('DepartmentType')!='IT').select('EmpID','DepartmentType')
# Find employees whose salary is not 50,000.
df.filter(col('salary')>50000).select('EmpID','salary').display()
# Find employees whose age is between 25 and 35.
# df.filter(col('age')>25 & col('age')<35).select("EmpID","age").dsiplay()
# Find employees whose salary is greater than 70,000 and age is less than 35.
# df.filter((col('salary')>70000) & (col('age')<35)).select('EmpID','salary','age').show()

# COMMAND ----------

# 3. LOGICAL OPERATORS

# Find employees from IT whose salary is greater than 80,000.
df.filter((col('DepartmentType')=='IT/IS') & (col('salary')>80000)).select('EmpID','DepartmentType','salary').display()
# Find employees from HR whose age is less than 30.
# df.filter(col('DepartmentType="HR") & col('age')<30)).select('EmpID','DepartmentType','salary').display()

# Find employees from either IT or Finance.
df.filter((col('DepartmentType')=='IT/IS') | (col('DepartmentType')=='Sales')).select('EmpID','DepartmentType').display()
# Find employees who are from 6050 AND salary > 70,000.
df.filter((col('LocationCode')==6050) & (col('salary')>70000)).select('EmpID','LocationCode','salary').display()
# Find employees who are from 6050 OR 78789.
df.filter((col('LocationCode')==6050) | (col('LocationCode')==78789)).select('EmpID','LocationCode').display()
# Find employees who are NOT from IT.
df.filter(~(col('DepartmentType')=='IT/IS')).select('EmpID','DepartmentType').display()
# Find employees who are in IT AND are female.
df.filter((col('DepartmentType')=='IT/IS') & (col('GenderCode')=='Female')).select('EmpID','DepartmentType','GenderCode').display()
# Find employees who are either:
# IT employees with salary > 80,000
# OR Finance employees with salary > 65,000.
df.filter(((col('DepartmentType')=='IT/IS') & (col('salary')>80000)) | ((col('DepartmentType')=='Finance') & (col('salary')>65000))).display()

# COMMAND ----------


# 4. MEMBERSHIP OPERATORS
# PySpark equivalent:
# col("dept").isin("Production", "Sales")
df.filter(col('DepartmentType').isin('Prodcution Technician','Sales')).select('EmpID','DepartmentType').show()
# Find employees belonging to "Sales" or ""IT/IS.
df.filter(col('DepartmentType').isin('Sales')|col('DepartmentType').isin('IT/IS')).select('DepartmentType','EmpID').show()
# Find employees belonging to Executive Office, IT/IS, or Area Sales Manager.
df.filter(col('DepartmentType').isin('Executive Office','IT/IS','Area Sales Manager')).select('DepartmentType','EmpID').show()

# Find employees who are NOT from sales or IT/IS.
df.filter(~col('DepartmentType').isin('Sales','IT/IS')).select('DepartmentType','EmpID').show()
# Find employees from 46204,30428 or 80820.
df.filter(col('LocationCode').isin[46204,30428,80820]).select('LocationCode','EmpID').show()
# Find employees whose salary belongs to:
# 50000, 65000, 75000, 90000
df.filter(col('salary').isin(50000,65000,75000,90000)).select('salary','EmpID').show()
# Find employees whose department is NOT in:
#sales,Production Techinician
df.filter(~col('DepartmentType').isin('Sales','Production Technician')).select('DepartmentType','EmpID').show()


# COMMAND ----------

