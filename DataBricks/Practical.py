# Databricks notebook source
# DBTITLE 1,managed table
# MAGIC %sql
# MAGIC create table  data_dev.default.test(
# MAGIC     id int,
# MAGIC     name string
# MAGIC ) using delta

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into data_dev.default.test values(1,'sunitha')

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from data_dev.default.test;

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table data_dev.default.test;

# COMMAND ----------

# DBTITLE 1,external location
# MAGIC %sql
# MAGIC create table  data_dev.default.test(
# MAGIC     id int,
# MAGIC     name string
# MAGIC ) using delta
# MAGIC location '/tmp/test'
# MAGIC     

# COMMAND ----------

# DBTITLE 1,volume
# MAGIC %sql
# MAGIC create volume data_dev.default.practical
# MAGIC

# COMMAND ----------

