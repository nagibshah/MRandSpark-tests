#!/usr/local/bin/python3 
import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin)
        Input format:  key \t value
        Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)


def videoCategoryReducer():
    """ This reducer reads in video category, country:count key-value pairs and returns the
    average count per category by sum(count)/num of country 
    Input format: category \t {country=1}
    Output format: category:average
    """
 
    data = read_map_output(sys.stdin)
    for category, countrycounts in data: 
        # split the country counts by , delimiter and then by = to get a list of counts only
        count_list = [int(country.split("=")[1]) for country in countrycounts.split(",")] 
        total = sum(count_list)
        avg = total / len(count_list)
        # now print out the results 
        print("{0}: {1}".format(category, avg))

if __name__ == "__main__":
    videoCategoryReducer()
