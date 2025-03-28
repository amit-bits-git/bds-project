hadoop fs -mkdir /mydata
hadoop fs –mkdir /mydata/testfolder
hadoop fs -put fitnessdata.txt /mydata/testfolder


hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file mapper_fitness_1.py -file reducer_fitness_1.py -mapper "python mapper_fitness_1.py" -reducer "python reducer_fitness_1.py" -input /mydata/testfolder/fitnessdata.txt -output /mydata/testfolder/wordcount
hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file mapper_fitness_2.py -file reducer_fitness_2.py -mapper "python mapper_fitness_2.py" -reducer "python reducer_fitness_2.py" -input /mydata/testfolder/fitnessdata.txt -output /mydata/testfolder/wordcount2
hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file mapper_fitness_3.py -file reducer_fitness_3.py -mapper "python mapper_fitness_3.py" -reducer "python reducer_fitness_3.py" -input /mydata/testfolder/fitnessdata.txt -output /mydata/testfolder/wordcount3
hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file mapper_fitness_4.py -file reducer_fitness_4.py -mapper "python mapper_fitness_4.py" -reducer "python reducer_fitness_4.py" -input /mydata/testfolder/fitnessdata.txt -output /mydata/testfolder/wordcount4
hadoop jar /opt/hadoop-3.2.4/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar -file mapper_fitness_5.py -file reducer_fitness_5.py -mapper "python mapper_fitness_5.py" -reducer "python reducer_fitness_5.py" -input /mydata/testfolder/fitnessdata.txt -output /mydata/testfolder/wordcount5

hadoop fs -cat /mydata/testfolder/wordcount/part*
hadoop fs -cat /mydata/testfolder/wordcount2/part*
hadoop fs -cat /mydata/testfolder/wordcount3/part*
hadoop fs -cat /mydata/testfolder/wordcount4/part*
hadoop fs -cat /mydata/testfolder/wordcount5/part*
