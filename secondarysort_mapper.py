#!/usr/bin/python3
#coding=utf-8
import sys

for line in sys.stdin:
    # 清除掉头部和尾部多余的回车换行之类的符号
    line = line.strip()
    cellphone, rest_info = line.split('\t', 1)
    print('%s\t%s' %(cellphone,rest_info))
    


    