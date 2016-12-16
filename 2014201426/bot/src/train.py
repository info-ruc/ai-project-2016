#!/usr/bin/python

f1 = open('data/tag.txt', 'r')
f2 = open('data/train.txt', 'w')
f3 = open('data/test.txt','w')

num=[12000, 11999,9955,7939,8000,7378,9680,10000,12000,8000,10000,12000]
num2=[12000,11990,9950,7930,8000,7370,9660,10000,12000,8000,10000,12000]
#94900 data/train.txt
#24000 data/test.txt

i=-1
j=0

for line in f1:
    if line.find(' '+str(i)) == -1:
        i=i+1
        print i-1,j
        j=0
        f3.write(line)
    else:
        if j<2000:
            f3.write(line)
        elif j<num2[i]:
            f2.write(line)
    j=j+1




f1.close()
f2.close()
f3.close()


