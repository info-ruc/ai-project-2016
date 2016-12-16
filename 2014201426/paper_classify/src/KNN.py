from utils import *
import os,sys
import math

traindir = "Dataset/TRAINING/"
testdir = "Dataset/TESTING/"
k=5
folders= os.listdir(traindir)
try:
	frequency = eval(sys.argv[1])
except: 
	frequency=0

totalc=0.0
correct=0.0
print ""
print ""
print "KNN:"
print ""
                         
print "Orignal            Predicted             File_Name"
print "-----------------------------------------------------"

data = []
for folder in folders:
	files = os.listdir(traindir+folder)
	for f in files:
		flist = []
		flist.append(make_token(traindir+folder+"/"+f, frequency=frequency))
		flist.append(folder)
		data.append(flist)

folders = os.listdir(testdir)
for folder in folders:
	files = os.listdir(testdir+folder)
	for f in files:
		totalc+=1
		ftoken = make_token(testdir+folder+"/"+f, frequency=frequency)
		knn = similarity(ftoken)
		knn = sorted(knn,key=lambda l:l[0], reverse=True)
		print folder,classify(knn[0:k], folders),f
		if folder==classify(knn[0:k]):
			correct+=1
	print " "

print "K-Nearest Neighbour Classifier  k=="+str(frequency)+":"+str(correct/totalc*100.0)+"%" 

