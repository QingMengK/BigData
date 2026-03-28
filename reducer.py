#!/usr/bin/python3
#coding=utf-8

from operator import itemgetter
import sys

record_word = None
record_count = 0
word = None

for line in sys.stdin:
    words = line.strip()
    # 清除掉头部和尾部多余的回车换行之类的符号
    word, count = words.split('\t')
    # word中存放mapper产生的中间结果的key，这里就是例如买家ID之类的项目
    # count中存放mapper产生的中间结果的value，这里就是字符'1'
    
    try:
        count = int(count)
        # 字符1变为数值1，为了和后续对value做累加计算时方便
        # 字符是拼接，数值才是累加
    except ValueError:
        continue

    if record_word == word:
        # 如果record_word等于word，说明现在处理的这个word正在被计数
        # 所以record_count计数行为持续进行，实现＋1操作，这里1就是count数值化后的1
        # 第一次执行因为record_word是空的，所以这个if肯定要跳过去
        record_count += count
    else:
        # 第一次执行，因为record_word为空，肯定定要进入这个else
        # 第一次执行，record_word为空，所以一定会把正在处理的word赋给record_word
        # 第一次执行，record_word为空，所以一定会把正在处理的count赋给record_count
        if record_word:
            # 第二次执行或者第n次执行，在第二次处理的word内容和保存前一次处理结果的record_word的内容不一致时
            # 此时表明统计个数的key已经发生了改变，所以此时应该讲前面统计的record_word的数量record_count输出print出来
            # 因为模拟时使用sort和MapReduce的shuffle存在，所以reducer处理的输入部分内容都是mapper结果根据key排序后的内容
            # 因为有排序，所以reducer的输入中一旦key的部分发生变化，则一定是开启新计数，不会有二次对同一个key计数的可能
            print ('%s\t%s' %(record_word, record_count))
        record_count = count
        record_word = word

if record_word == word:
    # 最后一次执行，不在接收到系统发来的单行文本
    # 此时record_word和record_count的内容应该被输出，但是没有新的输入到来
    # 所以这个最后的剩下的record_word和record_count需要人为输出
    # 如果剩下的record_word和record_count仍处于计数状态，那么就直接print
    print ('%s\t%s' %(record_word, record_count))
    # 如果剩下的record_word和record_count不处于计数状态，即record_word和word不一致，那么在前面的for中会自动print，因此这里不需要考虑该情况



