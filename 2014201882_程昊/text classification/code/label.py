# encoding=utf-8
import sys  
import re 
import numpy as np
reload(sys)  
sys.setdefaultencoding('utf-8')

'''
s = []
for i in range(0, 600000):
	s.append(0)
s[0] = 0
with open("index.txt","rb") as f1:
	lines = f1.readlines()
	for line in lines:
		l = line.split()
		s[int(l[0])] = s[int(l[0])-1] + int(l[1])
print s[7040] 

'''

with open("label.txt", "rb") as f:
	with open("index.txt","rb") as f1:
		lines = f1.readlines()
		j = 0
		for line in f:
			s1=line.split(" ")
			id = int(s1[0])
			type = int(s1[1])
			x = ''

			num_1 = 0
			for i in range(0, id-1):
				s = lines[i].split(" ")
				num_1 = num_1 + int(s[1])
			s = lines[id-1].split()

			num_2 = num_1 + int(s[1])
			if j == 0:
				print lines[id-1], num_1, num_2
			for line_num in range(num_1, num_2):
				x = x + str(line_num) + ' '
			f2 = open(str(type)+".txt",'a+')
			f2.write(x+'\n')
			f2.close()
			j = j+1
		f1.close()
	f.close()


