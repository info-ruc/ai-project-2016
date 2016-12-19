import string  
import re 
import os
import collections
def count(path):
	result = {}
    	with open(path) as file_obj:  
        	all_the_text = file_obj.read()
	for word in all_the_text.split():  
            if word not in result:  
                result[word] = 0  
            result[word] += 1   
              
        return collections.OrderedDict(sorted(result.items(), key = lambda t: -t[1]))	

if __name__ == '__main__':
    pt =  os.listdir('/home/lxz/test/t/output_t/')
    pf =  os.listdir('/home/lxz/test/t/output_f/')
    for allDir in pt:
        child = os.path.join('%s%s' % ('/home/lxz/test/t/output_t/', allDir))
	path='/home/lxz/test/t/count_t.txt'
    	a = count(child)
	i=1
	f=open(path,'a+')
	b=[]
	for key,value in a.items():
		if i<301:
			b.append(value)
		i=i+1
	t=re.sub("[\[\]]","",str(b))
	f.write(t)
	f.write('\n')
	f.close()
    for allDir in pf:
        child = os.path.join('%s%s' % ('/home/lxz/test/t/output_f/', allDir))
	path='/home/lxz/test/t/count_f.txt'
    	a = count(child)
	i=1
	f=open(path,'a+')
	b=[]
	for key,value in a.items():
		if i<301:
			b.append(value)
		i=i+1
	t=re.sub("[\[\]]","",str(b))
	f.write(t)
	f.write('\n')
	f.close()
