#!/usr/bin/python3
#coding=utf-8
import sys

current_cellphone = None
rest_info = []
cellphone = None

for line in sys.stdin:
    tel_rec = line.strip()
    cellphone, datetime, talktime, address = tel_rec.split('\t')
    if current_cellphone != cellphone:
        if rest_info != []:
            rest_info_collection = sorted(rest_info, key=lambda item: (item[0]), reverse=True)
            for records in rest_info_collection:
                print('%s\t%s' %(current_cellphone, '\t'.join(records)))
        current_cellphone = cellphone
        rest_info.clear()
    rest_info.append([datetime, talktime, address])

if rest_info != []:
    rest_info_collection = sorted(rest_info, key=lambda item: (item[0]), reverse=True)
    for records in rest_info_collection:
        print('%s\t%s' %(current_cellphone, '\t'.join(records)))

        

        

