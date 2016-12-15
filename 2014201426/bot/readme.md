#BOT图片分类
##1.任务目标
	给定十二种不同的动物图片，用caffe训练出模型来判断新的图片属于哪一种动物。
##2.数据预处理
####(一) 获取训练样本
	样本来源：BOT图片集
	代码：train.py

####(二)转换pdf
	用linux自带的pdftotext将pdf转化为txt
	在pdf转化为txt已经自动进行了去除图和表格
####(三)处理txt
	去除标题和作者信息
	去除Reference 信息
	去除论文引用的标号 []
	将其他括号，标点符号替换为空
	所有单词转化为小写
	数字归一化处理
	去除停顿词且长度小于四的单词后用空格连起来，每篇文章一行，训练和测试各放一个文件夹，真论文和假论文各放文件夹中的一个文件中，每个文章一行。
	
***
	def make_seg(filename,Dir,frequency=0):
		raw=openfile(filename)
		tokens = word_tokenize(raw)
		tokens=[t.lower() for t in tokens if t not in string.punctuation and t.isalpha()]
		lemmatizer = nltk.WordNetLemmatizer()
		tokens = [lemmatizer.lemmatize(token) for token in tokens]
		stopwords1 = stopwords.words('english')
		tokens = [token for token in tokens if token not in stopwords1]
		tokens = [token for token in tokens if token not in newstop]
		fdist = nltk.FreqDist(tokens)
		tokens = ([w for w in tokens if len(w)> 3 and fdist[w]>frequency])
		filename = filename.split("/")[-1][:-4]
		f = open(Dir+filename+".txt","w")
		f.write(' '.join(tokens)+'\n')
		f.close()
		return fdist
***
	代码：processTxt.py getSegment.py
##3.判定
####word2vec+svm
	用gensim 自带的word2vec生成文章中词汇的词向量，然后每篇文章的词向量由单词的词向量加起来归一化后所得。
	    model=word2vec.Word2Vec(size=128,window=6,cbow_mean=0,sample=1e-4,hs=1,negative=0,workers=12)

        for word in line:
            try:
                vec=vec+model[word]
            except:
                wa+=1
        fout.write(str(ss)+' ')
        vec=preprocessing.normalize(vec)[0]
        for i,num in enumerate(vec):
            fout.write(str(1+i)+":"+str(num)+' ')
        fout.write('\n')    
####结论   
	然后用svm训练词向量得到模型去预测测试集中的论文，结果100%，比用传统机器学习的方法准确率更高且速度更快。
	
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/233) 

####得到TXT-final后运行

	python getSegment.py
	python train_w2v.py
	python getvec_w2v.py
	python predict.py
