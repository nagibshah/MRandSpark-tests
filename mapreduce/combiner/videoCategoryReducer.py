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
        sum of each video id country appearances per category. Sum is only carried out for matching
        videoids.  
        Input format: category \t {video_id=count}
        Output format: category \t {count}
        """

        category_video_counts = {}  
        video_id_list = {}
        data = read_map_output(sys.stdin)
    
        for category, video_id_counts in data: 
                vididList = []
                vidcountList = []
                for record in video_id_counts.split(","):
                    vididList.append(record.split("=")[0]) 
                    vidcountList.append(int(record.split("=")[1])) 
                current_counts = dict(list(zip(vididList, vidcountList)))  

                # split the country counts by , delimiter and then by = to get a list of counts only
                if category_video_counts.get(category) != None:
                        # category entry in dictionary exists 
                        # check the video id to match before summing
                        existingCountsDict = category_video_counts.get(category) 
                        for key, value in current_counts.items():
                                existingCountsDict[key] = existingCountsDict.get(key, 0) + value 
                else:
                        # value does not exist set the dictionary for the first time 
                        category_video_counts[category] = current_counts

        # print out all the values from the dictionary for the final reducer 
        for category, counts in category_video_counts.items():
                output = category + "\t"
                i = 0
                for vidid, count in counts.items(): 
                        if i < len(counts)-1:
                                output += "{},".format(count)
                        else: 
                                output += "{}".format(count)
                        i += 1
                print(output.strip())                

if __name__ == "__main__":
    videoCategoryReducer()
