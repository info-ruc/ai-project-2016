# encoding=utf-8
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
	i = 0;
	f = open('zuowenfenju.dat')
	line = f.readline()
	while line:
		seg_list = jieba.cut(line, cut_all=False)
		final = ''
		for seg in seg_list:
			final = final + " " +seg
		#print final				
		f2 = file('zuowenfenci.dat','a+')
		f2.write(final)
		line = f.readline()
	f2.close()
	f.close() 





