#!/bin/bash
if [ $# -ne 2 ]; then
    echo "Invalid number of parameters!"
    echo "Usage: ./Top10FastestDislikes_SparkJob.sh [enter path to input file] [enter path to output folder]"
    echo "Ensure all paths have the appropriate suffix - e.g. file://<full path>"
    exit 1
fi

spark-submit \
    --master local[4] \
    Top10FastestDislikes_SparkJob.py --input $1 --output $2
	 

    
