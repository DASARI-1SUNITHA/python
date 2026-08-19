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

# 5. NULL / MISSING VALUE PRACTICE
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("demo").getOrCreate()
df=spark.read.csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/employee_data.csv',header=True,inferSchema=True)
df.display()
# Modify some rows so that city, salary, or manager_id contains NULL.
# df = df.withColumn('salary',when(col('EmpID').isin(3427,3430),None).otherwise(col('salary')));
# df.display()
# df = df.withColumn('city',when(col('EmpID').isin(3427,3430),None).otherwise(col('city'))); 
# df.display()
# df = df.withColumn('manager_id',when(col('EmpID').isin(3427,3430),None).otherwise(col('manager_id')));
# df.display()
# Find employees where manager_id is NULL.
df1=df.filter(col('manager_id').isNull());
df1.display()
# Find employees where manager_id is NOT NULL.
df2=df.filter(col('manager_id').isNotNull())
df2.display()
# Count the number of NULL values in salary.
df.filter(col('salary').isNull()).count()
# Replace NULL salary with 0.
# df = df.withColumn('salary',when(col('salary').isNull(),0).otherwise(col('salary')))
# # Replace NULL city with "Unknown".
# df = df.withColumn('city',when(col('city').isNull(),'Unknown').otherwise(col('city')))
# # Remove rows where salary is NULL.
# df = df.filter(col('salary').isNotNull()); display(df)
# Remove rows where either salary OR city is NULL.
df.filter(col('salary').isNotNull() & col('city').isNotNull()).display()
# Remove rows where both salary AND city are NULL.
df.filter(col('salary').isNotNull() | col('city').isNotNull()).display()

# COMMAND ----------

# 6. STRING FUNCTIONS
# Practice:upper(), lower(), length(), trim(), substring(), concat(), concat_ws(), split(), regexp_replace(), like/rlike

# Convert employee names to uppercase.
from pyspark.sql.functions import (
    col, upper, lower, length, substring,
    concat, concat_ws, split, regexp_replace,
    trim, count, sum, avg, max, min,lit
)
# Convert employee names to uppercase.
df.select("emp_name", upper(col("emp_name"))).display()

# Convert employee names to lowercase.
df.select("emp_name", lower(col("emp_name"))).display()

# Find the length of every employee name.
df.select("emp_name", length(col("emp_name"))).display()

# Find employees whose name starts with A.
df.filter(col('emp_name').startswith("A")).display()
# Find employees whose name ends with a.
df.filter(col('emp_name').endswith("a")).display()
# Find employees whose name contains "a".
df.filter(col('emp_name').contains("a")).display()
# Extract the first 3 characters of employee names.
df.select("emp_name", substring(col("emp_name"), 1, 3)).display()
# Extract the last 3 characters of employee names.
df.select("emp_name", substring(col("emp_name"),-3,3)).display()

# Concatenate employee name and department.
# Expected format:
# Alice-IT
# Bob-HR
df.select(concat(col('emp_name'),lit("-"),col("dept"))).display()
# Create:
# emp_id_emp_name
# Example:
# 101_Alice
# 102_Bob
df.select(concat_ws('-','emp_id','emp_name')).display()
# Split the skills column.
df.select('emp_name','skills',split(col('skills'),',')).display()
# Replace "Python" with "PySpark" in the skills column.
df.select('emp_name','skills',regexp_replace(col('skills'),lit('Python'),'PySpark')).display()
# Remove spaces from city names using trim().
df.select('city',trim(col('city'))).display()
# Find names having more than 5 characters.
df.filter(length(col('emp_name'))>5).display()
# Find employees whose names match the pattern:%a%
df.filter(col('emp_name').like('%a%')).display()
# Find employees whose names match the pattern:A%
df.filter(col('emp_name').like('A%')).display()
# Find employees whose names contain "e".
df.filter(col("emmp_name").rlike('e')).display()

# COMMAND ----------

# 7. GROUP BY
# Use:groupBy()
# count(), sum(), avg(), min(), max()

