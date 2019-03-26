#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./videoCategoryCountryAggregator.sh [enter path to input file] [enter path to output file]"
    exit 1
fi

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='Video Category Country Average list' \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file videoCategoryMapper.py \
-mapper videoCategoryMapper.py \
-file videoCategoryCombiner.py \
-combiner videoCategoryCombiner.py \
-file videoCategoryReducer.py \
-reducer videoCategoryReducer.py \
-input $1 \
-output tmpOutput

hadoop jar /usr/lib/hadoop/hadoop-streaming-2.8.5-amzn-1.jar \
-D mapreduce.job.reduces=3 \
-D mapreduce.job.name='Video Category Country Average list - chain 2' \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file videoCategoryMapper2.py \
-mapper videoCategoryMapper2.py \
-file videoCategoryReducer2.py \
-reducer videoCategoryReducer2.py \
-input tmpOutput/part-00000 \
-input tmpOutput/part-00001 \
-input tmpOutput/part-00002 \
-output $2

hadoop fs -rm -r tmpOutput
