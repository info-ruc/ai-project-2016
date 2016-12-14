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
	return raw

def make_token(filename,frequency=5):
	raw=openfile(filename)
	tokens = word_tokenize(raw)
	tokens=[t.lower() for t in tokens if t not in string.punctuation and t.isalpha()]
	lemmatizer = nltk.WordNetLemmatizer()
	tokens = [lemmatizer.lemmatize(token) for token in tokens]
	stopwords1 = stopwords.words('english')
	tokens = [token for token in tokens if token not in stopwords1]
	tokens = [token for token in tokens if token not in newstop]
	fdist = nltk.FreqDist(tokens)
	tokens = ([w for w in tokens if len(w)> 4 and fdist[w]>frequency])
	fdist = nltk.FreqDist(tokens)
	return fdist

def make_token_ori(filename,frequency=5):
	raw=openfile(filename)
	tokens = word_tokenize(raw)
	tokens=[t.lower() for t in tokens if t not in string.punctuation]
	fdist = nltk.FreqDist(tokens)
	tokens = ([w for w in tokens if len(w)> 4 and fdist[w]>frequency])
	fdist = nltk.FreqDist(tokens)
	return fdist

def norm(d):
	n=0.0
	for val in d.values():
		n = n+val*val
	return math.sqrt(n)

def similarity(ftoken):
	similar = []
	for d in data:
		val = 0.0
		for key in ftoken.keys():
			val = val+ftoken[key]*d[0][key]
		if(not ftoken or not d[0]):
			continue
		val = val/norm(ftoken)
		val = val/norm(d[0])
		l = []
		l.append(val)
		l.append(d[-1])
		similar.append(l)
	return similar

def classify(vector, folders):
	knnclass = ""
	maxsum = 0.0
	for folder in folders:		
		s = 0.0
		for v in vector:
			if(v[1]==folder):
				s = s+v[0]
			if(s>maxsum):
				maxsum = s
				knnclass = v[1]
	return knnclass


