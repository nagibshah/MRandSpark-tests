#!/usr/local/bin/python3 
import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin)
        Input format:  key \t value
        Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)


def videoCategoryCombiner():
    """ This reducer reads in video category, country-counts key-value pairs and returns the
    total sum of country-counts per category in the same format as the input to allow
    the reducer to be used as a combiner.
    Input format: category \t {video_id=1|country}
    Output format: category \t {video_id=count}
    """
    current_category = ""
    country_id_set = set() # set to keep track of id & countries 
    video_id_count = {} # dictionary 

    data = read_map_output(sys.stdin)
    for category, videodata in data:
        video_id_counts = videodata.split("|")[0]
        country = videodata.split("|")[1]

        if current_category != category:

            if current_category != "":
                output = current_category + "\t"
                i = 0
                for video_id, count in video_id_count.items():
                    if i < len(video_id_count)-1:
                        output += "{}={},".format(video_id, count)
                    else: 
                        output += "{}={}".format(video_id, count)
                    i += 1
                print(output.strip())

            current_category = category
            video_id_count = {}

        for videocount in video_id_counts.strip(",").split(","):
            video_id, count = videocount.strip().split("=")
            combo = video_id + "-" + country
            # check if video already appeared in country
            if combo in country_id_set: 
                # do not increment 
                video_id_count[video_id] = video_id_count.get(video_id, 0)
            else: 
                # increment 
                country_id_set.add(combo)
                video_id_count[video_id] = video_id_count.get(video_id, 0) + int(count) 

    if current_category != "":
        output = current_category + "\t"
        i = 0
        for video_id, count in video_id_count.items():
            if i < len(video_id_count)-1:
                output += "{}={},".format(video_id, count)
            else: 
                output += "{}={}".format(video_id, count)
            i += 1
        print(output.strip())

if __name__ == "__main__":
    videoCategoryCombiner()
