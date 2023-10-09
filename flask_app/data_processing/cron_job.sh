while true
do
    # remove old local data
    rm -d -r -f data
    echo "deleted the old data"

    # dowload new data
    mkdir data
    cd data
    kaggle datasets download -d rsrishav/youtube-trending-video-dataset
    echo "downloaded new data"

    # "*" ensures we still get the data if the filename changes for some reason one day
    mv *.zip data.zip
    unzip data.zip
    echo "unzipped all the data for today"

    # remove old data in the cloud
    gsutil rm -r gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/data
    gsutil rm -r gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/categories
    gsutil rm -r gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/final_data
    echo "deleted old data"

    # upload data to google cloud storage
    cd ..
    gsutil -m cp data/*.csv gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/data/
    gsutil -m cp data/*.json gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/categories/
    echo "uploaded new data"

    # run pyspark script for cleaning the data
    python data_processing.py

    # upload new combined data
    gsutil rm -r gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/clean_data/_SUCCESS
    hadoop fs -getmerge gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/clean_data/ ./clean_data.csv
    # add the header to the csv file because it is lost in the merging process
    sed -i '1s/^/video_id,title,publishedAt,categoryId,trending_date,view_count,likes,dislikes,comment_count,thumbnail_link,region,video_links,category_name/' ./clean_data.csv
    gsutil -m cp ./clean_data.csv gs://dataproc-staging-us-central1-123791584787-rwa2xlbh/final_data/clean_yt_data.csv
    rm ./clean_data.csv
    sleep 24h
done
