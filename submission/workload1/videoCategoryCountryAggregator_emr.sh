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
-mapper videoCategoryReducer.py \
-combiner videoCategoryReducer.py \
-file videoCategoryReducer2.py \
-reducer videoCategoryReducer2.py \
-input $1 \
-output $2