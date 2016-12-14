#!/usr/bin/python

import os

name=["cat", "dog", "giraffe", "hyena", "sikadeer", "weasel", "chipmunk", "fox", "guinea\ pig", "reindeer", "squirrel", "wolf"]



for i in xrange(len(name)):
    s1="unrar x /root/BOT/data/"+name[i]+".rar /root/BOT/data/"
    s="cp -r /root/BOT/data/"+name[i]+"/.    /root/BOT/data/pic"
    #print s1
    print s
    #os.system(s1)
    os.system(s)



