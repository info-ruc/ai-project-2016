# -*-coding:utf-8 -*-
from utils import *

truePath = r'./TXT-final/True'
falsePath = r'./TXT-final/False'
TrueNum = 2500
FalseNum = 1100

trueFre = freq(truePath,TrueNum,isTrain=True)
falseFre = freq(falsePath,FalseNum,isTrain=True)
train_data = dict(trueFre , **falseFre)
train_fileName = [name[0] for i , name in enumerate(train_data.items())]

trueFre = freq(truePath,TrueNum,isTrain=False)
falseFre = freq(falsePath,FalseNum,isTrain=False)
test_data = dict(trueFre , **falseFre)
test_fileName = [name[0] for i , name in enumerate(train_data.items())]

rightNum_real = rightNum_noReal = 0
real_num = noReal_num = 0

k = 3

for fileName , wordCnt in test_data.items():
    tag = False if fileName.find('scimakelatex')!=-1 else True
    if tag: real_num += 1
    else: noReal_num += 1
    distances  = [(fileTrain,similarity(wordCnt, wordCntTrain)) for  fileTrain,wordCntTrain in train_data.items()]
    distances.sort(key=lambda x:x[1])
    truePaper = falsePaper = 0
    for name , dis in distances[:k]:
        temp_tag = False if name.find('scimakelatex')!=-1 else True
        if temp_tag: truePaper+=1
        else: falsePaper+=1
    if truePaper > falsePaper and tag: rightNum_real +=1
    elif truePaper < falsePaper and not tag:rightNum_noReal+=1

print 'T:',real_num
print 'F:', noReal_num  
print 'TP:',rightNum_real 
print 'FN:',rightNum_noReal
print rightNum_real+rightNum_noReal,len(test_data),(rightNum_real+rightNum_noReal) *1.0/len(test_data)
