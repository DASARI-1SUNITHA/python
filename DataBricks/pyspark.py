# Databricks notebook source
# MAGIC %sql
# MAGIC create  database development.data

# COMMAND ----------

# MAGIC %sql
# MAGIC create volume development.data.files

# COMMAND ----------

# MAGIC %md
# MAGIC Data Frame Catalog

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()
df=spark.read.csv("/Volumes/development/data/files/orders/")

# COMMAND ----------

df.show()

# COMMAND ----------

df.display()

# COMMAND ----------

df=spark.read.csv('/Volumes/development/data/files/orders/',header=True )
df.show()

# COMMAND ----------

#to know schems
df.printSchema()

# COMMAND ----------

#to have proper datatypes to each col
df=spark.read.csv('/Volumes/development/data/files/orders/',header=True,inferSchema=True )
df.printSchema()

# COMMAND ----------

df=spark.read.format('csv').options(header=True,inferSchema=True).load('/Volumes/development/data/files/orders/')
df.display()

# COMMAND ----------

#read json files
df=spark.read.json('/Volumes/development/data/files/orders/orders_new.json',multiLine=True)
display(df)

# COMMAND ----------

df=spark.read.format('json').options(multiLine=True).load(
    '/Volumes/development/data/files/orders/orders_new.json'
)
df.show()

# COMMAND ----------

df=spark.read.parquet('/Volumes/development/data/files/orders/orders.parquet')
df.show()

# COMMAND ----------

df=spark.read.format('parquet').load('/Volumes/development/data/files/orders/orders.parquet').show()

# COMMAND ----------

#select Transformation
df=spark.read.parquet('/Volumes/development/data/files/orders/orders.parquet')
df.select('order_id','order_date','quantity').show()

# COMMAND ----------

display(df.select('order_id','order_date','city','category'))

# COMMAND ----------

from pyspark.sql.functions import  col
df.select(col('order_id'),col('order_date')).show()

# COMMAND ----------

df.select(col('order_id'),col('city').alias('location')).show()

# COMMAND ----------

#to add new column and modify the exisitng column:withColumn() is used
from pyspark.sql.functions import col
display(df.withColumn('id1',col('order_id')+1000))

# COMMAND ----------

from pyspark.sql.functions import lit
display(df.withColumn('state',lit('abc')))

# COMMAND ----------

#create a new column based on certain logic
df.withColumn('order_id',col('order_id')-1).show()

# COMMAND ----------

#withColumnRenamed:
df.withColumnRenamed('order_id','id').show()

# COMMAND ----------

#filter transformation similar to where() in sql 
df.filter(df.category=='Books').show()

# COMMAND ----------


df.filter((df['category']=='Books')&(df['quantity']>5)).show()


# COMMAND ----------

df.filter((df['category']=='Electronics')|(df['quantity']>5)).show()


# COMMAND ----------

df.filter(df.category.endswith('g')).show()

# COMMAND ----------

df.filter(df.category.startswith('G')).show()

# COMMAND ----------

df.filter(df.city.like('%Hy%')).show()

# COMMAND ----------

#distinct transformation:removes entire row match
data=[
    (1,'a',23),
    (2,'b',25),
    (3,'c',20),
    (1,'a',23)
]
columns=['id','name','age']
df=spark.createDataFrame(data,columns)
df.show()


# COMMAND ----------

df.distinct().show()

# COMMAND ----------

df.dropDuplicates(['id']).show()

# COMMAND ----------

