import re 
import os
import string
def dive(path,path1,stopList=None):
    f1 = open(path1, 'w')
    f = open(path, 'r')
    myList = []
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
        f1.write(strs)
        myList = []
    f1.write('\n')
    return 1
if __name__ == '__main__':
    stopList = {'b','c','d','e','f','g','h','i','j','k','l','m','n','q','o','p','r','s','u','v','w','x','y','z','t','a','about','above','across','after','afterwards','again','against','all','almost','alone','along','already','also','although','always','am','among','amongst','amoungst','amount','an','and','another','any','anyhow','anyone','anything','anyway','anywhere','are','around','as','at','back','be','became','because','become','becomes','becoming','been','before','beforehand','behind','being','below','beside','besides','between','beyond','bill','both','bottom','but','by','call','can','cannot','cant','co','computer','con','could','couldnt','cry','de','describe','detail','do','done','down','due','duringeach','eg','eight','either','eleven','else','elsewhere','empty','enough','etc','even','ever','every','everyone','everything','everywhere','except','few','fifteen','fify','fill','find','fire','first','five','for','former','formerly','forty','found','four','from','front','full','further','get','give','go','had','has','hasnt','have','he','hence','her','here','here','hereafter','hereby','herein','hereupon','hers','herself','him','himself','his','how','however','hundred','i','ie','if','in','inc','indeed','interest','into','is','it','its','itself','keep','last','latter','latterly','least','less','ltd','made','many','may','me','meanwhile','might','mill','mine','more','moreover','most','mostly','move','much','must','my','myself','name','namely','neither','never','nevertheless','next','nine','no','nobody','none','noone','nor','not','nothing','now','nowhere','of','off','often','on','once','one','only','onto','or','other','others','otherwise','our','ours','ourselves','out','over','own','part','per','perhaps','please','put','rather','re','same','see','seem','seemed','seeming','seems','serious','several','she','should','showside','since','sincere','six','sixty','so','some','somehow','someone','something','sometime','sometimes','somewhere','still','such','system','take','ten','than','that','the','their','them','themselves','then','thence','there','thereafter','thereby','therefore','therein','thereupon','these','they','thick','thin','third','this','those','though','throughout','thru','thus','to','together','too','top','toward','towards','twelve','twenty','two','un','under','until','up','upon','us','very','via','was','we','well','were','what','whatever','when','whence','whenever','where','whereafter','whereas','whereby','wherein','whereupon','wherever','whether','which','while','whither','who','whoever','whole','whom','whose','why','will','with','within','without','would','yet','you','your','yours','yourself','yourselves'}
    pt = os.listdir('/home/lxz/test/t/input_t/')
    pf = os.listdir('/home/lxz/test/t/input_f/')
    i=0
    for allDir in pt:
        child = os.path.join('%s%s' % ('/home/lxz/test/t/input_t/', allDir))
	path='/home/lxz/test/t/output_t/'+str(i)+'.txt'
    	a = dive(child , path, stopList)
	i=i+1
    i=0
    for allDir in pf:
        child = os.path.join('%s%s' % ('/home/lxz/test/t/input_f/', allDir))
	path='/home/lxz/test/t/output_f/'+str(i)+'.txt'
    	a = dive(child , path, stopList)
	i=i+1
