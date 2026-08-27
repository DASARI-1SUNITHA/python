# Databricks notebook source
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Spark DataFrames").getOrCreate()


data = [
    (101, "Anita",  "IT",      "Hyderabad",  "2022-01-15", "1998-05-12", "2026-08-20 09:15:00", 65000, 201, "2026-08-20", None,         "Present"),
    (102, "Rahul",  "HR",      "Chennai",   "2021-03-10", "1995-08-22", "2026-08-20 09:30:00", 55000, 202, "2026-08-20", None,         "Present"),
    (103, "Priya",  "Finance", None,        "2023-06-25", "1999-11-10", None,                  60000, 203, "2026-08-20", None,         "Present"),
    (104, "Kiran",  "IT",      "Bangalore", None,         "1997-02-18", "2026-08-19 10:10:00", None, 201, "2026-08-19", "2026-08-19", "Leave"),
    (105, "Suresh", None,      "Hyderabad",  "2020-11-05", None,         "2026-08-20 09:45:00", 72000, None,"2026-08-20", None,         "Present"),
    (106, "Divya",  "HR",      "Mumbai",     "2024-01-20", "2000-04-15", None,                  48000, 202, "2026-08-20", "2026-08-20", "Leave"),
    (107, "Arjun",  "IT",      None,        "2022-07-12", "1996-09-25", "2026-08-18 09:05:00", 68000, 201, "2026-08-18", None,         "Present"),
    (108, "Meena",  "Finance", "Pune",      "2023-09-18", "1998-12-30", "2026-08-20 09:20:00", None, 203, "2026-08-20", None,         "Present"),
    (109, "Vijay",  "IT",      "Chennai",   "2021-12-01", "1994-07-19", None,                  75000, None,"2026-08-20", None,         "Present"),
    (110, "Sneha",  "HR",      None,        "2022-04-22", "1997-10-11", "2026-08-20 09:35:00", 52000, 202, "2026-08-20", None,         "Present"),
    (111, "Ravi",   None,      "Hyderabad",  "2020-08-15", "1993-03-05", "2026-08-19 09:40:00", 80000, 201, "2026-08-19", "2026-08-19", "Leave"),
    (112, "Pooja",  "Finance", "Mumbai",     None,         "1999-01-28", "2026-08-20 09:55:00", 58000, 203, "2026-08-20", None,         "Present"),
    (113, "Manoj",  "IT",      "Pune",      "2023-02-14", None,         "2026-08-17 10:00:00", 62000, 201, "2026-08-17", None,         "Present"),
    (114, "Lakshmi","HR",      "Chennai",   "2021-06-30", "1996-06-14", None,                  None, 202, "2026-08-20", None,         "Present"),
    (115, "Naveen", "Finance", None,        "2024-03-11", "2001-09-09", "2026-08-20 09:25:00", 50000, 203, "2026-08-20", None,         "Present"),
    (116, "Swathi", "IT",      "Hyderabad",  "2022-10-17", "1998-02-21", "2026-08-20 09:50:00", 67000, 201, "2026-08-20", None,         "Present"),
    (117, "Venkat", None,      "Bangalore", "2020-05-09", "1992-12-03", "2026-08-18 10:15:00", 85000, None,"2026-08-18", None,         "Present"),
    (118, "Asha",   "HR",      "Mumbai",     "2023-11-21", None,         None,                  47000, 202, "2026-08-20", "2026-08-20", "Leave"),
    (119, "Gopal",  "Finance", "Pune",      "2021-09-13", "1995-05-17", "2026-08-20 09:10:00", None, 203, "2026-08-20", None,         "Present"),
    (120, "Kavya",  "IT",      None,        "2024-05-27", "2000-08-26", "2026-08-20 09:40:00", 56000, 201, "2026-08-20", None,         "Present")
]

columns = [
    "employee_id",
    "employee_name",
    "department",
    "city",
    "joining_date",
    "birth_date",
    "last_login",
    "salary",
    "manager_id",
    "attendance_date",
    "leave_date",
    "status"
]

df = spark.createDataFrame(data, columns)

display(df)

# COMMAND ----------

# Understanding NULL Values
# Beginner

# Q1. Display the schema of the DataFrame.
df.printSchema()
# Q2. Find the number of NULL values in every column.
# Expected concept:

# df.select(...)

# and

# isNull()
from pyspark.sql.functions import count,when,count,col
df.select([count(when(col(c).isNull(),c)).alias(c) for c in df.columns]).show()
# Q3. Find employees whose city is NULL.
df.filter(col('city').isNull()).show()