#groupBy
data=[
    {"emp_id": 101, "name": "Aarav", "department": "IT", "city": "Hyderabad", "salary": 65000},
    {"emp_id": 102, "name": "Priya", "department": "HR", "city": "Bangalore", "salary": 55000},
    {"emp_id": 103, "name": "Rahul", "department": "IT", "city": "Chennai", "salary": 72000},
    {"emp_id": 104, "name": "Sneha", "department": "Finance", "city": "Hyderabad", "salary": 68000},
    {"emp_id": 105, "name": "Kiran", "department": "IT", "city": "Pune", "salary": 58000},
    {"emp_id": 106, "name": "Ananya", "department": "HR", "city": "Hyderabad", "salary": 62000},
    {"emp_id": 107, "name": "Vikram", "department": "Finance", "city": "Mumbai", "salary": 75000},
    {"emp_id": 108, "name": "Meera", "department": "IT", "city": "Bangalore", "salary": 81000},
    {"emp_id": 109, "name": "Arjun", "department": "Sales", "city": "Chennai", "salary": 60000},
    {"emp_id": 110, "name": "Divya", "department": "Sales", "city": "Hyderabad", "salary": 67000},

    {"emp_id": 111, "name": "Rohan", "department": "IT", "city": "Mumbai", "salary": 76000},
    {"emp_id": 112, "name": "Pooja", "department": "HR", "city": "Pune", "salary": 59000},
    {"emp_id": 113, "name": "Suresh", "department": "Finance", "city": "Chennai", "salary": 71000},
    {"emp_id": 114, "name": "Kavya", "department": "Sales", "city": "Bangalore", "salary": 64000},
    {"emp_id": 115, "name": "Manish", "department": "IT", "city": "Hyderabad", "salary": 88000},
    {"emp_id": 116, "name": "Neha", "department": "HR", "city": "Mumbai", "salary": 61000},
    {"emp_id": 117, "name": "Aditya", "department": "Finance", "city": "Pune", "salary": 79000},
    {"emp_id": 118, "name": "Isha", "department": "Sales", "city": "Hyderabad", "salary": 57000},
    {"emp_id": 119, "name": "Naveen", "department": "IT", "city": "Chennai", "salary": 69000},
    {"emp_id": 120, "name": "Swathi", "department": "HR", "city": "Bangalore", "salary": 73000},

    {"emp_id": 121, "name": "Harish", "department": "Finance", "city": "Hyderabad", "salary": 82000},
    {"emp_id": 122, "name": "Lakshmi", "department": "Sales", "city": "Mumbai", "salary": 63000},
    {"emp_id": 123, "name": "Varun", "department": "IT", "city": "Pune", "salary": 74000},
    {"emp_id": 124, "name": "Deepa", "department": "HR", "city": "Chennai", "salary": 56000},
    {"emp_id": 125, "name": "Sanjay", "department": "Finance", "city": "Bangalore", "salary": 86000},
    {"emp_id": 126, "name": "Keerthi", "department": "Sales", "city": "Pune", "salary": 70000},
    {"emp_id": 127, "name": "Mohan", "department": "IT", "city": "Hyderabad", "salary": 91000},
    {"emp_id": 128, "name": "Asha", "department": "HR", "city": "Mumbai", "salary": 66000},
    {"emp_id": 129, "name": "Ravi", "department": "Finance", "city": "Chennai", "salary": 77000},
    {"emp_id": 130, "name": "Nisha", "department": "Sales", "city": "Bangalore", "salary": 69000}
]

df=spark.createDataFrame(data)
df.show()

# COMMAND ----------

from pyspark.sql.functions import  count
df.groupBy('department').count().show()


# COMMAND ----------

from pyspark.sql.functions import sum
df.groupBy('salary').agg(sum('salary').alias('total_salary')).show()

# COMMAND ----------

df.groupBy('department').agg({'salary':'sum'}).show()

# COMMAND ----------

#joins
emp_data = [
    (1, "Alice", 1),
    (2, "Bob", 2),
    (3, "Charlie", 3),
    (4, "David", 5)   # dept_id not in dept
]
emp_columns = ["emp_id", "name", "dept_id"]

emp_df = spark.createDataFrame(emp_data, emp_columns)
emp_df.show()

dept_data = [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance"),
    (4, "Marketing")
]
dept_columns = ["dept_id", "dept_name"]

dept_df = spark.createDataFrame(dept_data, dept_columns)
dept_df.show()

# COMMAND ----------

emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'inner').show()

# COMMAND ----------

emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'left').show()

# COMMAND ----------

emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'right').show()

# COMMAND ----------

emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'full').show()

# COMMAND ----------

emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'left_semi').show()

# COMMAND ----------

emp_df.join(dept_df,emp_df.dept_id==dept_df.dept_id,'left_anti').show()

# COMMAND ----------

#union & union all

data1 = [
    (1, "Alice", "HR"),
    (2, "Bob", "IT")
]
columns = ["id", "name", "dept"]

df1 = spark.createDataFrame(data1, columns)
df1.show()

data2 = [
    (3, "Charlie", "Finance"),
    (4, "David", "IT"),
    (2, "Bob", "IT")   # duplicate row
]

df2 = spark.createDataFrame(data2, columns)
df2.show()

# COMMAND ----------

df1.union(df2).show()

# COMMAND ----------

df1.unionAll(df2).show()

# COMMAND ----------

df1.unionByName(df2).show()

# COMMAND ----------

df1.union(df2).distinct().show()