# Count employees in each department.
df.groupBy('dept').agg(count("*")).display()
# Find total salary by department.
df.groupBy('dept').agg(sum('salary')).display()
# Find average salary by department.
df.groupBy('dept').agg(avg('salary')).display()
# Find maximum salary by department.
df.groupBy('dept').agg(max('salary')).display()
# Find minimum salary by department.
df.groupBy('dept').agg(min('salary')).display
# Find employee count by city.
df.groupBy('city').agg(count("*")).display()
# Find average age by department.
df.groupBy('dept').agg(avg('salary')).display()
# Find total salary by gender.
df.groupBy('gender').agg(sum('salary')).display()
# Find average salary by department and gender.
df.groupBy('dept','gender').agg(avg('salary')).display()
# Find maximum salary in each city.
df.groupBy('city').agg(max('salary')).display()
# Find minimum salary in each department.
df.groupBy('dept').agg(min('salary')).display()


# COMMAND ----------

# 8. GROUP BY + HAVING:PySpark doesn't use SQL's HAVING keyword directly. Use filter() after aggregation.
from pyspark.sql.functions import count,avg,sum,min,max,col 
# Find departments having more than 2 employees.
df.groupBy('dept').agg(count('*').alias('emp_count')).filter(col('emp_count')>2).display()
# Find departments where average salary is greater than 70,000.
df.groupBy('dept').agg(avg('salary').alias('avg_salary')).filter(col('avg_salary')>70000).display()
# Find departments where total salary is greater than 200,000.
df.groupBy('dept').agg(sum('salary').alias('total_salary')).filter(col('total_salary')>200000).display()

# Find cities having more than 3 employees.
df.groupBy('city').agg(count('*').alias('emp_count')).filter(col('emp_count')>3).display()
# Find departments where maximum salary is greater than 90,000.
df.groupBy('dept').agg(max('salary').alias('max_salary')).filter(col('max_salary')>90000).display()
# Find departments where minimum salary is less than 60,000.
df.groupBy('dept').agg(min('salary').alias('min_salary')).filter(col('min_salary')<60000).display()

# COMMAND ----------

# 9. ORDER BY / SORT
# Sort employees by salary ascending.
df.sort('salary',ascending=True).display()
# Sort employees by salary descending.
df.sort('salary',ascending=False).display()
# Sort employees by age ascending.
df.sort('age',ascending=True).display()
# Sort employees by age descending.
df.sort('age',ascending=False).display()
# Sort employees by department ascending and salary descending.
df.sort(col('dept').asc(),col('salary').desc()).display()
# Sort employees by city ascending and salary ascending.
df.sort(col('city').asc(),col('salary').asc()).display()
# Find the highest-paid employee.
df.sort(col('salary').desc()).limit(1).display()

# Find the lowest-paid employee.
df.sort(col('salary').asc()).limit(1).display()

# Find the top 3 highest-paid employees.
df.sort('salary', ascending=False).limit(3).display()
# Find the 3 youngest employees.
df.sort('age',ascending=True).limit(3).display()
# Sort by salary descending and display only employee name and salary.
df.sort('salary',ascending=False).select('emp_name','salary').display()


# COMMAND ----------

# 10. DISTINCT
# Find unique departments.
df.select('dept').distinct().display()
# Find unique cities.
df.select('city').distinct().display()
# Find unique combinations of department and city.
df.select('dept','city').distinct().display()
# Count the number of unique departments.
df3=df.select('dept').distinct()
display(df3.count())
# Count the number of unique cities.
df4=df.select('city').distinct()
display(df4.count())


# COMMAND ----------

# 11. DATE FUNCTIONS
from pyspark.sql.functions import col, current_date, date_add, date_format, to_date
# Convert hire_date into a proper date type.
df.select('hire_date',to_date(col('hire_date'))).display()
# Extract the year from hire_date.
df.select('hire_date',year(col('hire_date'))).display()
# Extract the month from hire_date.
df.select('hire_date',month(col('hire_date'))).display()
# Extract the day from hire_date.
df.select('hire_date',day(col('hire_date'))).display()

