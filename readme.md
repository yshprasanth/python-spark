# Installation Steps

## Apache Spark

1. Download latest version from - https://spark.apache.org/downloads.html

    For ex., `spark-3.0.1-bin-hadoop2.7.tgz`

2. Unzip using the command:
    `tar -xvf spark-3.0.1-bin-hadoop2.7.tgz`

3. Set to Path variable:
    `export PATH="<<absolute path>>/spark-3.0.1-bin-hadoop2.7/bin:$PATH"`

4. Open Spark shell by executing below command:
    `spark-shell`
    
## PySpark

1. Ensute latest pip is installed using the command:
    `python3.8 -m pip install --upgrade pip`

2. Install pyspark using the command:
    `pip3 install pyspark`

3. Ensure SPARK_HOME variable is set:
    `export SPARK_HOME="<<absolute path>>/spark-3.0.1-bin-hadoop2.7/"`

4. Open PySpark shell by running following command:
    `pyspark`
