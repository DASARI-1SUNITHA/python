# Databricks notebook source
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('sparktaskprcatice').getOrCreate()
df=spark.read.csv('/Workspace/Users/dasarisunitha402@gmail.com/Drafts/emp.csv',header=True,inferSchema=True,)
df.show()

# COMMAND ----------

# 🟢 Level 1 — DataFrame Basics
from pyspark.sql .functions import col
# Q1 Display the complete DataFrame.
df.show()
# Q2 Display only name, department, and salary.
df.select('name','department','salary').show()
# Q3.Display only emp_id, name, and city.
df.select('emp_id','name','city').show()
# Q4 Display the schema of the DataFrame.
df.printSchema()
# Q5.Count the total number of employees.
print(f"Total employees: {df.count()}")
# Q6.Display all unique departments.
df.select('department').distinct()
# Q7.Display all unique cities.
df.select('city').distinct()
# Q8.Display the first 5 employees.
df.show(5)
# Q9.Display employees whose salary is greater than 60000.
df.filter(col('salary')>60000).show()
# Q10.Display employees whose salary is less than 50000.
df.filter(col('salary')<50000).show()

# COMMAND ----------

# 🟢 Level 2 — filter() / where()
from pyspark.sql.functions import col 
# Q11.Find employees who work in the IT department.
df.filter(col('department')=='IT').show()
# Q12.Find employees who work in IT or Finance.
df.filter((col('department')=='IT') | (col('department')=='Finance')).show()
# Q13.Find employees who work in IT and have salary greater than 70000.
df.filter((col('department')=='IT') & (col('salary')>70000)).show()
# Q14.Find employees from Hyderabad.
df.select('name').filter(col('city')=='Hyderabad').show()
# Q15.Find employees from Hyderabad who work in IT.
df.select('name','department','city').filter((col('department')=='IT') & (col('city')=='Hyderabad')).show()
# Q16.Find employees whose experience is greater than 4 years.
# df.filter(col('experience').try_cast('int')>4).show()
# Q17.Find employees whose experience is between 3 and 6 years.
df.select('name','experience').filter(col('experience').try_cast('int').between(3, 6)).show()
# Q18.Find employees whose salary is between 60000 and 80000.
df.filter((col('salary')>60000)& (col('salary')>80000)).select('name','experience','salary').show()
# Q19.Find employees who are not from Hyderabad.
df.select('name','city').filter(col('city')!='Hyderabad').show()
# Q20.Find employees who are not working in HR.
df.select('name','department').filter(col('department')!='HR').show()
# Q21.Find employees whose salary is greater than 70000 OR experience is greater than 5.
df.select('name','salary','experience').filter(col('salary')>70000).filter(col('experience').try_cast('int')>5).show()
# Q22.Find employees whose salary is greater than 60000 AND experience is greater than 3.
df.select('name','salary','experience').filter((col('salary')>60000) & (col('experience').try_cast('int')>3)).show()

# COMMAND ----------

# 🟡 Level 3 — withColumn()
# Q23.Create a new column called annual_salary.Formula:salary * 12
df.withColumn('annual_salary',col('salary')*12).show()
# Q24.Create a column called salary_after_bonus. Give every employee a 10% bonus.
df.withColumn('salary_after_bonus',col('salary')*0.1).show()
# Q25

# Create a column called experience_months.

# Formula:

# experience * 12
# df.withColumn('experience_months', functions.try_cast(col('experience'), 'int')*12).show()
# Q26

# Create a column called salary_in_lakhs.

# Formula:

# salary / 100000
df.withColumn('saalry_in_lakhs',col('salary')/100000).show()
#h Q27

# Create a column called employee_info.

# Expected format:

# Sunitha - IT - Hyderabad
from pyspark.sql.functions import *
df.withColumn('employee_info',concat_ws('-',col('name'),col('city'))).show()
# Q28

# Create a column called salary_category.

# Rules:

# salary >= 80000 → High
# salary >= 60000 → Medium
# otherwise → Low
from pyspark.sql.functions import when
df.withColumn('salary_Category',when(col('salary')>=80000,"High").
              when(col('salary')>=60000,'Medium').when(col('salary')<60000,'Low')).show()
# Q29

# Create a column called experience_category.

# Rules:

# experience < 3 → Junior
# experience 3-5 → Mid
# experience > 5 → Senior
# df.withColumn('experience_category',when(col('experience')<3,'junior').when(col('experience').between(3,5),'Mid').when(col('experience')>5,'Senior')).show()
# Q30

# Create a column called bonus.

# Rules:

# IT       → 15% of salary
# Finance  → 10% of salary
# HR       → 8% of salary
# Sales    → 12% of salary
df.withColumn('bonus',when(col('department')=='IT',col('salary')*0.15).when(col('department')=='Finance',col('salary')*0.1).when(col('department')=='HR',col('salary')*0.08).when(col('department')=='Sales',col('salary')*0.12)).show()

# COMMAND ----------



# COMMAND ----------

