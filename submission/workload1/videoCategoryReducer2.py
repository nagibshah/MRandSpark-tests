#!/usr/bin/python3
import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin)
        Input format:  key \t value
        Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)


def videoCategoryReducer2():
    """ This reducer reads in video category, country:count key-value pairs and returns the
    average count per category by sum(count)/num of country 
    Input format: category \t {video_id=1}
    Output format: category:average
    """

    category_video_counts = {}  
    data = read_map_output(sys.stdin)
    
    for category, video_id_counts in data: 
        # split the country counts by , delimiter and then by = to get a list of counts only
        count_list = [int(video_id.split("=")[1]) for video_id in video_id_counts.split(",")] 
        # [sum(x) for x in zip(list1, list2)]
        total = sum(count_list)
        avg = total / len(count_list)
        # now print out the results 
        print("{0}: {1}".format(category, round(avg,2)))

if __name__ == "__main__":
    videoCategoryReducer2()
