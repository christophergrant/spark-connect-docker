from pyspark.sql import SparkSession

# Create a SparkSession, point to spark connect via docker on port 15002
spark = (
    SparkSession.builder 
    .appName("MySparkApplication")
    .remote("sc://localhost")
    .getOrCreate()
)

# write simple data to kafka, serializing as JSON
df = (
    spark.range(100)
    .selectExpr("CAST(id AS STRING) AS key", "to_json(struct(id)) AS value")
)

# display generated data
df.show()

# write to kafka
(
    df.write.format("kafka")
    .option("kafka.bootstrap.servers", "kafka:29092") # use kafka network name and internal port
    .option("topic", "test")
    .save()
)


# write to object storage
(
    df.write
    .format("parquet")
    .mode("overwrite")
    .save("s3a://test/parquet") # need to use s3a
)
