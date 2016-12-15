#BOT图片分类
##1.任务目标
	给定十二种不同的动物图片，用caffe训练出模型来判断新的图片属于哪一种动物。
##2.数据预处理
####(一) 获取训练样本
	样本来源：BOT图片集
####(二)划分训练集和测试集
	将BOT数据集的rar压缩包解压，得到预览集和大的数据集，将预览集留作测试，大的数据集用来训练，
	大数据集划分成了train set和development set（用于调节参数防止过拟合）
	处理后得到train.txt,test.txt，txt文件每一行包含图片名和标签（代表所属的类别）和picture文件夹中包含所有图片，
	由于图片包含jpg，jpeg，png，gif格式，在转换为lmdb时会报错（无法打开文件），
	所以这里将所有的非jpg格式的文件转换成jpg（用imagemagick转换），这里可能会损失图片质量，导致最后准确率无法提升。
	代码：	
			python merge.py
			python getTrain.py
			mv data/Dog data/dog
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/1.png) 

####(三)转换成LMDB格式
	 在转换成lmdb格式时要制定图片resize的width和height，这里对应着prototxt中的cropsize，
	 最开始的实验中我在这里使用了256×256,而cropsize设成了32，导致每一次都只截取了图片的一小部分进行训练和测试，
	 导致训练和测试的准确率都只有百分之三十多。
	 代码：bash con2jpg.sh
##3.模型训练
####resnet-20层
	借用了处理cifar10数据集的参数选择，训练和测试的batchsize都设为100
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/2.png) 
##4.训练结果   
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/3.png) 

	可以看到在五万多次左右train set的准确率在不断上升，test set的准确率却在70%左右不变。
####finetune
	所以在保持这个训练到64000次迭代的同时，用51500次迭代后保存的model用测试集进行fine-tune
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/4.png) 

	开始finetune使用训练的起始lr=0.1,但是发现loss太大了，于是立刻停止将lr改为0.01![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/5.png)

#####solver2.prototxt![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/6.png)
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/7.png)

	然后再用新得到的10000次迭代后的weight去finetune训练集	可以看到在5000次迭代左右测试集准确率稳定在79%左右，测试集在83%到93%![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/8.png)

##5.测试
	分别用64000次迭代不加finetune所得到最后的模型和51500次迭代加上10000次finetune所得到的模型对预览集进行测试
	![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/9.png)
![](https://github.com/Victorianuonuo/ai-project-2016/blob/master/2014201426/pictures/10.png)

	从测试结果中可以看出用development set finetune 所得到的模型更具有普适性，更能准确的描述测试集。##6.反思：	测试集准确率没有达到90%，考虑有以下几点原因	一：在转图片格式为jpg以便处理成lmdb格式时损失了信息（个人认为是主要原因）	二：没有gpu跑起来的速度太慢无法训练更多以尝试不同的参数来达到更高的准确率

####运行
	python merge.py
	python getTrain.py
	mv data/Dog data/dog
	bash con2jpg.sh
	python changeTag.py
	python train.py
	bash getLMDB.sh
	bash train.sh
