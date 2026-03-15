#!/usr/bin/python3
#coding=utf-8
import sys


record_relation = ''
record_common_friends = ''
common_result = []

for line in sys.stdin:
    # 清除掉头部和尾部多余的回车换行之类的符号
    social_relation = line.strip()
    # relation是要寻找的共同好友的两个人
    # common_friends是这两个人中其中一个人的全部好友列表
    # 通过tab切分出来
    relation, common_friends = social_relation.split('\t')
    # 去除掉common_friends结果前后的中括号，美观
    common_friends = common_friends.strip('[]')
    # 如果发现record_relation == relation
    '''
    说明两个相同key的输入内容被遇到
    这时候把这两个相同key对应的不同value进行处理
    两个value分别放在common_friends和record_common_friends
    这两个字符串根据逗号切分成列表
    然后在这两个列表中寻找共同的元素
    共同的元素组成新列表后再通过join变成一个逗号分隔的字符串
    '''
    if record_relation == relation:
        record_common_friends = record_common_friends.split(',')
        common_friends = common_friends.split(',')
        common_result = ','.join([x for x in record_common_friends if x in common_friends])
        '''
        # 调试使用
        print(record_relation)
        print(relation)
        print('record_common_friends: ',record_common_friends)
        print('common_friends: ',common_friends)
        print('common_result: ',common_result)
        '''        
    else:
        '''
        进入到这个else时说明前后两个key不同
        第一次运行时肯定进入这个else
        中间不同的key时也会进入这个else
        '''
        if record_relation:
            # 因为key发生切换，导致key变化
            # 所以应该在key（record_relation）非空时输出前一次key的计算结果common_result
            if common_result != [] and common_result != '':
                print ('%d %s %s' %(common_result.count(',')+1,record_relation, common_result))
            else:
                print ('%d %s %s' %(0,record_relation,common_result))
        #更新record_relation和record_common_friends
        record_relation = relation
        record_common_friends = common_friends

# 最后一次输入到达，把此前的结果输出
# 否则最后一次计算结果可能会留在common_result没有被输出
if record_relation == relation:
    if common_result != [] and common_result != '':
        print ('%d %s %s' %(common_result.count(',')+1,record_relation, common_result))
    else:
        print ('%d %s %s' %(0,record_relation,common_result))
    
