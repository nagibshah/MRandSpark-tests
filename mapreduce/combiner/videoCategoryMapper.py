#!/usr/local/bin/python3 

import sys
import csv

def videoCategoryMapper():
    """ This mapper select categories and return the country trend (country count) information. 
    Input format: video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,
                    comment_count,ratings_disabled,video_error_or_removed,country
    Output format: category \t country=count
    """

    reader = csv.reader(sys.stdin, delimiter=',')
    next(reader) # skip the header row 
    #reader.next() 
    for line in reader:
        video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,\
        comment_count,ratings_disabled,video_error_or_removed,country = line 
        print("{0}\t{1}=1".format(category, country))

    """ 
    for line in sys.stdin:
        # Clean input and split it
        line = line.strip()
        stats = line.split(",")

        # Check that the line is of the correct format
        if len(stats) != 12:
          continue

        # zero based index when retrieving values 
        # key:value pairs 
        country = stats[11].strip()
        #video_id = stats[0].strip()
        category = stats[3].strip()

        print("{}\t{}=1".format(category, country))
    """

if __name__ == "__main__":
    videoCategoryMapper()
