# -*-coding:utf-8 -*-
import os
import re
from math import fabs
separator = re.compile(r'[!?.\n\t\r]')
paragraphSeparator = set(['!','?','.'])
separator2 = re.compile(r'[!?.]')
def createGraph(fileName):
    G = nx.Graph()
    with open(fileName,'r') as f:
        curParagraph = ''
        for line in f:
            line = line.strip()
            if len(line.split(' ')) < 5: continue
            if line and line[-1] in paragraphSeparator:
   
                curParagraph = curParagraph + ' '+line
                curParagraph = separator2.sub('',curParagraph)
                words = curParagraph.split(' ')
                i , lenWords = 1 , len(words)
                while i < lenWords:
                    if not words[i] and not words[i-1]:
                        del(words[i])
                        lenWords-=1
                    else:  i+=1
                    
                if lenWords >=2:
                    one , two = words[0] , words[1]
                    if one and two: G.add_edge(one,two)
                    for i in xrange(2,len(words)):
                        three = words[i]
                        if one and three: G.add_edge(one,three)
                        if two and three: G.add_edge(two,three)
                        one , two = two ,three
             
                curParagraph=''
            else:
                curParagraph +=line
            
    degrees = nx.degree(G) 
    temp = sum([degrees[x] for x in degrees])
    
    try:
        node = nx.number_of_nodes(G)           
        edges= nx.number_of_edges(G)         
        avgDegree =  temp / nx.number_of_nodes(G)       
        avgShort = nx.average_shortest_path_length(G)    
        r = nx.diameter(G)                     
        clu = nx.average_clustering(G)             
        feature = [
                    node *1.0/1849 ,               
                    edges *1.0/12044 ,              
                    avgDegree *1.0  /14  ,           
                    avgShort *1.0/3.84,             
                    r *1.0/18,                      
                    clu / 0.597602193129          
                ]
        return feature
    except Exception, e:
            print e
def getTestCaseForJudge(path):
    test_input ,fileNames = [],[] 
    with open(path,'r') as f:
        for line in f:
            line = line.strip()
            content = line.split(' ')
            fileName = content[0]
            fileNames.append(fileName)
            temp = []
            for i in content[1:-1]:
                temp.append(float(i))
            test_input.append(temp)
    return fileNames,test_input, [content[-1] for i in xrange(len(test_input))]

def getTestCase(path):
    saveFile = './data/merge.data'
    with open(saveFile,'w') as f:
        f.write('')
    files = os.walk(path).next()[-1]
    for i , fileName in enumerate(files):
        print i , fileName
        temp_tag = False if fileName.find('scimakelatex')!=-1 else True
        feature = createGraph(path+fileName)
        if feature:
            feature = ' '.join(str(k) for k in feature) + ' ' +str(temp_tag)
            with open(saveFile,'a+') as f:
                f.write(fileName+' '+feature+'\n')
def freq(path,num,isTrain=True):
    frequencies = {}
    files = os.walk(path).next()[-1][:num] if isTrain else os.walk(path).next()[-1][num:] 
    for fileName in files:
        content = ''
        with open(path + '/' + fileName, 'r') as f:
            content = f.read()
        content = separator.sub(' ', content)
        words = content.split(' ')
        curDic = {}
        for word in words:
            if word:
                curDic.setdefault(word, 0)
                curDic[word] += 1
                
        frequencies[fileName] = curDic
    return frequencies


def similarity(dicA, dicB):
    NA = sum([cnt for word, cnt in dicA.items()])
    NB = sum([cnt for word, cnt in dicB.items()])
    rate = NA * 1.0 / NB
    dis = 0
    for word in dicA:
        if word  in dicB: dis = dis + fabs(dicA[word] - dicB[word] * rate)
        elif (dicA[word] >> 1) != 0: dis = dis + dicA[word]
    for word in dicB:
        if word not in dicA : dis = dis + dicB[word]
    return dis * 1.0 / (NA << 1)
