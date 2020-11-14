from pyspark.sql import SparkSession
from pyspark.sql import SQLContext

if __name__ == "__main__":
    scSpark = SparkSession.builder.appName("super market").getOrCreate()
    data_file = "./data/supermarket_sales - Sheet1.csv"

    # EXECUTE
    sdfData = scSpark.read.csv(data_file, header=True, sep=",").cache()

    # TRANSFORM
    gender = sdfData.groupBy("Gender").count()
    print(gender.show())

    # TRANSFORM
    sdfData.registerTempTable("sales")
    output1 = scSpark.sql("SELECT * FROM sales")
    output1.show()

    # TRANSFORM
    output2 = scSpark.sql("SELECT * FROM sales WHERE `Unit price` < 15 AND Quantity < 10")
    output2.show()

    # TRANSFORM
    output3 = scSpark.sql("SELECT count(*) as Total, City FROM sales GROUP BY City")
    output3.show()

    # LOAD
    output1.coalesce(1).write.format('json').save('output/output1-filtered.json')
    output2.coalesce(1).write.format('json').save('output/output2-filtered.json')
    output3.coalesce(1).write.format('json').save('output/output3-grouped.json')