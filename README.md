# hadoop-mini-project
Accident count by automobile make and year by using MapReduce method. 


1. The mapper1 will generate the key value pairs for vehicle VIN_number as a key and vehicle model, year and incident type as a tuple
2. The reducer1 will capture the vehicle model and year as key and accident count as value
3. The mapper2  will pass the key-value from reducer1
4. The reducer2 will combine the total accident count for the key vehicle model and year and total accident count.

To execute the MapReduce in the Virtual machine

1. Create two HDFS folders /input and /output
2. Upload data.csv to  /input folder
3. Upload mapper1.py, reducer1.py, mapper2.py, reducer2.py, hadoop_bash.sh into /home/cloudera/MapReduce folder
4. Run the shell script using the bash command "bash hadoop_bash.sh" in /home/cloudera/MapReduce folder 
5. Verify result in /output/result.txt file 
