# from pyspark.sql import SparkSession

# spark=SparkSession.builder \
#     .appName("MySQLIntegretion") \
#     .config(
#     "spark.driver.extraClassPath",
#     "C:/Users/keert/Downloads/mysql-connector-j-26.10.0/mysql-connector-j-26.10.0.jar"
#     )\
#     .getOrCreate()

# spark.sparkContext.setLogLevel("Warn")
# df_mysql=spark.read.format("jdbc")\
#    .option(
#        "url",
#        "jdbc:mysql://localhost:3306/company_db?useSSL=false&allowPublicKeyRetrieval=true& serverTimezone=UTC"
#    )\
#    .option("dbtable","employees")\
#    .option("user","root")\
#    .option("password","Keerthi@1")\
#    .option("driver","com.mysql.cj.jdbc.Driver")\
#    .load()

# print("emeployee data from MySQL")
# df_mysql.show()

# print("table schema")
# df_mysql.printSchema()

# print("total employees : ",df_mysql.count())

# print("IT department employees")
# df_mysql.filter(df_mysql.department=="IT").show()

# from pyspark.sql.functions import avg
# print("average salary")
# df_mysql.select(avg("salary").alias("Average_salary")).show()
# spark.stop()