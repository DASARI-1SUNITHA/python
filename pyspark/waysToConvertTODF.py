# Databricks notebook source
#ways to convert array (list) to dataframe
#array/list
#createDataFrame from list of tuples
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data=[(101,'a',50000),(102,'b',60000),(103,'c',70000)]
df=spark.createDataFrame(data,['id','name','salary'])
df.show()


# COMMAND ----------

#create DataFRame from lists of lists:
data=[[101,'d',50000],[102,'e',60000],[103,'f',70000]]
df=spark.createDataFrame(data,['id','name','salary'])
df.show()

# COMMAND ----------

#create data frame from list of dictionaries:
data =[{"id":101,"name":"John","salary":50000},
    {"id":102,"name":"Alice","salary":60000},
    {"id":103,"name":"Bob","salary":55000}]
df=spark.createDataFrame(data)
df.show()

# COMMAND ----------

#lis of row objects:
from pyspark.sql import Row
data=[Row(id=101,name='John',salary=50000),
    Row(id=102,name='Alice',salary=60000),
    Row(id=103,name='Bob',salary=55000)]
df=spark.createDataFrame(data)
df.show()

# COMMAND ----------

#lists with explicit Schema
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
schema = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("name",StringType(),True), \
    StructField("salary",IntegerType(),True)])
data=[(101,'John',50000),(102,'Alice',60000),(103,'Bob',55000)]
df=spark.createDataFrame(data,schema)
df.show()



# COMMAND ----------

#lists -->RDD---->dataframe

# data = [
#     (101, "John", 50000),
#     (102, "Alice", 60000)
# ]

# rdd = sc.parallelize(data)

# df = rdd.toDF(["id", "name", "salary"])

# df.show()


# COMMAND ----------



# COMMAND ----------

#single column list
data=[101,102,103]
df=spark.createDataFrame([(x,) for x in data],['id'])
df.show()

# COMMAND ----------

#nested list
data=[[101,'John',50000],[102,'Alice',60000],[103,'Bob',55000]]
df=spark.createDataFrame(data,['id','name','salary'])
df.show()

# COMMAND ----------

#numpy array---->dataframe
import numpy as np
arr=np.array([[101,'John',50000],[102,'Alice',60000],[103,'Bob',55000]])
df=spark.createDataFrame(arr.tolist(),['id','name','salary'])
df.show()

# COMMAND ----------

#pandas dataframe----->pysparkdataframe
import pandas as pd
pdf=pd.DataFrame({'id':[101,102],'name':['angel','sunitha'],'salary':[50000,60000]})
df=spark.createDataFrame(pdf)
df.show()


# COMMAND ----------

