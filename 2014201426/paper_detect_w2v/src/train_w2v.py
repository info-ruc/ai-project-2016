#!/usr/bin/python
# -*- coding:utf-8 -*-

from gensim.models import word2vec


def main(datapath='data'):

    if not datapath.endswith('/'):
        datapath=datapath+'/'

    documents=word2vec.LineSentence(datapath+'segment.dat')

    model=word2vec.Word2Vec(size=128,window=6,cbow_mean=0,sample=1e-4,hs=1,negative=0,workers=12)

    model.build_vocab(documents)

    model.train(documents)

    model.save('_'.join(datapath.split('/'))+'_word2vec')    

    try:
    	print "ok"
    except:
    	pass

if __name__ == '__main__':
        main("Train/True/")  
        main("Test/True/")  
        main("Train/False/")  
        main("Test/False/")  