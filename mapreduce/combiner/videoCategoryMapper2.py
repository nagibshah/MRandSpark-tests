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
    """ This mapper behaves like an identity mapper only for grouping and sorting purposes. 
    Input format: category \t value 
    Output format: category \t value
    """

    data = read_map_output(sys.stdin)

    for category, video_id_counts in data: 
        print("{0}\t{1}".format(category, video_id_counts))

if __name__ == "__main__":
    videoCategoryMapper2()
