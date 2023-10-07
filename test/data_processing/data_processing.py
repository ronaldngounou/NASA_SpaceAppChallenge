#imports
from pyspark.sql import SparkSession
from google.cloud import storage
from pyspark.sql.functions import col, create_map, lit, concat
from itertools import chain
import json
import logging as lg

# set up logging
lg.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=lg.DEBUG)

log = logging.getLogger("my-logger")

# create spark session
spark = SparkSession.builder.getOrCreate()

# create file links
bucket = "dataproc-staging-us-central1-123791584787-rwa2xlbh"
data_folder = "data"
client = storage.Client()
files = [blob.name for blob in client.list_blobs(bucket, prefix=data_folder)]
files = ["gs://"+bucket+"/"+file for file in files]
lg.info(f"created filenames {str(files)}")

# read files into dataframes
df_list=[]
for filename in sorted(files):
    data = spark.read.option("header",True).option("multiLine", "true").csv(filename)
    data = data.drop("description").drop("tags").drop("channel_id")
    if "BR" in filename:
        data = data.withColumn("region", lit("Brazil"))
    elif 'CA' in filename:
        data = data.withColumn("region", lit("Canada"))
    elif 'DE' in filename:
        data = data.withColumn("region", lit("Germany"))
    elif 'FR' in filename:
        data = data.withColumn("region", lit("France"))
    elif 'GB' in filename:
        data = data.withColumn("region", lit("Great Britain"))
    elif 'IN' in filename:
        data = data.withColumn("region", lit("India"))
    elif 'JP' in filename:
        data = data.withColumn("region", lit("Japan"))
    elif 'KR' in filename:
        data = data.withColumn("region", lit("Korea"))
    elif 'MX' in filename:
        data = data.withColumn("region", lit("Mexico"))
    elif 'RU' in filename:
        data = data.withColumn("region", lit("Russia"))
    elif 'US' in filename:
        data = data.withColumn("region", lit("USA")) 
    df_list.append(data)

# combine all dataframes
df_all = df_list[0]
for i in range(1,len(df_list),1):
    df_all = df_all.union(df_list[i])

# remove all unnecessary columns and create video_link column
df_all = df_all.drop("channelId").drop("channelTitle").drop("tags").drop("comments_disabled").drop("ratings_disabled").drop("description")
df_all = df_all.withColumn("video_url_prefix", lit("https://www.youtube.com/watch?v=")).withColumn("video_links", concat(col("video_url_prefix"), col("video_id")))
df_all = df_all.drop("video_url_prefix")

# get the categories
categories_folder = "categories"
categories_list = [json.loads(blob.download_as_string(client=None)) for blob in client.list_blobs(bucket, prefix=categories_folder)]
categories_map = {}
for caregories in categories_list: 
    for item in caregories["items"]:
        categories_map[item["id"]] = item["snippet"]["title"]


#source: https://stackoverflow.com/questions/42980704/pyspark-create-new-column-with-mapping-from-a-dict
mapping_expr = create_map([lit(x) for x in chain(*categories_map.items())])
df_all =df_all.withColumn("category_name", mapping_expr.getItem(col("categoryId")))


df_all.write.csv("gs://"+bucket+"/clean_data/")