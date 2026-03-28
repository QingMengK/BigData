#!/usr/bin/python3
#coding=utf-8
import sys

for line in sys.stdin:  # 遍历读入数据的每一行
    
    line = line.strip()  # 将行尾行首的空格去除
    words = line.split(',')  #按空格将句子分割成单个单词
    for seq,word in enumerate(words):
        if seq == 0:
            # 清除掉csv文件第一行，第一行是每一列的列头，无数值意义，不计入计数，break            
            if word == 'user_id':
                continue
            else:
                # 如果不是列头，则开始对第一列产生<key,value>
                print ('%s\t%s' %('买家id:'+word, 1))
        elif seq == 1:
            print ('%s\t%s' %('商品id:'+word, 1))
        elif seq == 2:
            print ('%s\t%s' %('商品类别id:'+word, 1))
        elif seq == 3:
            print ('%s\t%s' %('卖家id:'+word, 1))
        elif seq == 4:
            print ('%s\t%s' %('品牌id:'+word, 1))
        elif seq == 5:
            print ('%s\t%s' %('交易时间月:'+word, 1))
        elif seq == 6:
            print ('%s\t%s' %('交易时间日:'+word, 1))
        elif seq == 7:
            if word == '0':
                print ('%s\t%s' %('买家行为点击商品:', 1))
            elif word == '1':
                print ('%s\t%s' %('买家行为放购物车:', 1))
            elif word == '2':
                print ('%s\t%s' %('买家行为购买商品:', 1))
            elif word == '3':
                print ('%s\t%s' %('买家行为放收藏夹:', 1))
            else:
                pass
        elif seq == 8:
            if word == '0':
                print ('%s\t%s' %('买家年龄 0-17岁:', 1))
            elif word == '1':
                print ('%s\t%s' %('买家年龄18-24岁:', 1))
            elif word == '2':
                print ('%s\t%s' %('买家年龄25-29岁:', 1))
            elif word == '3':
                print ('%s\t%s' %('买家年龄30-34岁:', 1))
            elif word == '4':
                print ('%s\t%s' %('买家年龄35-39岁:', 1))
            elif word == '5':
                print ('%s\t%s' %('买家年龄40-49岁:', 1))
            elif word == '6':
                print ('%s\t%s' %('买家年龄50岁以上:', 1))
            else:
                pass
        elif seq == 9:
            if word == '1':
                print ('%s\t%s' %('买家男性:', 1))
            elif word == '0':
                print ('%s\t%s' %('买家女性:', 1))
            else:
                pass            
        elif seq == 10:
            print ('%s\t%s' %('买家省份:'+word, 1))
        else:
            pass

