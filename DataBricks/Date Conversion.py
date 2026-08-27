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

# Part H — Date Conversion
# Currently these columns are strings:

# joining_date
# birth_date
# attendance_date
# leave_date

# Q33.

# Check the schema and identify their current datatype.
df.printSchema()
# Q34.

# Convert joining_date from string to date.

# Use:

# to_date()
from pyspark.sql import functions as F
from pyspark.sql.functions import col,to_date
df=df.withColumn("joining_date",to_date(col('joining_date'),'yyyy-MM-dd'))
df.printSchema()
# Q35.

# Convert:

# birth_date
# attendance_date
# leave_date
# into proper date columns.4
df=(df.
    withColumn('birth_date',to_date('birth_date','yyyy-MM-dd'))
    .withColumn('attendance_date',to_date('attendance_date','yyyy-MM-dd'))
    .withColumn('leave_date',to_date('leave_date','yyyy-MM-dd')))

df.printSchema()

# COMMAND ----------

# Part I — Timestamp Conversion
# last_login contains
# 2026-08-20 09:15:00

# Q36.

# Convert last_login from string to timestamp.

# Use:

# to_timestamp()
from pyspark.sql.functions import to_timestamp,to_date,date_format
df=df.withColumn('last_login',to_timestamp('last_login','yyyy-MM-dd HH:mm:ss'))
df.printSchema()
# Q37.

# Extract the date from last_login.

# Expected:

# 2026-08-20
df=df.withColumn('last_login',to_timestamp('last_login','yyyy-mm-dd HH:mm:ss'))
df=df.withColumn('login_date',to_date('last_login'))
df.select('employee_name','last_login','login_date').show()
# Q38.

# Extract only the time from last_login.

# Expected:

# 09:15:00
df=df.withColumn('last_login',to_timestamp('last_login','yyyy-MM-dd HH:mm:ss'))
df=df.withColumn('login_time',date_format('last_login','HH:mm:ss'))
df.show()


# COMMAND ----------

# Part J — Date Formatting
from pyspark.sql.functions import year,month,dayofmonth
# Q39.

# Convert:

# 2026-01-15

# into:

# 15-01-2026
df=df.withColumn('format_joining_date',date_format('joining_date','dd-MM-yyyy'))
df.select('employee_name','format_joining_date').show()
# Q40.

# Convert joining_date into:

# 15/01/2022
df=df.withColumn('formatted_joining_date',date_format('joining_date','dd/MM/yyyy'))
df.select('employee_name','joining_date').show()

# Q41.

# Convert joining_date into:

# 15-Jan-2022
df.withColumn('joining_date',date_format('joining_date','dd-MMM-yyyy')).show()
# Q42.

# Convert joining_date into:

# January 15, 2022
df.withColumn('joining_date',date_format('joining_date','MMMM dd, yyyy')).show()
# Q43.

# Extract:

# year
# month
# day
# from joining_date.

# Use:

# year()
# month()
# dayofmonth()
df.select('employee_name',
          year('joining_date').alias('joining_year'),
          month('joining_date').alias('joinin_month'),dayofmonth('joining_date').alias('joining_day')).show()


# COMMAND ----------

# Part K — Date Difference
# Q44.
from pyspark.sql.functions import floor,datediff,current_date
# Calculate how many days each employee has been with the company.

# Concept:

# current_date - joining_date
df2=df.withColumn('experience_days',datediff(current_date(),col('joining_date')))
df2.select('employee_name','experience_days').show()
# Q45.

# Calculate employee experience in years.

# For example:

# joining_date = 2022-01-15
# current date = 2026-08-25

# experience ≈ 4 years
df2=df2.withColumn('experience_years',floor(datediff(current_date(),col('joining_date'))/365.0))
df2.select('employee_name','experience_years').show()
# Q46.

# Find employees who joined before:

# 2022-01-01
df2.filter(col('joining_date')<'2022-01-01').select('employee_name','joining_date')
# Q47.

# Find employees who joined after:

# 2023-01-01
df2.filter(col('joining_date') >'2023-01-01').select('employee_name','joining_date').show()
# Q48.

# Find employees who joined between:

# 2021-01-01
# 2023-12-31
df2.filter(col('joining_date').between('2021-01-01','2023-12-31')).select('employee_name','joining_date').show()

# COMMAND ----------

# Part L — Date Functions
from pyspark.sql.functions import current_date,current_timestamp,dayofweek,dayofyear,weekofyear,quarter
# Q49.

# Find the joining year of every employee.
df.select('employee_name',year('joining_date').alias('joining_year')).show()
# Q50.

# Find employees who joined in 2022.
df.select('employee_name',year('joining_date')==2022).show()
# Q51.

# Find employees who joined in January.
df.select('employee_name',month('joining_date')==1).show()
# Q52.

# Find employees who joined during Q1.
df.select('employee_name',quarter('joining_date')==1)
# Q53.

# Find the number of employees who joined in each year.

# Expected:

# year    count
# 2020    ...
# 2021    ...
# 2022    ...
# 2023    ...
# 2024    ...
df.groupBy(year('joining_date').alias('joining_year')).count().orderBy('joining_year').show()

# COMMAND ----------

# Part M — Date + NULL Together
# Q54.

# Find employees whose joining_date is NULL.
df.filter(col('joining_date').isNull()).select('employee_name').show()
# Q55.

# Find employees whose joining_date is NOT NULL.
df.filter(col('joining_date').isNotNull()).select('employee_name').show()
# Q56.

# Find employees who joined after 2022 but whose leave_date is NULL.
df.filter((col('joining_date') > '2022-01-01') & col('leave_date').isNull()).select('employee_name').show()
# Q57.

# Find employees where:

# joining_date IS NULL
# OR
# birth_date IS NULL
df.filter(col("joining_date").isNull() | col("birth_date").isNull( ))
# Q58.

# Find employees where both:

# joining_date IS NOT NULL
# birth_date IS NOT NULL
df.filter(col('joining_date').isNotNull() & col('birth_date').isNotNull()).select('employee_name','joining_date','birth_date').show()


# COMMAND ----------

