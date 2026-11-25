# from pyspark.sql import SparkSession

# spark=SparkSession.builder.appName("Data Analytics").getOrCreate()
# print("spark session created successfully")

# df=spark.read.csv("customer_churn_business_dataset.csv",header=True,inferSchema=True)

# df.show()
# df.printSchema()

# df.select("churn","city").show()

# print(df.count())

# df.filter(df.churn==0).show()

# df.groupBy("country").sum("total_revenue").show()

# df.groupBy("country").avg("total_revenue").show()

# df.orderBy(df.country.desc()).show()

# df.orderBy(df.country.asc()).show()


