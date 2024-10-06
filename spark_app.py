from pyspark.sql import SparkSession

# Create a SparkSession
spark = (
    SparkSession.builder 
    .appName("MySparkApplication")
    .remote("sc://localhost")
    .getOrCreate()
)

# You can now use the 'spark' variable to interact with Spark
df = spark.range(100).selectExpr("CAST(id AS STRING) AS key", "CAST(id AS STRING) AS value")

df.show()

df.write.format("kafka").option("kafka.bootstrap.servers", "kafka:29092").option("topic", "test").save()