# COMMAND ----------

#structType and StructField
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("StructType").getOrCreate()
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), True),
    StructField("age",IntegerType(),False)])
data=[(1,"James",-1),(2,"Ann",0),(3,"Jeff",40)]
df = spark.createDataFrame(data=data, schema=schema)
df.show()
df.printSchema()

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
spark = SparkSession.builder.appName("SparkByExamples.com").getOrCreate()
schema=StructType([
    StructField("name",StringType(),True),
    StructField("dob",StringType(),True),
    StructField("gender", StringType(), True),
    StructField("salary", IntegerType(), True)])
df=spark.read.csv('emp.csv',schema=schema,header=True)
df.show()
df.printSchema()

# COMMAND ----------

#pivot & unpivot
#inorder convert row to column based we use pivot
data = [
    ("Banana", 100, "USA"),
    ("Carrots", 150, "USA"),
    ("Beans", 160, "Russia"),
    ("Orange", 80, "USA"),
    ("Orange", 70, "USA"),
    ("Banana", 105, "japan"),
]
columns = ["Product", "Amount", "Country"]
df = spark.createDataFrame(data, columns)
df.show()


# COMMAND ----------

df.groupBy("Product").pivot("Country").sum("Amount").show()

# COMMAND ----------

df1=df.groupBy("Product").pivot("Country").sum("Amount")
df1.show()

# COMMAND ----------

from pyspark.sql.functions import expr
df1.select('Product',expr('stack(3,"USA",USA,"Russia",Russia,"japan",japan) as (Country, Amount)')).show()

# COMMAND ----------

#UDF
from pyspark.sql.functions import udf
data=[('a','sdf','53'),('b','asdsw',23),('c','hjk',21)]
df=spark.createDataFrame(data,["name","address","age"])
df.show()


# COMMAND ----------

def age_group(age):
    if age<18:
        return "Teenager"
    elif age>=18 and age<60:
        return "Adult"
    else:
        return "Senior Citizen"
age_group(49)

# COMMAND ----------

from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
age_group_category=udf(age_group,StringType())
df.withColumn('age_cat',age_group_category(df.age.cast('int'))).show()

# COMMAND ----------

#temperory view
data=[('a',19),('b',22),('c',23)]
columns=['name','age']
df=spark.createDataFrame(data,columns)
df.show()

# COMMAND ----------

df.createOrReplaceTempView('test')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from test;

# COMMAND ----------

df=spark.read.parquet('/Volumes/development/data/files/orders/orders.parquet')
df.createOrReplaceTempView('orders')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from orders;

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(distinct order_id) from orders

# COMMAND ----------

#window functions
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number,rank,dense_rank,ntile,percent_rank,cume_dist,lead,lag,col
df=spark.read.csv('/Volumes/development/data/files/orders/employee_data.csv',header=True,inferSchema=True)
df.show()

# COMMAND ----------

df.createOrReplaceTempView('emp_details')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from emp_details;

# COMMAND ----------

# MAGIC %sql
# MAGIC select *,row_number() over(partition by dept order by salary desc) as rownumber from emp_details;

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number,rank,dense_rank,ntile,percent_rank,cume_dist,lead,lag,col
w=Window.partitionBy('dept').orderBy(col('salary').desc())
df.withColumn('row_number',row_number().over(w)).show()


# COMMAND ----------

df.withColumn('rank',rank().over(w)).show()

# COMMAND ----------

df.withColumn('dense_rank',dense_rank().over(w)).show()

# COMMAND ----------

df.withColumn('ntile',ntile(3).over(w)).show()


# COMMAND ----------

df.withColumn('percent_rank',percent_rank().over(w)).show()


# COMMAND ----------

df.withColumn('cume_dist',cume_dist().over(w)).show()

# COMMAND ----------

df.withColumn('lead_emp',lead('salary',1).over(w)).show()

# COMMAND ----------

df.withColumn('lag_emp',lag('salary',1).over(w)).show()

# COMMAND ----------

#date format()
from pyspark.sql.functions import to_date,date_format
df.select('emp_id','hire_date',to_date('hire_date','yyyy-MM-dd').alias('new_date')).show()
#)


# COMMAND ----------

df.select('emp_id','hire_date',to_date('hire_date','yyyy/MMM/dd').alias('new_date')).show()



# COMMAND ----------

df.select('emp_id','hire_date',to_date('hire_date','yyyy/MM/dd').alias('new_date')).show()

# COMMAND ----------

# MAGIC %md
# MAGIC