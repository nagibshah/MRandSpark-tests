# MapReduce Workload
MapReduce &amp; Spark Analysis Workloads

## Prep

1. Ensure Hadoop us running. 
2. Ensure the HADOOP_HOME environment variable is set  
3. Copy the data file to hdfs folder 
```
hadoop fs -put [host file location] [hdfs file location]
```
4. python3 interpreter location must be proper (update the #! statement) - must point to the python3 binaries folder
```
#!/usr/bin/python3 
```

## Running on local workload 

1. navigate to the "/mapreduce/combiner" folder 
2. Set the right permission on the shell script files
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

Ensure EMR is started in with m5.xlarge (1 instance). Also ensure that the security groups are configured to allow SSH connections

1. SSH to the EMR instance 
```
ssh -i ~/<PATH TO PEM FILE>/<NAME>.pem hadoop@<EMR PUBLIC DNS>
```
2. Install git on EMR 
```
sudo yum install git 
```
3. Clone the git repo containing the codebase 
```
git clone <git repo url>
```
4. Copy the data file via SCP to EMR. Replace the paths with the appropriate values. NOTE: File will be copied to hadoop users directory 
```
scp -i ~/<PATH TO PEM FILE>/<NAME>.pem <PATH TO INPUT DATA FILE>/AllVideos_short.csv hadoop@<EMR PUBLIC DNS>:~
AllVideos_short.csv
```
5. Copy the data file to hdfs folder 
```
hadoop fs -mkdir input_files
hadoop fs -put AllVideos_short.csv input_files/AllVideos_short.csv
```
6. Set the right permission on the shell script files in the "workload1" folder 
```
chmod +x videoCategoryCountryAggregator_emr.sh
```
7. Update the shell sript file to increase the number of reducers as required 
8. Execute the shell script 
```
./videoCategoryCountryAggregator_emr.sh input_files/AllVideos_short.csv out_results
```
9. Wait for the success message 
10. View the contents of the file (cat head or tail) - NOTE: the execution of the script writes output to "out_results" folder. 
```
hadoop fs -cat out_results/part-00000 | tail -10
```
11. If a re-run is required please ensure either a new output folder is specified. Alternatively, the previous output folder and its content must be deleted first

# Spark Workload
Spark Analysis Workloads

Ensure EMR (Spark: Spark 2.4.0 on Hadoop 2.8.5 YARN with Ganglia 3.7.2 and Zeppelin
0.8) is started in with m5.xlarge (1 instance). Also ensure that the security groups are configured to allow SSH connections 

1. SSH to the EMR instance 
```
ssh -i ~/<PATH TO PEM FILE>/<NAME>.pem hadoop@<EMR PUBLIC DNS>
```
2. Install git on EMR 
```
sudo yum install git 
```
3. Clone the git repo containing the codebase 
```
git clone <git repo url>
```
4. Copy the data file via SCP to EMR. Replace the paths with the appropriate values. NOTE: File will be copied to hadoop users directory 
```
scp -i ~/<PATH TO PEM FILE>/<NAME>.pem <PATH TO INPUT DATA FILE>/AllVideos_short.csv hadoop@<EMR PUBLIC DNS>:~
AllVideos_short.csv
```
5. update the bash profile to include "PYSPARK_PYTHON" environment variable and set the value to "python3"
```
echo PYSPARK_PYTHON=python3
```
NOTE: reload the bash profile with source command
6. browse to the repo "workload2" (cd workload2)
7. Ensure the shell file has executable rights 
```
chmod +x emr_submit.sh
```
8. Run the following command to execute the spark job (first param is input file and 2nd param is output folder) 
```
./emr_submit.sh file:///home/hadoop/AllVideos_short.csv file:///home/hadoop/top10out
```
9. Wait until the job is completed without any errors and open via an editor to verify content 
```
nano ~/top10out/part-00000
```
