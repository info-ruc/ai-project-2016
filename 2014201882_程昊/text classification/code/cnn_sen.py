# encoding=utf-8
import load_sen
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding
from keras.layers import Conv1D, MaxPooling1D, Convolution2D, MaxPooling2D, Embedding
from keras.utils.np_utils import to_categorical
from keras import backend as K
from keras.layers import Merge
from keras.optimizers import SGD,Adagrad, Adadelta
import pandas as pd 
import numpy as np 
np.random.seed(1337)

def main():
    x, y, embeddings_index, word_index = load_sen.load()

    indices = np.arange(x.shape[0])
    np.random.shuffle(indices)
    x = x[indices]
    y = y[indices]
    print 'shuffle done'
    p_valid = 0.2
    p_test = 0.1
    l = len(x)
    l1 = int ( l * (1.0 - p_valid - p_test) )
    l2 = int ( l * (1.0 - p_test) )
    print 'datasize =', l
    x_train = x[:l2]
    y_train = y[:l2]
    x_test = x[l2:]
    y_test = y[l2:]

    # prepare embedding matrix
    nb_words = len(word_index)
    print x_train[0]
    print y_train[0]
    embedding_matrix = np.zeros((nb_words + 1, 128))
    j = 0
    for word, i in word_index.items():
        word = str(word).decode('utf-8')
        embedding_vector = embeddings_index.get(word)
        if embedding_vector is not None:
            j += 1
            # words not found in embedding index will be all-zeros.
            embedding_matrix[i] = embedding_vector
    print j
    print len(embeddings_index)
    print len(embedding_matrix)

    model1 = Sequential()
    model1.add(Embedding(nb_words + 1,
                            128,
                            weights=[embedding_matrix],
                            input_length = 68,
                            trainable=True))
    model1.add(Conv1D(64, 3))
    model1.add(Activation('relu'))
    model1.add(MaxPooling1D(model1.output_shape[1]))
    model1.add(Flatten())
   
    model2 = Sequential()
    model2.add(Embedding(nb_words + 1,
                            128,
                            weights=[embedding_matrix],
                            input_length = 68,
                            trainable=True))
    model2.add(Conv1D(64, 4))
    model2.add(Activation('relu'))
    model2.add(MaxPooling1D(model2.output_shape[1]))
    model2.add(Flatten())

    model3 = Sequential()
    model3.add(Embedding(nb_words + 1,
                            128,
                            weights=[embedding_matrix],
                            input_length = 68,
                            trainable=True))
    model3.add(Conv1D(64, 5))
    model3.add(Activation('relu'))
    model3.add(MaxPooling1D(model3.output_shape[1]))
    model3.add(Flatten())

    merged = Merge([model1, model2, model3], mode='concat')
    
    final_model = Sequential()
    final_model.add(merged)    
    final_model.add(Dense(150))
    final_model.add(Dropout(0.5))
    final_model.add(Activation('relu'))
    final_model.add(Dense(100))
    final_model.add(Dropout(0.5))
    final_model.add(Activation('relu'))
    final_model.add(Dense(7))
    final_model.add(Activation('softmax'))  

    sgd = SGD(lr=0.05)
    final_model.compile(optimizer='Adagrad',loss='categorical_crossentropy',metrics=['acc'])

    final_model.fit([x_train,x_train,x_train], y_train, validation_split=0.2,
          nb_epoch=50, batch_size=50)

    score = final_model.evaluate([x_test,x_test,x_test], y_test,batch_size=16)   
    print score

    final_model.save('model.h5')

if __name__ == '__main__':
    main()
