
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-file /home/cloudera/MapReduce/mapper1.py -mapper "python mapper1.py" \
-file /home/cloudera/MapReduce/reducer1.py -reducer "python reducer1.py" \
-input /input/data.csv -output /output/all_accidents

hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-mr1.jar \
-file /home/cloudera/MapReduce/mapper2.py -mapper "python mapper2.py" \
-file /home/cloudera/MapReduce/reducer2.py -reducer "python reducer2.py" \
-input /output/all_accidents -output /output/result