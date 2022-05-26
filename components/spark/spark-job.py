from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
import sys
import os


def run(input_dir: str, output_dir: str, config_dir: str):

    # create an app named demo
    spark = SparkSession.builder.appName('demo').getOrCreate()
    df = spark.read.parquet(input_dir)
    parametric = spark.read.json(config_dir)

    # print schemas
    df.printSchema()
    parametric.printSchema()

    # print data
    df.show()
    parametric.show()

    # actions
    data = df.groupBy("vehicle_id", "vehicle_type", "event_mark_time", "tag").agg(sum("distance").alias("km"))
    data = data.where(data.tag == "SHIFT")

    data.createOrReplaceTempView("consolidate")
    parametric.createOrReplaceTempView("parametric")

    result = spark.sql("""
        SELECT cd.vehicle_id vehicle,
               cd.vehicle_type,
               cd.event_mark_time event_date,
               cd.km, round(cd.km * pr.consume_per_km, 2) consume_per_day
        FROM consolidate cd
        INNER JOIN parametric pr
            ON cd.vehicle_type == pr.vehicle_type
    """)
    result.show()
    df.coalesce(1).write.mode("overwrite").parquet(os.path.join(output_dir, "parquet", "compressed"))
    result.coalesce(1).write.mode("overwrite").parquet(os.path.join(output_dir, "parquet", "consolidated"))


if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    config_dir = sys.argv[3]
    run(input_dir, output_dir, config_dir)
