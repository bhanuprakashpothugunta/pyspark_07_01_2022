import pyspark
from pyspark.sql import SparkSession
if __name__ == "__main__":
    print("Application started......")

    spark = SparkSession.builder.master("local") \
        .appName('SparkByExamples.com') \
        .getOrCreate()
    df = spark.read.csv('C:\\Users\\banup\\OneDrive\\Desktop\\spark\\emp1.txt', header=True)
    df.show()

    print("first bug fix")

    print("Application Completed......")

