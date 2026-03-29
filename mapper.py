#!/usr/bin/python3
#coding=utf-8
import sys


for line in sys.stdin:
    line = line.strip()
    # 清除掉头部和尾部多余的回车换行之类的符号
    '''
    王俊栋:杨  璐,白少东,符式江,郭李萍,于金艳,沈名杰,朱  妍,明佳音,元明亮,栾司琪,王洪洋,王  俪,冉波太,焦美晴,陈  婷
    通讯录所有者是王俊栋，根据：切分出来，给owner
    通讯录中好友名单friends 杨  璐,白少东,符式江,郭李萍,于金艳,沈名杰,朱  妍,明佳音,元明亮,栾司琪,王洪洋,王  俪,冉波太,焦美晴,陈  婷
    根据逗号，逐个切分出来，给列表friend_list
    '''
    owner,friends = line.split(':')
    friend_list = friends.split(',')

    for friend in friend_list:
        '''
        因为朋友是双向关系
        所以A是B的朋友，则B也是A的朋友
        因此会出现<A,B>和<B,A>这两个key
        但是实际上这两个key所对应的value应该进行下一步的reducer计算
        所以让<A,B>和<B,A>这两个key，变成同一个key，通过sort或者shuffle
        则它俩的value就会在一个reducer上被处理
        让这两个key变成同一个key的方法就是遵循一个顺序
        这里设计的顺序就是比较两个字符串owner和friend的大小
        根据字符串的大小，统一key的顺序
        不管key是<A,B>和<B,A>
        value永远都是通讯录中好友名单friends的内容
        '''
        if owner > friend:
            print('<%s,%s>\t[%s]' %(owner, friend, friends))
        else:
            print('<%s,%s>\t[%s]' %(friend, owner, friends))


    