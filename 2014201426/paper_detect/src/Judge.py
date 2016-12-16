# -*-coding:utf-8 -*-
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from utils import getTestCaseForJudge

realPath = './data/paper.data'
unRealPath = './data/scigen.data'

realNum = 2700
unrealNum = 1200

fileNames1,input1,output1 = getTestCaseForJudge(realPath)
fileNames2,input2 , output2 = getTestCaseForJudge(unRealPath)
train_input , train_output = input1[:realNum] + input2[:unrealNum] ,output1[:realNum]+output2[:unrealNum]

fileNames,test_input , test_output = fileNames1[realNum:] + fileNames2[unrealNum:] ,input1[realNum:] + input2[unrealNum:] ,output1[realNum:]+output2[unrealNum:]

clf = KNeighborsClassifier(n_neighbors=3) 
clf.fit(train_input,train_output)
predicted = clf.predict(test_input)
p = 0
for i in xrange(len(predicted)):
    result = predicted[i]
    p += predicted==test_output[i]
print("Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(test_output, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(test_output, predicted))

clf = svm.SVC(gamma=0.4,C=2)
clf.fit(train_input,train_output)
predicted = clf.predict(test_input)
p = 0
for i in xrange(len(predicted)):
    result = predicted[i]
    p += predicted==test_output[i]

print("Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(test_output, predicted)))
print("Confusion matrix:\n%s" % metrics.confusion_matrix(test_output, predicted))
