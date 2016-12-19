from collections import defaultdict



for i in range(901, 3914):
	#with open('neg_papers/'+str(i)+'.txt') as f:
	with open('pos_papers/'+str(i)+'.txt') as f:
		print 1
		vocab = defaultdict(float)
		for line in f :
			s = line.split(" ")
			for j in range(len(s)):
				if(len(s[j]) > 0):
					vocab[s[j]] += 1
		vocab = sorted(vocab.items(), key = lambda item:item[1], reverse=True)
		print len(vocab)
		k = 0
		s = '1'
		for a in vocab:
			if(k < 300):
				#print k, a[0], a[1]
				s = s + ' ' + str(k) + ':'+str(a[1])
			k+=1
		print s
		outfile = open('data_train.txt','a')
		outfile.write(s+'\n')
		outfile.close()


