# coding: utf-8
import csv

# 打开数据文件
csvfile_src = open("/home/ldzh/data_set/BigDataApplicationPractice/int.exp1/user_log.csv","r")
csvfile_dst = open("/home/ldzh/data_set/BigDataApplicationPractice/exp3/user_log_small.csv","w")

# 生成一个可用于csv文件的对象
reader = csv.reader(csvfile_src)
writer = csv.writer(csvfile_dst)

cnt = 0

for row in reader:
    writer.writerow(row)
    cnt = cnt + 1
    if cnt == 10000:
        break

