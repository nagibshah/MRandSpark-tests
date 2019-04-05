import csv
"""
This module includes a few functions used in locate top 10 more disliked trending videos
"""


def extractMovieRecord(record):
    """This function converts entries of AllVideos_short.csv into key,value(s) pair of the following format
    (K, (V, W)) = (video_id, (category, likes, dislikes, country))
    Args:
        record (str): A row of CSV file, with the columns separated by comma
        Input format: video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,
        comment_count,ratings_disabled,video_error_or_removed,country
    Returns:
        The return value is a tuple - (video_id, (category,likes,dislikes,country))
    """
    
    try:
        for row in csv.reader([record]):
            if len(row) != 12: # ensure the CSV is well formed 
                continue
            # get the data points of interest
            video_id, category, likes, dislikes, country= row[0],row[3],int(row[6]),int(row[7]),row[11]
            return ((video_id,country), [category, likes, dislikes])
    except:
        return ()

def mapFirstTwoRecords(records): 
    """ this function takes an iterable V as record post a groupByKey on the RDD (K, List<V>) 
    and returns only first two rows of the iterable back as results in the same (K, List<V>) format
    where the new V is a merge of the first two rows 
    Args: 
        record (List<V>) 
    Returns: 
        the merger of the first two rows in a new V 
    """ 
    firstTwo = list(records)[:2]
    return firstTwo

def reduceLikesDislikesGrowth(v1, v2):
    likesGrowth = v2[1] - v1[1] # difference of likes 
    dislikesGrowth = v2[2] - v1[2] # difference of dislikes 
    # prep & return the new value keeping the category of the first appearance 
    return [v1[0], likesGrowth, dislikesGrowth]

def mapDislikesTrend(line):
    key = line[0]
    category = line[1][0]
    likesGrowth = line[1][1]
    dislikesGrowth = line[1][2]
    # calculate trend dislikesGrowth - likesGrowth 
    trend = dislikesGrowth - likesGrowth
    return (key[0],trend, category, key[1])