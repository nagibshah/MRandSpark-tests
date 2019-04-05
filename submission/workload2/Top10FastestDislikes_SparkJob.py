# all required import libraries 
import sys
from pyspark import SparkContext
import filterHelpers as helpers
import argparse

if __name__ == "__main__":
    sc = SparkContext(appName="Average Rating per Genre")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="the input path",
                        default='/Users/nagibshah/dev/COMP5349_MRandSpark/data/')
    parser.add_argument("--output", help="the output path",
                        default='/Users/nagibshah/dev/COMP5349_MRandSpark/data/top10VideosOut/')
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    
    #videoData = sc.textFile(input_path + "AllVideos_short.csv")
    videoData = sc.textFile(input_path)

    videoStats = videoData.map(helpers.extractMovieRecord).filter(lambda x: x)

    # group by key & filter by country 
    groupedTrends = videoStats.groupByKey().mapValues(helpers.mapFirstTwoRecords)
    # unpack the values in the rdd (K, [V,V]) > (K, V) & sort by the key 
    videoTrends = groupedTrends.flatMap(lambda x: [(x[0], y) for y in x[1]]).sortByKey()
    # reduce by key to sum the likes and dislikes 
    videoTrendsDislikes = videoTrends.reduceByKey(helpers.reduceLikesDislikesGrowth).map(helpers.mapDislikesTrend)
    # sort by the trend value in descending order 
    videoTrendsSorted = videoTrendsDislikes.sortBy(lambda x: x[1],ascending=False)

    # get the top 10 video records and save to file 
    top10ControversialVideos = sc.parallelize(videoTrendsSorted.take(10))
    # coalesce to create a single partition out of the top 10 entries
    top10ControversialVideos.coalesce(1,False).saveAsTextFile(output_path)