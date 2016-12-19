import string  
import re 
import os
import collections
from svmutil import * 

def read_vec(path1,path2):
	lists1=[]
	answer1=[]
	f1=open(path1,'r')
	for line in f1.readlines():
		arr=[]
		arr.extend(line.replace(' ','').replace('\n','').split(','))
		if arr[0]!='':
			arr = map(int, arr)
			lists1.append(arr)
			answer1.append(1)
	lists2=[]
	answer2=[]
	f2=open(path2,'r')
	for line in f2.readlines():
		arr=[]
		arr.extend(line.replace(' ','').replace('\n','').split(','))
		if arr[0]!='':
			arr = map(int, arr)
			lists2.append(arr)
			answer2.append(-1)
	lists1.extend(lists2)
	answer1.extend(answer2)	
	prob=svm_problem(answer1,lists1)
	param=svm_parameter()
	m=svm_train(prob,param)
	svm_save_model("paper.model",m)
	return 0

if __name__ == '__main__':
    read_vec('/home/lxz/test/t/count_t.txt','/home/lxz/test/t/count_f.txt')
