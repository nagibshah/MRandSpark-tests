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
        Input format: category \t {video_id=1}
        Output format: category:average
        """
    
        category_video_counts = {}  
        video_id_list = {}
        data = read_map_output(sys.stdin)
    
        for category, video_id_counts in data: 
                # split the country counts by , delimiter and then by = to get a list of counts only
                if category_video_counts.get(category) != None:

                        count_list = [int(video_id.split("=")[1]) for video_id in video_id_counts.split(",")] 
                        category_video_counts[category] = [sum(x) for x in zip(count_list, category_video_counts.get(category))] 
                else:
                        # value exists set the dictionary for the first time 
                        category_video_counts[category] = [int(video_id.split("=")[1]) for video_id in video_id_counts.split(",")]
                        video_id_list[category] = [str(video_id.split("=")[0]) for video_id in video_id_counts.split(",")] 

        # print out all the values from the dictionary for the final reducer 
        for category, counts in category_video_counts.items():
                output = category + "\t"
                i = 0
                videoid = list(video_id_list.get(category))
                for count in counts: 
                        if i < len(counts)-1:
                                output += "{}={},".format(videoid[i], count)
                        else: 
                                output += "{}={}".format(videoid[i], count)
                        i += 1
                print(output.strip())
                

if __name__ == "__main__":
    videoCategoryReducer()
