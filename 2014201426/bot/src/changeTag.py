#!/usr/bin/python

f1 = open('data/tag_all.txt', 'r')
f2 = open('data/tag.txt','w')


num=[12000, 11999,9955,7939,8000,7378,9680,10000,12000,8000,10000,12000]
num2=[12000,11990,9950,7930,8000,7370,9660,10000,12000,8000,10000,12000]
#94900 data/train.txt
#24000 data/test.txt

for line in f1:
    line=line.replace("png","jpg")
    line=line.replace("jpeg","jpg")
    line=line.replace("gif","jpg")
    f2.write(line)



f1.close()
f2.close()