# Display hire date in:dd-MM-yyyy
df.select('hire_date',date_format(col('hire_date'),'dd-MM-yyyy')).display()
# Find employees hired in 2021.
df.select('hire_date',year(col('hire_date'))==2021).display()
# Find employees hired after 2020.
df.select('hire_date',year(col('hire_date'))>2020).display()
# Find employees hired before 2021.
df.select('hire_date',year(col('hire_date'))<2021).display()
# Find employees hired in January.
df.select('hire_date',month(col('hire_date'))==1).display()
# Find employees hired between 2020 and 2022.
df.filter((year(col('hire_date')) >= 2020) & (year(col('hire_date')) <= 2022)).display()
# Add 30 days to hire_date.
df.select('hire_date',date_add(col('hire_date'),30)).display()
# Subtract 10 days from hire_date.
df.select('hire_date',date_sub(col('hire_date'),10)).display()
# Add 3 months to hire_date.
df.select('hire_date',add_months(col('hire_date'),3)).display()
# Calculate how many days each employee has worked from their hire date until today.
df.select('hire_date',datediff(current_date(),col('hire_date'))).display()
# Find employees who have worked for more than 1000 days.
df.select('hire_date',datediff(current_date(),col('hire_date'))>1000).display()
# Find the oldest hire date.
df.select('hire_date',min(col('hire_date'))).display()

# Find the most recent hire date.
df.seelct('hire_date',max(col('hire_date'))).display()


# COMMAND ----------

# 12. CONDITIONAL OPERATIONS:# Practice when() and otherwise().
from pyspark.sql.functions import *
# Create a salary_level column:
# salary >= 90000 → High
# salary >= 70000 → Medium
# otherwise → Low
df.withColumn('salary_level',when(col('salary')>=90000,'high').when(col('salary')>=70000,'Medium').otherwise('low'))
df.display()
# Create an age_group:
# age < 30 → Young
# age between 30 and 35 → Middle
# age > 35 → Senior
df.withColumn('age_group',when(col('age')<30,'Young').when(col('age').between(30,35),'Middle').otherwise('Senior')).display()
# Create:
# salary > 70000 → Eligible
# otherwise → Not Eligible
df.withColumn('bonus',when(col('salary')>70000,'Eligible').otherwise('Not Eligible')).display()
# Give employees a bonus:
# IT → 15%
# HR → 10%
# Finance → 12%
df.withColumn('bonus',when(col('dept')=='IT',col('salary')*0.15).when(col('dept')=='HR',col('salary')*0.10).when(col('dept')=='Finance',col('salary')*0.12).otherwise(col('salary'))).display()

# Create a column:
# age >= 30 → Experienced
# age < 30 → Fresher
df.withColumn('experience',when(col('age')>=30,'Experienced').otherwise('Fresher')).display()


# COMMAND ----------

# 13. JOINS

# Create another DataFrame:
# Perform INNER JOIN between employees and departments.
df1.join(df2,df1.dept==df2.dept,'inner').display()

# Perform LEFT JOIN.
df1.join(df2.dept==df2.dept,'left').display()
# Perform RIGHT JOIN.
df1.join(df2.dept==df2.dept,'right').display()
# Perform FULL OUTER JOIN.
df1.join(df2.dept==df2.dept,'outer').display()
# Perform LEFT SEMI JOIN.
df1.join(df2.dept==df2.dept,'leftsemi').display()
# Perform LEFT ANTI JOIN.
df1.join(df2.dept==df2.dept,'leftanti').display()
# Perform CROSS JOIN.
df1.crossJoin(df2).display()
# Find employees whose department exists in the department table.
df1.join(df2.dept==df2.dept,'leftsemi').display()
# Find employees whose department doesn't exist in the department table.
df1.join(df2.dept==df2.dept,'leftanti').display()

