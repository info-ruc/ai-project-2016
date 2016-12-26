# encoding=utf-8
import csv
import re
import sys
import os 
from collections import defaultdict
csv.field_size_limit(sys.maxsize)
import pandas as pd 
import numpy as np 
from gensim.models import Doc2Vec
from gensim import models 
import logging
from keras.utils.np_utils import to_categorical
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def load_data():
    i = 0

def load_data_and_labels():

    print ("load_text_and_labels...")
    # Load data from files
    examples_0 = list(open("./data/sentences/0.txt", "r").readlines())
    examples_0 = [s.strip() for s in examples_0]

    examples_1 = list(open("./data/sentences/1.txt", "r").readlines())
    examples_1 = [s.strip() for s in examples_1]

    examples_2 = list(open("./data/sentences/2.txt", "r").readlines())
    examples_2 = [s.strip() for s in examples_2]

    examples_3 = list(open("./data/sentences/3.txt", "r").readlines())
    examples_3 = [s.strip() for s in examples_3]

    examples_4 = list(open("./data/sentences/4.txt", "r").readlines())
    examples_4 = [s.strip() for s in examples_4]

    examples_5 = list(open("./data/sentences/5.txt", "r").readlines())
    examples_5 = [s.strip() for s in examples_5]

    examples_6 = list(open("./data/sentences/6.txt", "r").readlines())
    examples_6 = [s.strip() for s in examples_6]

    x_text = examples_0 + examples_1 + examples_2 + examples_3 + examples_4 + examples_5 + examples_6
    # Generate labels

    y = []
    for _ in examples_0:
        y.append(0)
    for _ in examples_1:
        y.append(1)
    for _ in examples_2:
        y.append(2)
    for _ in examples_3:
        y.append(3)
    for _ in examples_4:
        y.append(4)
    for _ in examples_5:
        y.append(5)
    for _ in examples_6:
        y.append(6)
    print len(examples_0), len(examples_1), len(examples_2), len(examples_3), len(examples_4), len(examples_5), len(examples_6) 
    print "load done!"
    return [x_text, y]

def build_vocab(x_text):
    vocab = defaultdict(float)
    for s in x_text:
        words = set(s.split())
        for word in words:
            vocab[word] += 1
    return vocab

def load_doc2vec(fname, vocab):
    print ("load word vec...")
    model = Doc2Vec.load(fname)
    word_vecs = {}
    for word in vocab:
        word_vecs[word] = model.docvecs[int(word)-1]
    print "load done!"
    print len(word_vecs)
    return word_vecs 


def load():
    x_text, y = load_data_and_labels()
    vocab = build_vocab(x_text)
    w2v = load_doc2vec('./data/vec/doc2vec_fenju_128',vocab)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(x_text)
    sequences = tokenizer.texts_to_sequences(x_text)
    word_index = tokenizer.word_index
    data = pad_sequences(sequences,padding="post")
    y = to_categorical(np.asarray(y))
    print('Shape of data tensor:', data.shape)
    print('Shape of label tensor:', y.shape)

    max = 0
    for _ in data:
        if max < len(_):
            max = len(_)
    print "max len:",max

    l = len(data)
    print 'datasize =', l

    x = data
    return x, y, w2v, word_index
