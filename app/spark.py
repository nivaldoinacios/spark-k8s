from pyspark.sql import SparkSession

spark = (
    SparkSession
    .builder
    .appName("spark - k8s")
    .getOrCreate()
)

df = spark.range(0,1000000000)

print(f"exibição do frame {df.show()}")
print(f"contagem teste {df.count()}")

spark.stop()