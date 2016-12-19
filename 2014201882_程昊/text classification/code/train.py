#coding=utf-8

from gensim import models 

print "preprocess"
documents = models.doc2vec.TaggedLineDocument("zuowenfenci.dat")
model = models.doc2vec.Doc2Vec(dm=0, # DBOW
				size=128,
				window=8,
				min_count=5,
				dbow_words = 1) # DBOW, simultaneously train word vectors with doc vectors

print "build vocab"
model.build_vocab(documents)
print "train model"
model.train(documents)
print "save"
model.save('doc2vec_fenju_128')

