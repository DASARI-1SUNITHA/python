# Databricks notebook source

#joins

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("joins").getOrCreate()
df_emp=spark.read.options(header='True', inferSchema='True').csv('/Workspace/Users/dasarisunitha402@gmail.com/Drafts/employee_data.csv')
df_emp.show()
df_dep=spark.read.options(header='True', inferSchema='True').csv('/Workspace/Users/dasarisunitha402@gmail.com/Drafts/department.csv')
df_dep.show()

#

# COMMAND ----------

# Inner join.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'inner')
df.show()
# Left join.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'left')
df.show()
# Right join.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'right')
df.show()
# Full outer join.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'outer')
df.show()
# Left semi join.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'leftsemi')
# Left anti join.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'leftanti')

# Cross join.
df=df_dep.join(df_emp,df_dep.dept==df_emp.dept,'cross')
df.show()


# COMMAND ----------

# Join using multiple columns.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'inner')
df.show()
# Join when column names are different.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'inner').select(df_emp.emp_name,df_dep.dept)
df.show()
# Find employees without departments.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'leftanti')
df.show()
# Find departments without employees.
df=df_dep.join(df_emp,df_emp.dept==df_dep.dept,'rightanti')
df.show()
# Find employees working in Hyderabad departments.
df=df_emp.join(df_dep,df_emp.dept==df_dep.dept,'inner').filter(df_dep.location=='Hyderabad')
df.show()
# Find employees whose salary is greater than their department average.
df_avg=df_emp.groupBy('dept').agg({'salary':'avg'})
df=df_emp.join(df_avg,df_emp.dept==df_avg.dept,'inner').filter(df_emp.salary>df_avg.avg(salary))
df.show()

# COMMAND ----------

#window Functions
# Assign row numbers to all employees based on salary.
from pyspark.sql.window import Window
from pyspark.sql.functions  import *

# Assign row numbers separately for each department.
w=Window.orderBy(col('salary').desc())
df=df_emp.withColumn('rownumber',row_number().over(w))
df.show()
# Rank employees by salary.
df=df_emp.withColumn('rank',rank().over(w))
df.show()
# Rank employees within each department.
df=df_emp.withColumn('dense_rank',dense_rank().over(w))
df.show()
# Find the top 3 employees in each department.
w=Window.partitionBy('dept').orderBy(col('salary').desc())
df=df_emp.withColumn('rownumber',row_number().over(w)).filter(col('rownumber')<=3)
df.show()
# Find the highest-paid employee in each department.
w=Window.partitionBy('dept').orderBy(col('salary').desc())
result=df.withColumn('rownumber',row_number().over(w)).filter(col('rownumber')==1)
# Find the second-highest salary in each department.
w=Window.partitionBy('dept').orderBy(col('salary').desc())
result=df.withColumn('salary_rank',dense_rank().over(w)).filter(col('salary_rank')==2)
# Find the third-highest salary in each department.
w=Window.partitionBy('dept').orderBy(col('salary').desc())
result=df.withColumn('salary_rank',dense_rank().over(w)).filter(col('salary_rank')==3)
# Compare rank() vs dense_rank() using duplicate salaries.
df=df.withColumn('dense rank',dense_rank().over(w))
df.show()
# Use row_number() to remove duplicates.
w=Window.partitionBy('emp_id','emp_name','dept','salary').orderBy(col('emp_id'))
df1=df.withColumn('rownumber',row_number().over(w))
df1.show()

# COMMAND ----------

# LAG & LEAD
# Find the previous employee's salary within each department.
w=Window.partitionBy('dept').orderBy(col('salary').desc())
res=df.withColumn('previous_salary',lag('salary').over(w))
res.select('emp_name','dept','salary','previous_salary').show()
# Find the next employee's salary.
res=df.withColumn('next_salary',lead('salary').over(w))
res.select('emp_name','dept','salary','next_salary').show()

# Compare current salary with previous salary
res=df.withColumn('previous_salary',lag('salary').over(w))
result = res.withColumn(
    "salary_comparison",
    when(col("salary") > col("previous_salary"), "Higher")
    .when(col("salary") < col("previous_salary"), "Lower")
    .when(col("salary") == col("previous_salary"), "Same")
    .otherwise("First Employee"))
result.select('emp_name','dept','salary','previous_salary','salary_comparison').show()
# Find employees whose salary is greater than the previous employee.
result = df.withColumn("previous_salary",lag("salary").over(w))
result = result.filter(col("salary") > col("previous_salary"))

result.select("emp_name","dept","salary","previous_salary").show()
# Calculate salary difference:
# current_salary - previous_salary
result = (df.withColumn("previous_salary",lag("salary").over(w)))
res=result.withColumn('salary_Diff',col('salary')-col('previous_salary'))
res.select('emp_name','dept','previous_salary','salary_Diff').show()

# Find previous joining date.
w=Window.partitionBy('dept').orderBy(col('hire_date'))
res=df.withColumn('previous_hire_date',lag('hire_date').over(w))
res.select('emp_name','dept','hire_date','previous_hire_date').show()
# Calculate number of days between current employee and previous employee joining dates.
window_spec = Window.partitionBy("dept").orderBy("hire_date")
result = df.withColumn(
    "previous_hire_date",
    lag("hire_date").over(w))
res=result.withColumn('days_Diff',datediff(col("hire_date"), col("previous_hire_date")))
res.select('emp_name','dept','hire_date','previous_hire_date','days_Diff')
# 18. Running & Cumulative Calculations
# Calculate cumulative salary.
w=Window.orderBy('hire_date').rowsBetween(Window.unboundedPreceding,Window.currentRow)
res=df.withColumn('cumulative_salary',sum('salary').over(w))
res.select('emp_name','dept','hire_date','cumulative_salary').show()
# Calculate cumulative salary within each department.
res=df.withColumn('cumulative_salary',sum('salary').over(w))
res.select('emp_name','salary','dept','hire_date','cumulative_salary').show()
# Calculate running average salary.
result=df.withColumn('running_avg_salary',avg('salary').over(w))
result.select('emp_name','hire_date','salary','running_avg_salary').show()
# Find cumulative employee count.
res=df.withColumn('cumu_emp_count',count('*').over(w))
res.select('emp_name','hire_date','cumu_emp_count').show()
# Find minimum salary encountered so far.
res=df.withColumn('min_salary',min('salary').over(w))
res.select('emp_name','hire_date','salary','min_salary').show()

# Find maximum salary encountered so far.
result=df.withColumn('running_max_salary',max('salary').over(w))
result.select('emp_name','hire_date','salary','running_max_salary').show()

# COMMAND ----------



# COMMAND ----------