# Find departments that don't have employees.
df2.join(df1.dept==df1.dept,'rightanti').display()
# Display:emp_name,dept,location, manager
df1.join(df2,df1.dept==df2.dept,'left').select(df1.emp_name,df1.dept,df2.location,df1.manager_id).display()
# Find employees working in Hyderabad.
df1.join(df2,df1.dept==df2.dept,'left').filter(df2.location=='Hyderabad').select(df1.emp_name,df1.location).display()
# Find employees whose department manager is Raj.
df1.join(df2,df1.dept==df2.dept,'left').filter(df1.manager_id==2).select(df1.emp_name,df1.manager_id).display()
# Perform a self join using manager_id.
df1.alias('e1').join(df1.alias('e2'),col('e1.manager_id')==col('e2.emp_id'),'inner').select(col('e1.emp_name'),col('e2.emp_name')).display()
# 14. JOIN INTERVIEW QUESTIONS
# Find employees and their manager names using self join.
df1.alias('e1').join(df1.alias('e2'),col('e1.manager_id')==col('e2.emp_id'),'inner').select(col('e1.emp_name'),col('e2.emp_name')).display()

# Find employees whose manager earns more than them.
df1.alias('e1').join(df1.alias('e2'),col('e1.manager_id')==col('e2.emp_id'),'inner').filter(col('e1.salary')<col('e2.salary')).select(col('e1.emp_name'),col('e2.emp_name')).display()
# Find employees who don't have a valid manager.
df1.join(df2,df1.dept==df2.dept,'leftanti').display()
# Find departments having no employees.
df2.join(df1.dept==df1.dept,'rightanti').display()
# Find employees whose department location is different from their city.
df1.join(df2,df1.dept==df2.dept,'left').filter(df1.city!=df2.location).select(df1.emp_name,df1.city,df2.location).display()



# COMMAND ----------

# 15. WINDOW FUNCTIONS — BASIC

# This is one of the most important PySpark interview topics.

# Practice:

# Window.partitionBy()

# row_number()

# rank()

# dense_rank()

# lag()

# lead()

# sum() over

# avg() over

# Assign a row number to every employee.
# Assign row numbers separately for each department.

# Expected concept:

# IT       → 1,2,3,4
# HR       → 1,2,3
# Finance  → 1,2,3
# Rank employees based on salary.
# Rank employees based on salary within each department.
# Compare:
# rank()
# dense_rank()
# row_number()

# using duplicate salaries.

# 16. TOP-N USING WINDOW FUNCTIONS
# Find the highest-paid employee in each department.
# Find the top 2 highest-paid employees in each department.
# Find the top 3 highest-paid employees in each department.
# Find the second-highest salary in each department.
# Find the third-highest salary in each department.
# Find the youngest employee from each department.
# Find the oldest employee from each department.


# COMMAND ----------


# 17. LAG / LEAD
# Find the previous employee's salary within each department.
# Find the next employee's salary within each department.
# Compare an employee's salary with the previous employee's salary.
# Find employees whose salary is greater than the previous employee's salary.
# Find employees whose salary is lower than the next employee's salary.
# 18. WINDOW AGGREGATIONS
# Calculate average salary of each department and display it alongside every employee.

# Example:

# Alice     IT     75000     86250
# Charlie   IT     90000     86250
# Emma      IT     85000     86250
# Calculate department-wise total salary without collapsing rows.
# Calculate department-wise maximum salary without collapsing rows.
# Calculate each employee's salary percentage of their department's total salary.
# Calculate cumulative salary within each department.
# Calculate cumulative employee count within each department.


# COMMAND ----------

# 19. ADVANCED DATE + WINDOW
# Find the first employee hired in every department.
# Find the most recently hired employee in every department.
# Rank employees within each department based on hire date.
# Find the second employee hired in each department.
# Find the employee hired immediately before each employee.
# Find the number of days between the current employee's hire date and the previous employee's hire date.
# 20. MIXED INTERVIEW QUESTIONS 🔥

# Now don't think about which function to use. Decide the solution yourself.

# Find the second-highest salary employee in each department.
# Find the top 3 salaries in each department.
# Find employees whose salary is greater than their department's average salary.
# Find employees whose salary is greater than the company average salary.
# Find the department with the highest average salary.
# Find the department with the highest total salary.
# Find the city having the highest number of employees.
# Find the highest-paid female employee in each department.
# Find the highest-paid male employee in each department.
# Find employees who earn more than their manager.
# Find employees who earn the same salary as another employee.
# Find duplicate employee records.
# Remove duplicate employee records.
# Find employees who joined in the same year.
# Find the department with the oldest employee.
# Find employees who joined before their manager.