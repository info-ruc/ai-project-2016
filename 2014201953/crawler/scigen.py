#http://scigen.csail.mit.edu/cgi-bin/scigen.cgi?author=6&author=&author=&author=&author=
import urllib2
import HTMLParser
#from svm import *

start1=1
start2=1
size1=200
size2=1000

def fetch(start,end):
	t=0
	for t in xrange(start,end):
		urlText = []
		response = urllib2.urlopen('http://scigen.csail.mit.edu/cgi-bin/scigen.cgi?author=6&author=&author=&author=&author=')  
		html = response.read() 

		class parseText(HTMLParser.HTMLParser):
			def handle_data(self,data):
				if data != '\n' or data != '\n\n' or data!= '\n ' :
					urlText.append(data)

		lParser = parseText()
		lParser.feed(html)

		#print urlText
		file_object = open('fakepaper/paper'+str(t)+'.txt', 'w')
		i=0
		while i<len(urlText):
			if 'Back to the SCIgen homepage.'==urlText[i]:
				del urlText[i]
				break
			else:
				del urlText[i]
		str2 = '\n'.join(urlText)
		str2 = ' '.join(str2.split('\n'))
		file_object.write(str2)
		file_object.close( )
		print t
#fetch(300,301)
def count(i,dir,alpha,bound):	
	try:
		data = open(dir+str(i)+'.txt', 'r')
	except Exception as err:
		#print err
		return 0
	word_counts={}
	for line in data:
		line=line.split()
		for word in line:
			word_counts[word] = word_counts.get(word,0) + 1
	len1 = len(word_counts)
	if alpha != 0:bound = len1*alpha
	word_counts2 = word_counts.items()
	cnt=0
	#print word_counts2
	for key,value in word_counts2:
		cnt+=1
		if value <bound :
			del word_counts[key]
	#print cnt
	#print len(word_counts)
	#print [len(word_counts),len(word_counts2)]
	#print  float(len(word_counts))/float(len(word_counts2))
	# return [len(word_counts),len(word_counts2)]
	return float(len(word_counts))/float(len(word_counts2))

def svm():
	input=[]
	answer=[]
	for i in xrange(1,100):
		try:
			data = open('fakepaper/paper'+str(i)+'.txt', 'r')
		except Exception as err:
			#print err
			return 0
		word_counts={}
		for line in data:
			line=line.split()
			for word in line:
				word_counts[word] = word_counts.get(word,0) + 1
		input.append(word_counts)
		answer.append(-1)		
	for i in xrange(1,1000):
		try:
			data = open('realpaper/'+str(i)+'.txt', 'r')
		except Exception as err:
			#print err
			return 0
		word_counts={}
		for line in data:
			line=line.split()
			for word in line:
				word_counts[word] = word_counts.get(word,0) + 1
		input.append(word_counts)
		answer.append(1)
	prob = svm_problem(answer,input)

def judge(alpha,bound1,bound2,size1,size2,start1,start2):

	false1=0
	false2=0
	#bound=0.028
	sum=0
	for i in xrange(start1,start1+size1):
		cnt=count(i,'fakepaper/paper',alpha,bound2)
		if cnt>bound1:
			false1+=1
			#print "false1: "+str(cnt)
		sum+=cnt
	#print "flase size1: "+str(size1)+ "avg: "+str(sum/size1)

	sum=0
	error=0
	for i in xrange(start2,start2+size2):
		cnt=count(i,'realpaper/',alpha,bound2)
		if cnt ==0:error+=1
		elif cnt<bound1:
			false2+=1
			#print "false2 :"+str(cnt)
		sum+=cnt
	size2=size2-error
	#print "real: size2: "+str(size2)+"avg: "+str(sum/size2)
	#print "false1: "+str(false1)+" false2: "+str(false2)
	accuracy=(1-float((false1+false2))/float((size1+size2)))*100
	print "accuracy: "+str(accuracy)+"%"
	return accuracy
alphaList=[0]
bound1List=[]
bound2List=[]
# for i in xrange(1,10):
# 	alphaList.append(i*0.001)
for i in xrange(28,30):
	bound1List.append(i*0.001)
for i in xrange(805,810):
	bound2List.append(i*0.01)	
#print alphaList
maxAccurate=0
alpha0=0
bound10=0
bound20=0
print "training..."
for bound2 in bound2List:
	for alpha in alphaList:
		for bound1 in bound1List:
			accurate=judge(alpha,bound1,bound2,size1,size2,start1,start2)
			if accurate>maxAccurate:
				maxAccurate=accurate
				alpha0=alpha
				bound10=bound1
				bound20=bound2

print "max accuracy:"+ str(maxAccurate)+"%  alpha: "+str(alpha0)+ " bound1: "+str(bound10)+" bound2: "+str(bound20)
print "validation"
size1=100
size2=500
start1=200
start2=1000
accurate=judge(0,bound10,bound20,size1,size2,start1,start2)
print "validation accuracy:"+str(accurate)+"%"
#count(1,'fakepaper/paper')
#count(1,'realpaper/')

#svm()