# -*- coding:utf8 -*-
import string
import os

# 构建停用词表
stop_words = open('stop_words_2.txt', 'r').read().strip().split('\n')
stopwords = [sw.strip() for sw in stop_words]
print stopwords

# 对每个文件进行预处理
for filename in os.listdir('neg_txt'):
    print filename
    fin = open('neg_txt/'+filename, 'r')
    fout = open('neg/'+filename, 'w+')
    content = fin.read()
    # 去标点去数字
    identify = string.maketrans('', '')
    punc_dig = string.punctuation + string.digits
    new_content = content.translate(identify, punc_dig)
    # 小写
    new_content = new_content.lower()
    # 去停用词
    words = new_content.replace('\n',' ').split(' ')
    rst = ''
    for w in words:
        if w in stopwords:
            continue
        else:
            rst += w + ' '

    fout.write(rst)
    fin.close()
    fout.close()

