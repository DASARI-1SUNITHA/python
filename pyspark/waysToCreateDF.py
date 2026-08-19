# Databricks notebook source
#ways to create dataframe
#basic: from python list of tuples
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Spark Dataframes Demo").getOrCreate()
data=[(101,'A',30000),(102,'B',40000),(103,'C',50000)]
df=spark.createDataFrame(data)
df.show()

# COMMAND ----------

#from list of column names
data=[(101,'A',30000),(102,'B',40000),(103,'C',50000)]
cols=['id','name','salary']
df=spark.createDataFrame(data,cols)
df.show()

# COMMAND ----------

#using explicit schema
from pyspark.sql.types import *
schema=StructType([StructField('empid',LongType(),True),StructField('empname',StringType(),True),StructField('empsalary',LongType(),True)])
data=[(101,'sunitha',30000),(102,'angel',40000),(103,'grace',50000)]
df=spark.createDataFrame(data,schema)
df.printSchema()
# df.show()

# COMMAND ----------

#FRom RDD
rdd=spark.sparkContext.parallelize(data)
df=rdd.createDataFrame(rdd,['empid','empname','salary'])
df.shoW() 

# COMMAND ----------

#from dictionary
data=[{'id':101,'name':'sunitha','salary':30000},
      {'id':102,'name':'angel','salary':40000},
      {'id':103,'name':'grace','salary':35000}]
spark.createDataFrame(data)
df.show()

# COMMAND ----------

#reading csv file
df = spark.read \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .csv("/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.csv")

df.show()


# df=spark.read.csv('/FileStore/tables/emp.csv',header=True,inferSchema=True)
# df.show()
# #

# COMMAND ----------

#reading json
# df=spark.read.json([
# #   {"Employee_ID": "EE001", "First_Name": "John", "Last_Name": "Doe", "Department": "Engineering", "Salary": 95000},
# #   {"Employee_ID": "EE002", "First_Name": "Jane", "Last_Name": "Smith", "Department": "HR", "Salary": 82000},
# #   {"Employee_ID": "EE003", "First_Name": "Michael", "Last_Name": "Brown", "Department": "Sales", "Salary": 71000},
# #   {"Employee_ID": "EE004", "First_Name": "Emily", "Last_Name": "Davis", "Department": "Marketing", "Salary": 68000},
# #   {"Employee_ID": "EE005", "First_Name": "David", "Last_Name": "Wilson", "Department": "Finance", "Salary": 88000}
# ]
# )
df=spark.read \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .csv("/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.json")
df.show()

# COMMAND ----------

#reading parquet
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql import Row

# 1. Define the schema layout
schema = StructType([
    StructField("Employee_ID", StringType(), True),
    StructField("First_Name", StringType(), True),
    StructField("Last_Name", StringType(), True),
    StructField("Department", StringType(), True),
    StructField("Salary", DoubleType(), True),
    StructField("Experience_Years", IntegerType(), True)
])

# 2. Add high-quality mock records
data = [
    Row("EE001", "John", "Doe", "Engineering", 95000.00, 4),
    Row("EE002", "Jane", "Smith", "HR", 82000.00, 6),
    Row("EE003", "Michael", "Brown", "Sales", 71000.00, 2),
    Row("EE004", "Emily", "Davis", "Marketing", 68000.00, 3),
    Row("EE005", "David", "Wilson", "Finance", 88000.00, 5)
]

# 3. Create the PySpark DataFrame
df_mock = spark.createDataFrame(data, schema)

# 4. CHOOSE ONE TARGET PATH BELOW (Replace with your actual names)
# Option A: Saving to your Unity Catalog Volume (Recommended)
parquet_target_path = "/dbfs/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.parquet"

# Option B: Saving to your Workspace User folder
# parquet_target_path = "/Workspace/Users/your_email_address/emp.parquet"

# 5. Write out the binary files in overwrite mode
df_mock.write.mode("overwrite").parquet(parquet_target_path)
print(f"Success! Parquet data successfully written to: {parquet_target_path}")


# COMMAND ----------

#how to restrict and  read column names that are required:
#1.using select()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('demo1').getOrCreate()
df=spark.read.csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.csv',header=True,inferSchema=True)
df.show()

# COMMAND ----------

#using column names
from pyspark.sql.functions import col 
df.select(col("Email"),(col("Salary")*10).alias("Salary_emp")).show()


# COMMAND ----------

from pyspark.sql.functions import upper
df.select(col("Email"),upper(col("First_Name")).alias(" Upper_First_Name")).display()
df.show()

# COMMAND ----------

#read using schema
from pyspark.sql.types import *
schema=StructType([StructField('Employee_ID',StringType(),True),StructField('First_Name',StringType(),True),StructField('Last_Name',StringType(),True),StructField('Email',StringType(),True),StructField('Department',StringType(),True),StructField('Job_Title',StringType(),True),StructField('Salary',IntegerType(),True),StructField('Hire_Date',DateType(),True),StructField('Status',StringType(),True)])
df=spark.read.csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.csv',header=True,schema=schema)
df.show()


# COMMAND ----------

#read required columns from parquet:
from pyspark.sql import Row
df=spark.read.parquet('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/flight_data.parquet')
df.show()
df1=df.select('DEST_COUNTRY_NAME','count')
df1.show()




# COMMAND ----------

#use sql
df.createOrReplaceTempView('emploee')
result=spark.sql('''select * from emploee''')
result.show()

# COMMAND ----------

#drop unwanted columns
df=df.drop("count")
df.show()

# COMMAND ----------

#Dynamicalli select columns
df = spark.read \
    .option('header', 'true') \
    .option('inferSchema', 'true') \
    .csv('/Workspace/Users/dasarisunitha83@gmail.com/Drafts/emp.csv')
req_cols=['Employee_ID','First_Name','Last_Name','Email','Department','Salary','Status']
df2=df.select(*req_cols)
df2.show()

# COMMAND ----------

#select columns by patterns
cols=[c for c in df.columns if c.startswith('J')]
df.select(*cols).show()
cols1=[c for c in df.columns if  'salary' in c]
df.select(*cols1).show()

# COMMAND ----------

