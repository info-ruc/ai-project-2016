import nltk
import numpy
import re
from nltk import word_tokenize
import string
import re
import operator
import sys
import math
from nltk.corpus import stopwords

stop=open('newstopwords.txt') 
newstop=[]
for line in stop:
	newstop.append(line[:-1])

def openfile(filename):
	
	f = open(filename, 'rU')
	raw= f.read()
	raw = unicode(raw, errors='ignore')
	f.close()
	return raw

def make_seg(filename,Dir,frequency=0):
	raw=openfile(filename)
	tokens = word_tokenize(raw)
	tokens=[t.lower() for t in tokens if t not in string.punctuation and t.isalpha()]
	lemmatizer = nltk.WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]
	stopwords1 = stopwords.words('english')
	tokens = [token for token in tokens if token not in stopwords1]
	tokens = [token for token in tokens if token not in newstop]
	fdist = nltk.FreqDist(tokens)
	tokens = ([w for w in tokens if len(w)> 3 and fdist[w]>frequency])
	filename = filename.split("/")[-1][:-4]
	f = open(Dir+filename+".txt","w")
	f.write(' '.join(tokens)+'\n')
	f.close()
	return fdist
def norm(d):
	n=0.0
	for val in d.values():
		n = n+val*val
	return math.sqrt(n)

