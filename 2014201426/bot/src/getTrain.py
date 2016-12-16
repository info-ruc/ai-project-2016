#!/usr/bin/python 
# coding:utf-8
import os

name=["cat", "dog", "giraffe", "hyena", "sikadeer", "weasel", "chipmunk", "fox", "guinea\ pig", "reindeer", "squirrel", "wolf"]
gs=["jpg","jpeg","gif","png"]

s1="find ~/BOT/data/"
s2=''' -name \*.'''
s3=''' | cut -b '''
s7='''- | sed "s/$/ '''
s4='''/">>~/BOT/data/'''
s5="/tag.txt"

os.system("rm  ~/BOT/data/tag_all.txt")

for i in xrange(len(name)):
    na=name[i]
    os.system("rm  ~/BOT/data/"+na+"/train.txt")
    os.system("rm  ~/BOT/data/"+na+"/tag.txt")
    for j in xrange(4):
        ll=len(na)
        if i==8:
            ll=ll-1
        s=s1+na+s2+gs[j]+s3+str(17+ll)+s7+str(i)+s4+na+s5
        os.system(s)
        if  j==0:
            print s
    os.system("wc -l  ~/BOT/data/"+na+"/tag.txt")

for i in xrange(len(name)):
    os.system('''cat  ~/BOT/data/'''+name[i]+'''/tag.txt>> ~/BOT/data/tag_all.txt''')
os.system("wc -l  ~/BOT/data/tag_all.txt")