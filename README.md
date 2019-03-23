# MapReduce & Spark Workloads
MapReduce &amp; Spark Analysis Workloads

## Prep

1. Ensure Hadoop us running. 
2. Ensure the HADOOP_HOME environment variable is set  
3. Copy to hdfs folder 
```
hadoop fs -put [host file location] [hdfs file location]
```
4. python3 interpreter location must be proper (update the #! statement) - must point to the python3 binaries folder
```
#!/usr/bin/python3 
```

## Running on local workload 

1. navigate to the "/mapreduce/combiner" folder 
2. Set the right permission on the shell script files (only for local machine execution)
```
chmod +x videoCategoryCountryAggregator.sh
```
3. Update the shell sript file to increase the number of reducers if required 
4. Execute the shell script 
```
./videoCategoryCountryAggregator.sh input_files/AllVideos_short.csv out_results
```
5. Wait for the success message 
6. View the contents of the file (cat head or tail) - NOTE: the execution of the script writes output to "out_results" folder. 
```
hadoop fs -cat out_results/part-00000 | tail -10
```
7. If a re-run is required please ensure either a new output folder is specified. Alternatively, the previous output folder and its content must be deleted first 


## Running on EMR 
