#!/usr/local/bin/python3 

import sys

def read_map_output(file):
        """ Return an iterator for key, value pair extracted from file (sys.stdin)
                Input format:  key \t value
                Output format: (key, value)
        """
        for line in file:
                yield line.strip().split("\t", 1)

def videoCategoryMapper2():
    """ This mapper select categories and return the country trend (country count) information. 
    Input format: video_id,trending_date,category_id,category,publish_time,views,likes,dislikes,
                    comment_count,ratings_disabled,video_error_or_removed,country
    Output format: category \t country=count \t country
    """

    data = read_map_output(sys.stdin)

    for category, video_id_counts in data: 
        print("{0}\t{1}".format(category, video_id_counts))

if __name__ == "__main__":
    videoCategoryMapper2()
