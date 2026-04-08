# coding: utf-8
import csv
import time
from kafka import KafkaProducer

# 实例化一个KafkaProducer示例，用于向Kafka投递消息
producer = KafkaProducer(bootstrap_servers='kafka2:9093')
# 打开数据文件
csvfile = open("/home/ldzh/下载/data_set/BigDataApplicationPractice/int.exp1/user_log.csv","r")
# 生成一个可用于读取csv文件的reader
reader = csv.reader(csvfile)
#for line in reader:
#    gender = line[9] # 性别在每行日志代码的第9个元素
#    if gender == 'gender':
#        continue # 去除第一行表头
#    time.sleep(1) # 每隔1秒发送一行数据
#    producer.send('testkafka',line[9].encode('utf8'))
for line in reader:
    action = line[7]
    age_range = line[8] # 性别在每行日志代码的第8个元素
    gender = line[9]
    province = line[10]
    if action == 'action' or age_range == 'age_range' or gender == 'gender' or province == 'province':
        continue # 去除第一行表头
    time.sleep(0.1) # 每隔1秒发送一行数据
    totalcontent = line[7]+','+line[8]+','+line[9]+','+line[10]
    producer.send('testkafka',totalcontent.encode('utf8'))
    print(totalcontent.encode('utf8'))
    #print(line[10].encode('utf8').decode('utf8'))
