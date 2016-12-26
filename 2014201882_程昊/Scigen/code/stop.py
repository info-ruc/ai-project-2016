import  jieba
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')   


def count_word(line):
    result = {}
    for word in line.split():
        if word not in result:
            result[word] = 0
        result[word] += 1 
            
    return result

if __name__ == '__main__':
	for i in range(1, 3914):
		stopwords = {}.fromkeys([ line.strip() for line in open('stopword.txt') ])
		#with open('neg_papers/'+str(i)+'.txt') as f:
		with open('pos_papers/'+str(i)+'.txt') as f:
			s = ''
			for line in f:
				line = line.replace(',','').replace('.','').replace(';','').replace('\'','').replace('\"','')
				line = line.replace('\n',' ').replace('(','').replace(')','').replace('[','').replace(']','')
				line = line.replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','')
				line = line.replace('7','').replace('8','').replace('9','').replace('0','').replace('-','').replace('/','')
				line = line.replace(':','').replace('=','').replace('>','').replace('<','').replace('%','').replace('~','')
				#line = line.replace('','').replace('','').replace('','').replace('','').replace('','').replace('','')
				seg_list = line.split()
				final = ''
				for seg in seg_list:
					if (seg not in stopwords and len(seg)>3):
						final = final + " " +seg				
				s = s + final
			s = s.lower()
			print s
			#outfile = open('neg/'+str(i)+'.txt','w')
			outfile = open('pos/'+str(i)+'.txt','w')
			outfile.write(s)
			outfile.close()
		f.close() 





