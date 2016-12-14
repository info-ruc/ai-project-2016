#!/usr/bin/python

#encoding=utf-8
import sys
import os


    
def main(trainpath,testpath):

    if not trainpath.endswith('/'):
        trainpath=trainpath+'/'
    if not testpath.endswith('/'):
        testpath=testpath+'/'

    print 'start svm '+trainpath
    os.system("rm Train/train.dat")
    os.system("rm Test/*.dat")

    os.system(" cat Train/True/vec_w2v.dat  Train/False/vec_w2v.dat >> Train/train.dat")
    os.system(" cat Test/True/vec_w2v.dat  Test/False/vec_w2v.dat >> Test/test.dat")
    os.system(' '.join(['./svm-train ',trainpath+'train.dat',testpath+'model.dat']))
    os.system('wc -l '+testpath+'model.dat')
    os.system(' '.join(['./svm-predict',testpath+'test.dat',testpath+'model.dat',testpath+'predict.dat']))
    
    print 'end svm '+testpath

if __name__ == '__main__':
    main("Train/","Test")
