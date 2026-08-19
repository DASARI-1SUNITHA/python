# Databricks notebook source
# PySpark Practice Tasks: DataFrames, RDDs, JSON, Parquet & ORC 
# Module 1: DataFrame Creation 
# • Task 1: Create a DataFrame from a list of tuples. Print schema, display data, rename Salary to MonthlySalary.
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

spark = SparkSession.builder.appName("Spark DataFrames").getOrCreate()
df=spark.createDataFrame([(1,'James',10000),(2,'Michael',20000),(3,'Robert',30000),(4,'Maria',40000),(5,'James',50000)],['id','name','salary'])
df.printSchema()
df.show()
df = df.withColumnRenamed('salary','MonthlySalary')
df.show()
# • Task 2: Create a DataFrame from a list of dictionaries. Check schema and add a Department column. 
data=[{'id':101,"name":"John","salary":50000},
    {"id":102,"name":"Alice","salary":60000},
    {"id":103,"name":"Bob","salary":55000}]
df=spark.createDataFrame(data)
df.printSchema()
df.show()
df=df.withColumn("Department",lit('IT'))
df.show()
# • Task 3: Create a DataFrame using an explicit schema (IntegerType, StringType, DoubleType, DateType). 
from pyspark.sql.types import *
import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import *
data_col=StructType([StructField('id',IntegerType(),True)
                ,StructField('name',StringType(),True),
                StructField('salary',DoubleType(),True),
                StructField('joinDate',DateType(),True)])
data=[(1,'a',789.09,'12-09-23'),(2,'b',7889.09,'22-09-23'),(3,'c',78679.09,'18-09-26')]


# Convert date strings to datetime.date objects
data=[(1,'a',789.09,datetime.date(2023,9,12)),(2,'b',7889.09,datetime.date(2023,9,22)),(3,'c',78679.09,datetime.date(2026,9,18))]
df=spark.createDataFrame(data,schema=data_col)

df.printSchema()
df.show()

# COMMAND ----------

# Module 2: RDD to DataFrame 
# # • Task 4: Create an RDD and convert it to a DataFrame. 
# from pyspark.sql import SparkSession
# from pyspark.sql import Row
# spark=SparkSession.builder.appName("RDDtoDF").getOrCreate()
# sc=spark.sparkContext
# # rdd=sc.parallelize([
# #     (101,'John',50000),
# #     (102,'Alice',60000),
# #     (103,'Bob',55000)
# # ])
# # df=rdd.toDF(['id','name','salary'])
# # df.show()
# # • Task 5: Read a text file into an RDD and convert it to a DataFrame. 

# rdd=sc.textFile('input.txt')
# for row in rdd.collect():
#   print(row)
# rdd1=rdd.map(lambda x:Row(value=x))
# df=spark.createDataFrame(rdd1)
# df.show()
# # • Task 6: Convert a DataFrame back to an RDD and print rows using foreach()
# rdd2=df.rdd.map(lambda x:x.value)
# rdd2.foreach(print)


# COMMAND ----------

# Module 3: Array & Dictionary to DataFrame 
# • Task 7: Convert a list of course names into a single-column DataFrame. 
data=['Python','sql','pyspark','pandas','numpy']
df=spark.createDataFrame(data,['id'])
# df.show()
# Task 8:Convert a 2D array into a DataFrame. 
data=[[1,'a',23],[2,'b',24],[3,'c',24]]
df=spark.createDataFrame(data,['id','name','age'])
df.show()
# • Task 9: Convert a list of dictionaries into a DataFrame. 
data=[
    {'id':1,'name':'John','salary':50000},
    {'id':2,'name':'Alice','salary':60000},
    {'id':3,'name':'Bob','salary':55000}
]
df=spark.createDataFrame(data)
df.show()

# • Task 10: Create a DataFrame from nested dictionaries and print the schema.
data=[{'id':1,'name':'Sunitha','address':{'city':'HYD','state':'TS'}},
    {'id':2,'name':'Ravi','address':{'city':'HYD','state':'TS'}},
    {'id':3,'name':'Rajesh','address':{'city':'HYD','state':'TS'}}]
df=spark.createDataFrame(data)
df.printSchema()
df.show()


# COMMAND ----------

# Module 4: JSON 
# • Task 11: Read a JSON file and display the schema. 
df=spark.read.json('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.json')
df.show()
df.printSchema()
# • Task 12: Filter employees with salary > 50000.
emp=df.filter(df.Salary>80000)
emp.show() 


# • Task 13: Add a Bonus column (10% of salary). 
df=spark.createDataFrame([(1,'James',10000),(2,'Michael',20000),(3,'Robert',30000),(4,'Maria',40000),(5,'James',50000)],['id','name','salary'])
df.show()
df=df.withColumn('Bonus',df.salary*0.1)
df.show()


# • Task 14: Save the DataFrame as JSON. 
# data = [(101, "John", 50000),
#     (102, "Alice", 60000),
#     (103, "Bob", 55000)]
# columns = ["id", "name", "salary"]
# df = spark.createDataFrame(data, columns)
# df.write.mode('overwrite').json('/FileStore/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample.json')
# # df.show()
# • Task 15: Read nested JSON and flatten the address fields. 
from pyspark.sql.functions import col
data={
  "id": 1,
  "name": "John",
  "address": {'city':'NDL','state':'AP'}
}
df=spark.createDataFrame([data])
df.show()
df.printSchema()
# flat_df=df.select('id','name','address.city','address.state')
# flat_df.show()

# flat_df=df.select(col('id'),col('name'),col('address.city').alias('city'),col('address.state').alias('state')).show()


