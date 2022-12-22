# Import necessary libraries
import sys
import logging
from textblob import TextBlob
import time
import pyspark
import subprocess
from pyspark.streaming import StreamingContext
import mysql.connector
from kafka import KafkaProducer
from elasticsearch import Elasticsearch
from pyspark.streaming.kafka import KafkaUtils

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
                    filename="logfile.log", filemode="w")

# Set up the Spark context and the streaming context
sc = pyspark.SparkContext(appName="TwitterStream")
ssc = StreamingContext(sc, 10)  # batch interval of 10 seconds

# Get user input for the required variables
spark_home = input("Enter the path to your Spark installation: ")
zk_quorum = input("Enter the Zookeeper quorum (host:port): ")
consumer_group = input("Enter the consumer group name: ")
kafka_topic = input("Enter the Kafka topic name: ")
batch_interval = int(input("Enter the batch interval in seconds: "))
mysql_host = input("Enter the MySQL hostname: ")
mysql_user = input("Enter the MySQL username: ")
mysql_password = input("Enter the MySQL password: ")
mysql_database = input("Enter the MySQL database name: ")

# Set up the Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Set up the Kafka stream
kafka_stream = KafkaUtils.createDirectStream(
    ssc, "localhost:2181", "spark-streaming-consumer", {"twitter-topic": int(1)})  # fix: cast number of partitions to int

# Process the stream
tweets = kafka_stream.map(lambda x: x[1])  # x[1] contains the tweet text

# Send a message to the Kafka topic
topic = 'twitter-topic'
message = 'Hello, Kafka!'
producer.send(topic, message.encode('utf-8'))

# Set up the Elasticsearch client
es = Elasticsearch(['localhost:9200'])


# Write the tweets to Elasticsearch
def write_to_elasticsearch(rdd):
    try:
        rdd.foreachPartition(lambda records: insert_to_elasticsearch(records))
    except Exception as e:
        logging.error("Error writing to Elasticsearch: %s", e)
        sys.exit(1)


def insert_to_elasticsearch(records):
    for record in records:
        # calculate sentiment of tweet
        sentiment = TextBlob(record).sentiment.polarity
        es.index(index='twitter', doc_type='tweet', body={
                 'tweet': record, 'sentiment': sentiment})


# Write the tweets to MySQL
def write_to_mysql(rdd):
    try:
        rdd.foreachPartition(lambda records: insert_to_mysql(records))
    except Exception as e:
        logging.error("Error writing to MySQL: %s", e)
        sys.exit(1)


def insert_to_mysql(records):
    cnx = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = cnx.cursor()
    for record in records:
        # calculate sentiment of tweet
        sentiment = TextBlob(record).sentiment.polarity
        query = 'INSERT INTO tweets (tweet, sentiment) VALUES (%s, %s)'
        cursor.execute(query, (record, sentiment))
    cnx.commit()
    cursor.close()
    cnx.close()


# Set up the streaming context
tweets.foreachRDD(write_to_elasticsearch)
tweets.foreachRDD(write_to_mysql)

# Start the streaming context
ssc.start()

# Wait for the streaming context to stop
ssc.awaitTermination()
