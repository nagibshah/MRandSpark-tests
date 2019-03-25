#!/usr/local/bin/python3 

import sys
import csv

def videoCategoryMapper():
    """ This mapper select categories and return the country trend (country count) information. 
    Input format: video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,
                    comment_count,ratings_disabled,video_error_or_removed,country
    Output format: category \t country=count \t country
    """

    reader = csv.reader(sys.stdin, delimiter=',')
    next(reader) # skip the header row 
    #reader.next() 
    for line in reader:
        video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,\
        comment_count,ratings_disabled,video_error_or_removed,country = line 
        print("{0}\t{1}=1\t{2}".format(category, video_id, country))

if __name__ == "__main__":
    videoCategoryMapper()
