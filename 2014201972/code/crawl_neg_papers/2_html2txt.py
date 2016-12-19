# -*- coding:utf8 -*-
# 去标签
from bs4 import BeautifulSoup

for i in range(1000):
    print i
    infile = open('neg_html_3/' + str(i) + '.txt', 'r')
    outfile = open('neg_txt/' + str(i) + '.txt', 'w+')
    source_code = infile.read()
    soup = BeautifulSoup(source_code, 'lxml')
    text = soup.get_text()
    outfile.write(text.encode('utf-8'))

