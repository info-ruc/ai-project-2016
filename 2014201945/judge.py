import string  
import re 
import os
import collections
from svmutil import *

def judge(path,stopList=None):
    f = open(path, 'r')
    myList = []
    s=""
    for eachline in f:	
        eachline = eachline.lower()
        for line in re.split('[\s]',eachline): 
            for c in string.punctuation:
		line=line.replace(c,'')
	    for c in string.digits:
		line=line.replace(c,'')
            if not (line in stopList):
                myList.append(line)
        strs = " ".join(myList)
        s=s+strs
        myList = []
    s=s+'\n'
    result = {}
    for word in s.split():  
            if word not in result:  
                result[word] = 0  
            result[word] += 1           
    c=collections.OrderedDict(sorted(result.items(), key = lambda t: -t[1]))
    i=1
    s=""
    b=[]
    for key,value in c.items():
	if i<301:
		b.append(value)
	i=i+1
    t=re.sub("[\[\]]","",str(b))+'\n'
    lists=[]
    answer=[]
    arr=[]
    arr.extend(t.replace(' ','').replace('\n','').split(','))
    if arr[0]!='':
	arr = map(int, arr)
	lists.append(arr)
	label=-1
        answer.append(label)
    prob=svm_problem(answer,lists)
    param=svm_parameter()
    model=svm_load_model('/home/lxz/test/t/paper.model')
    print svm_predict(answer,lists,model)
    print "label="+'%d' %label

if __name__ == '__main__':
    stopList = {'b','c','d','e','f','g','h','i','j','k','l','m','n','q','o','p','r','s','u','v','w','x','y','z','t','a','about','above','across','after','afterwards','again','against','all','almost','alone','along','already','also','although','always','am','among','amongst','amoungst','amount','an','and','another','any','anyhow','anyone','anything','anyway','anywhere','are','around','as','at','back','be','became','because','become','becomes','becoming','been','before','beforehand','behind','being','below','beside','besides','between','beyond','bill','both','bottom','but','by','call','can','cannot','cant','co','computer','con','could','couldnt','cry','de','describe','detail','do','done','down','due','duringeach','eg','eight','either','eleven','else','elsewhere','empty','enough','etc','even','ever','every','everyone','everything','everywhere','except','few','fifteen','fify','fill','find','fire','first','five','for','former','formerly','forty','found','four','from','front','full','further','get','give','go','had','has','hasnt','have','he','hence','her','here','here','hereafter','hereby','herein','hereupon','hers','herself','him','himself','his','how','however','hundred','i','ie','if','in','inc','indeed','interest','into','is','it','its','itself','keep','last','latter','latterly','least','less','ltd','made','many','may','me','meanwhile','might','mill','mine','more','moreover','most','mostly','move','much','must','my','myself','name','namely','neither','never','nevertheless','next','nine','no','nobody','none','noone','nor','not','nothing','now','nowhere','of','off','often','on','once','one','only','onto','or','other','others','otherwise','our','ours','ourselves','out','over','own','part','per','perhaps','please','put','rather','re','same','see','seem','seemed','seeming','seems','serious','several','she','should','showside','since','sincere','six','sixty','so','some','somehow','someone','something','sometime','sometimes','somewhere','still','such','system','take','ten','than','that','the','their','them','themselves','then','thence','there','thereafter','thereby','therefore','therein','thereupon','these','they','thick','thin','third','this','those','though','throughout','thru','thus','to','together','too','top','toward','towards','twelve','twenty','two','un','under','until','up','upon','us','very','via','was','we','well','were','what','whatever','when','whence','whenever','where','whereafter','whereas','whereby','wherein','whereupon','wherever','whether','which','while','whither','who','whoever','whole','whom','whose','why','will','with','within','without','would','yet','you','your','yours','yourself','yourselves'}
    judge('/home/lxz/test/t/input.txt',stopList)
