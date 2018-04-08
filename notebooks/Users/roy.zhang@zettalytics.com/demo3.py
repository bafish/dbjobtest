# Databricks notebook source
x = 5

df = sqlContext.range(5).toDF("value")
#df.show()
df.createOrReplaceGlobalTempView("my_data")
dbutils.notebook.exit("my_data")
#dbutils.widgets.text("foo", "fooDefault", "fooEmptyLabel")
#print dbutils.widgets.get("foo")
#dbutils.notebook.exit("returnValue")
#dbutils.notebook.help()

# COMMAND ----------

