from utils import *
import os,sys
import math

traindir = "TXT-final/True/"
testdir = "TXT-final/False/"

files = os.listdir(traindir)
cnt = 0
for f in files:
	cnt+=1
	if cnt%100==0:
		print cnt
	make_seg(traindir+f,Dir='segment/True/')
files = os.listdir(testdir)
cnt=0
for f in files:
	cnt+=1
	if cnt%100==0:
		print cnt
	make_seg(testdir+f,Dir='segment/False/')
files = os.listdir('segment/True/Train/')
cnt=0
ff = open("Train/True/segment.dat",'w')
for f in files:
	cnt+=1
	if cnt%100==0:
		print cnt
	f2 = open('segment/True/Train/'+f,'r')
	ff.write(f2.readline())
	f2.close()
ff.close()
files = os.listdir('segment/False/Train/')
cnt=0
ff = open("Train/False/segment.dat",'w')
for f in files:
	cnt+=1
	if cnt%100==0:
		print cnt
	f2 = open('segment/False/Train/'+f,'r')
	ff.write(f2.readline())
	f2.close()
ff.close()
files = os.listdir('segment/True/Test/')
cnt=0
ff = open("Test/True/segment.dat",'w')
for f in files:
	cnt+=1
	if cnt%100==0:
		print cnt
	f2 = open('segment/True/Test/'+f,'r')
	ff.write(f2.readline())
	f2.close()
ff.close()
files = os.listdir('segment/False/Test/')
cnt=0
ff = open("Test/False/segment.dat",'w')
for f in files:
	cnt+=1
	if cnt%100==0:
		print cnt
	f2 = open('segment/False/Test/'+f,'r')
	ff.write(f2.readline())
	f2.close()
ff.close()
