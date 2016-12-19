# -*- coding:utf8 -*-
import re
import os

fout = open('vec.txt', 'w+')
for filename in os.listdir('neg'):
    line = '0 '
    # 生成每个文件的词频向量
    fin = open('neg/'+filename, 'r')
    dict = {}
    content = fin.read()
    words = content.replace('\n', ' ').split(' ')
    for word in words:
        if len(word.strip()) > 1:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    sorted_dict = sorted(dict.iteritems(), key=lambda d:d[1], reverse=True)

    num = 0
    for _ in sorted_dict:
        if num<300:
            line += str(num) + ':' +str(_[1]) + ' '
            num = num + 1

    fout.write(line+'\n')
    fin.close()

for filename in os.listdir('pos'):
    line = '1 '
    # 生成每个文件的词频向量
    fin = open('pos/'+filename, 'r')
    dict = {}
    content = fin.read()
    words = content.replace('\n', ' ').split(' ')
    for word in words:
        if len(word.strip()) > 1:
            if word in dict:
                dict[word] = dict[word] + 1
            else:
                dict[word] = 1
    sorted_dict = sorted(dict.iteritems(), key=lambda d:d[1], reverse=True)

    num = 0
    for _ in sorted_dict:
        if num<300:
            line += str(num) + ':' +str(_[1]) + ' '
            num = num + 1

    fout.write(line+'\n')
    fin.close()


fout.close()