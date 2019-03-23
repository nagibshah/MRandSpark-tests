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
    Input format: category \t {country=1}
    Output format: category \t {country=count}
    """
    current_category = ""
    country_count = {} # dictionary 

    data = read_map_output(sys.stdin)
    for category, countrycounts in data:
        if current_category != category:

            if current_category != "":
                output = current_category + "\t"
                i = 0
                for country, count in country_count.items():
                    if i < len(country_count)-1:
                        output += "{}={},".format(country, count)
                    else: 
                        output += "{}={}".format(country, count)
                    i += 1
                print(output.strip())

            current_category = category
            country_count = {}

        for countrycount in countrycounts.strip(",").split(","):
            country, count = countrycount.strip().split("=")
            country_count[country] = country_count.get(country, 0) + int(count)

    if current_category != "":
        output = current_category + "\t"
        i = 0
        for country, count in country_count.items():
            if i < len(country_count)-1:
                output += "{}={},".format(country, count)
            else: 
                output += "{}={}".format(country, count)
            i += 1
        print(output.strip())

if __name__ == "__main__":
    videoCategoryCombiner()