# Q4. Find employees whose salary is NULL.
df.filter(col('salary').isNull()).show()
# Q5. Find employees whose department is NULL.
df.filter('department is null').show()
# Q6. Find employees whose manager_id is NULL.
df.filter(col('manager_id').isNull()).show()
# Q7. Find employees where both city and salary are NULL.
df.filter(col('salary').isNull() & col('city').isNull()).show()
# Q8. Find employees where either city or salary is NULL.
df.filter(col('salary').isNull() | col('city').isNull()).show()


# COMMAND ----------

# Part B — Filtering NULL and NOT NULL

# Q9. Display employees whose salary is NOT NULL.
df.select(col('salary').isNotNull()).show()
# Q10. Display employees whose leave_date is NULL.
df.select(col('leave_date').isNull()).show()
# Q11. Display employees who have a leave_date.
df.select(col('leave_date').isNotNull()).show()
# Q12. Find employees who have a NULL department but a non-NULL salary.
df.select(col('salary').isNotNull(), col('department').isNull()).show()


# COMMAND ----------

# Part C — Counting NULL Values

# Q13. Count the number of NULL values in:

# city
# salary
# department
# manager_id
# joining_date
df.select([count(when(col(c).isNull(),c)).alias(c) for c in df.columns]).show()
# Q14. Find which column has the highest number of NULL values.
null_counts=df.select([count(when(col(c).isNull(),1)).alias(c) for c in df.columns])
null_counts.show()
# Q15. Calculate the percentage of NULL values in every column.

# For example:

# city       → 20%
# salary     → 15%
# department → 10%
total_rows=df.count()
df.select([(count(when (col(c).isNull(),1))/total_rows*100).alias(c) for c in df.columns]).show()

# COMMAND ----------

# Part D — Filling NULL Values


# Q16. Replace NULL city values with "Unknown".
df.fillna({'city':'Unknown'}).show()

# Q17. Replace NULL department values with "Not Assigned".
df.fillna({'department':'Not Assigned'}).show()
# Q18. Replace NULL salary values with 0.
df.fillna({'salary':0}).show()
# Q19. Replace NULL manager_id values with -1.
df.fillna({'manager_id':-1}).show()
# Q20. Replace NULL values in multiple columns using a dictionary.

# For example:

# {
#     "city": "Unknown",
#     "department": "Not Assigned",
#     "salary": 0
#}
df_clean=df.fillna({"city": "Unknown","department": "Not Assigned", "salary": 0})
df_clean.show()


# COMMAND ----------



# COMMAND ----------

# Part E — Handling NULL Salary
# Q21. Find the average salary ignoring NULL values.
from pyspark.sql.functions import avg,coalesce,col
from pyspark.sql.window import Window
df.select(avg('salary').alias('average_salary')).show()
# Q22. Replace NULL salaries with the average salary.

# Hint:

# avg_salary = df.select(avg("salary")).collect()[0][0]

# Then use:

# fillna()
avg_salary=df.select(avg('salary').alias('avg_salary')).collect()[0]['avg_salary']
print(avg_salary)
df_clean=df.fillna({'salary':avg_salary})
df_clean.show()
# Q23. Replace NULL salary with the department-wise average salary.

# This is more advanced.

# You'll need:

# Window
# partitionBy()
# avg()
w=Window.partitionBy('department')
df_clean=df.withColumn('dept_avg_salary',avg('salary').over(w))
df_clean=df_clean.withColumn('salary',coalesce(col('salary'),col('dept_avg_salary')))
df_clean=df_clean.drop('dept_avg_salary')
df_clean.show()


# COMMAND ----------

# Part F — dropna()

# Q24. Remove rows where salary is NULL.
df.dropna(subset=['salary']).show()
# Q25. Remove rows where city is NULL.
df.dropna(subset=['city']).show()
# Q26. Remove rows where all columns are NULL.
df.dropna(how='all').show()
# Q27. Remove rows where any column is NULL.
df.dropna(how='any').show()
# Q28. Remove rows only when both city and salary are NULL.
df.filter(~col('city').isNull() & col('salary').isNull()).show()

# COMMAND ----------

# Part G — NULL + Conditions

# Q29. Find employees where:

# salary > 60000
# OR
# salary IS NULL
df.filter((col('salary')>60000) | col('salary').isNull()).show()
# Q30. Find employees where:

# department = IT
# AND
# salary IS NOT NULL
df.filter((col('department')=='IT') & col('salary').isNotNull()).show()
# Q31. Find employees who have:

# status = Leave
# AND
# leave_date IS NOT NULL
df.filter((col('status')=='Leave') & col('leave_date').isNotNull()).show()
# Q32. Find employees where:

# manager_id IS NULL
# OR
# department IS NULL
df.filter(col('manager_id').isNull() | col('department').isNull()).show()


# COMMAND ----------