# COMMAND ----------

# Module 5: Parquet 
# • Task 16: Write a DataFrame as Parquet.
# data= [(101, "John", 50000),
#     (102, "Alice", 60000),
#     (103, "Bob", 55000)]
# schema=StructType([StructField("id", IntegerType(), True),
#     StructField("name", StringType(), True),
#     StructField("salary", IntegerType(), True)])
# df=spark.createDataFrame(data,schema)
# df.show()
# df.write.mode('overwrite').parquet('sample.parquet')

# • Task 17: Read a Parquet file and print the schema. 
# df=spark.read.parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/flight_data.parquet')
# df.show()
# • Task 18: Append new records to Parquet. 
# new_data = [("Australia", "United States", 18),
#     ("Germany", "India", 25)]
# columns = ["DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME", "count"]
# new_df = spark.createDataFrame(new_data, columns)
# new_df.show()
# new_df.write.mode('append').parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/flight_data.parquet')
# df=spark.read.parquet("/Workspace/Users/dasarisunitha83@gmail.com/Drafts/flight_data.parquet")
# df.show()
# • Task 19: Overwrite an existing Parquet file. 
import pandas as pd
# df=spark.createDataFrame([{'id':1,'name':'a','salary':10000},{'id':2,'name':'b','salary':20000},{'id':3,'name':'c','salary':30000}])
# df.show()
# df.write.mode('overwrite').parquet('/Workspace/Users/dasarisunitha83@gmail.com/flight_data.parquet')
# • Task 20: Read only selected columns from Parquet. 
path="/Workspace/Users/dasarisunitha83@gmail.com/Drafts/flight_data.parquet"
df=spark.read.parquet(path).select('ORIGIN_COUNTRY_NAME')
df.show()

# COMMAND ----------

# Module 6: ORC 
# • Task 21: Write a DataFrame as ORC. 
# data=[(3,'b',10000),(1,'b',20000),(2,'c',30000)]
# df1=spark.createDataFrame(data,schema=['id','name','salary'])
# path="/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample.orc"
# df1.write.format('orc').save(path)
# print("data sucessfully written")

# • Task 22: Read an ORC file and display the schema.
# path='/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample.orc'
# df_orc=spark.read.format('orc').load(path)
# df_orc.printSchema()
# df_orc.show()
# • Task 23: Filter employees with salary > 60000. 
# path='/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample.orc'
# df_orc=spark.read.format('orc').load(path)
# filter_df=df_orc.filter(df_orc['salary']>60000)
# filter_df.show()

# • Task 24: Compare ORC file size with JSON. 
# df=spark.read.csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample.csv')
# df.write.mode('overwrite').format('json').save('/Workspace/Users/dasarisunitha83/Darfts/json_data')
# df.write.mode('overwrite').orc('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/orc_data')
# json_size=sum(file.size for file in dbutils.fs.ls("/Workspace/Users/dasarisunitha83@gmail.com/Drafts/json_data"))
# orc_size=sum(file.size for file in dbutils.fs.ls("/Workspace/Users/dasarisunitha83@gmail.com/Drafts/orc_data"))
# print('json file:',json_size)
# print('orc file:',orc_size)

# COMMAND ----------


# Module 7: Conversion Tasks 
# • Task 25: CSV→ DataFrame → Parquet 
# df=spark.read.csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.csv',header=True,inferSchema=True)
# df.show()
# df.write.mode('overwrite').parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.parquet')
# df1=spark.read.parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample.parquet')
# df1.show()

# • Task 26: JSON → DataFrame → ORC 
# df=spark.read.json('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.json')
# df.show()
# df.write.mode('overwrite').orc('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.orc')
# df1=spark.read.orc('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.orc')
# df1.show()
# • Task 27: RDD → DataFrame → JSON 
# rdd=spark.SparkContext.parallelize([1,'a',34567),(2,'b',6789),(3,'c',90123)])
# df=spark.createDataFrame(rdd,['id','name','salary'])
# df.show()
# df.write.mode('overwrite').json('/Workspace/Users/dasarisunitha83@gamil.com/Drafts/sample_output.json')
# • Task 28: Dictionary → DataFrame → Parquet 
# df=[{'id':1,'name':'a','salary':2345},{'id':2,'name':'b','salary':23458}]
# df=spark.createDataFrame(df)
# df.write.mode("overwrite").parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.parquet')
# • Task 29: Parquet → DataFrame → RDD 
# df=spark.read.parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.parquet')
# df.show()
# rdd=df.rdd
#print(rdd.collect())
# • Task 30: ORC → DataFrame → JSON 
# df=spark.read.orc('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.orc')
# df.show()
# df.write.mode('overwrite').json('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/sample_output.json')

# COMMAND ----------

# Module 8: Mini Project 
# • Read employee.json, department.csv and salary.parquet. 
# • Join the datasets. 
# • Find employees earning more than 70,000. 
# • Add a 15% Bonus column. 
# • Save the output as JSON, Parquet and ORC. 
# • Read each output back and validate record counts. 
# • Compare storage sizes of JSON, Parquet and ORC. 


# COMMAND ----------

# Challenge Tasks 
# • Flatten nested JSON containing arrays. 
# • Read multiple JSON files from a directory into one DataFrame. 
# • Use explode() on ArrayType columns. 
# Create a DataFrame from dictionaries containing list values. 
# • Read Parquet, filter data and write to ORC. 
# • Compare inferSchema with explicit schemas. 
# • Convert key-value RDDs into DataFrames. 
# • Flatten JSON, save as Parquet and validate schema

# COMMAND ----------



# COMMAND ----------

