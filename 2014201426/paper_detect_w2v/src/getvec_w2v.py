#!/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from gensim.models import word2vec
import numpy as np
from gensim.models import word2vec
from sklearn import preprocessing



def main(datapath,ss):


    if not datapath.endswith('/'):
        datapath=datapath+'/'

    model=word2vec.Word2Vec(size=128,window=6,cbow_mean=0,sample=1e-4,hs=1,negative=0,workers=12)

    model=word2vec.Word2Vec.load("w2v/"+'_'.join(datapath.split('/'))+'_word2vec')

    fin=file(datapath+'segment.dat','r')
    fout=file(datapath+'vec_w2v.dat','w')

    idx=0

    wa=0

    for line in fin:
        idx+=1
        if idx%1000==0:
            print idx
        line=line.split()
        vec=np.zeros(128)
        for word in line:
            #word=word.decode('utf-8')
            try:
                vec=vec+model[word]
            except:
                wa+=1
        fout.write(str(ss)+' ')
        vec=preprocessing.normalize(vec)[0]
        for i,num in enumerate(vec):
            fout.write(str(1+i)+":"+str(num)+' ')
        fout.write('\n')    
     
    fin.close()
    fout.close()   
    print "wa:"+str(wa)



if __name__ == '__main__':
    main("Train/True/",1)  
    main("Test/True/",1)  
    main("Train/False/",0)  
    main("Test/False/",0)  
