# encoding=utf-8
import load_word
import load_sen
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, BatchNormalization
from keras.layers import Embedding
from keras.layers import Conv1D, MaxPooling1D, Convolution2D, MaxPooling2D, Embedding
from keras.utils.np_utils import to_categorical
from keras import backend as K
from keras.layers import Merge
from keras.optimizers import SGD, Adagrad, Adadelta

import pandas as pd 
import numpy as np 
np.random.seed(1337)



def main():
    x_word, y_word, embeddings_index_word, word_index_word = load_word.load()

    # prepare embedding matrix
    nb_words = len(word_index_word)
    embedding_matrix_word = np.zeros((nb_words + 1, 150))
    j = 0
    for word, i in word_index_word.items():
        word = str(word).decode('utf-8')
        embedding_vector = embeddings_index_word.get(word)
        if embedding_vector is not None:
            j += 1
            # words not found in embedding index will be all-zeros.
            embedding_matrix_word[i] = embedding_vector
    print j
    print len(embeddings_index_word)
    print len(embedding_matrix_word)



    model1 = Sequential()
    model1.add(Embedding(nb_words + 1,
                            150,
                            weights=[embedding_matrix_word],
                            input_length = 252,
                            trainable=True))
    model1.add(Conv1D(64, 3))
    model1.add(Activation('relu'))
    model1.add(Dropout(0.3))
    model1.add(BatchNormalization(epsilon=1e-04, momentum=0.9, weights=None, beta_init='zero', gamma_init='one'))
    model1.add(MaxPooling1D(model1.output_shape[1]))
    model1.add(Flatten())
   
    model2 = Sequential()
    model2.add(Embedding(nb_words + 1,
                            150,
                            weights=[embedding_matrix_word],
                            input_length = 252,
                            trainable=True))
    model2.add(Conv1D(64, 4))
    model2.add(Activation('relu'))
    model2.add(Dropout(0.3))
    model2.add(BatchNormalization(epsilon=1e-04,  momentum=0.9, weights=None, beta_init='zero', gamma_init='one'))
    model2.add(MaxPooling1D(model2.output_shape[1]))
    model2.add(Flatten())

    model3 = Sequential()
    model3.add(Embedding(nb_words + 1,
                            150,
                            weights=[embedding_matrix_word],
                            input_length = 252,
                            trainable=True))
    model3.add(Conv1D(64, 5))
    model3.add(Activation('relu'))
    model3.add(Dropout(0.3))
    model3.add(BatchNormalization(epsilon=1e-04, momentum=0.9, weights=None, beta_init='zero', gamma_init='one'))
    model3.add(MaxPooling1D(model3.output_shape[1]))
    model3.add(Flatten())



    x_sen, y_sen, embeddings_index_sen, word_index_sen = load_sen.load()
    # prepare embedding matrix
    nb_words = len(word_index_sen)
    embedding_matrix_sen = np.zeros((nb_words + 1, 128))
    j = 0
    for word, i in word_index_sen.items():
        word = str(word).decode('utf-8')
        embedding_vector = embeddings_index_sen.get(word)
        if embedding_vector is not None:
            j += 1
            # words not found in embedding index will be all-zeros.
            embedding_matrix_sen[i] = embedding_vector
    print j

    print len(embeddings_index_sen)
    print len(embedding_matrix_sen)

    model4 = Sequential()
    model4.add(Embedding(nb_words + 1,
                            128,
                            weights=[embedding_matrix_sen],
                            input_length = 68,
                            trainable=True))
    model4.add(Conv1D(32, 3))
    model4.add(Activation('relu'))
    model4.add(Dropout(0.3))
    model4.add(BatchNormalization(epsilon=1e-04, momentum=0.9, weights=None, beta_init='zero', gamma_init='one'))
    model4.add(MaxPooling1D(model4.output_shape[1]))
    model4.add(Flatten())
   
    model5 = Sequential()
    model5.add(Embedding(nb_words + 1,
                            128,
                            weights=[embedding_matrix_sen],
                            input_length = 68,
                            trainable=True))
    model5.add(Conv1D(32, 4))
    model5.add(Activation('relu'))
    model5.add(Dropout(0.3))
    model5.add(BatchNormalization(epsilon=1e-04, momentum=0.9, weights=None, beta_init='zero', gamma_init='one'))
    model5.add(MaxPooling1D(model5.output_shape[1]))
    model5.add(Flatten())

    model6 = Sequential()
    model6.add(Embedding(nb_words + 1,
                            128,
                            weights=[embedding_matrix_sen],
                            input_length = 68,
                            trainable=True))
    model6.add(Conv1D(32, 5))
    model6.add(Activation('relu'))
    model6.add(Dropout(0.3))
    model6.add(BatchNormalization(epsilon=1e-04, momentum=0.9, weights=None, beta_init='zero', gamma_init='one'))
    model6.add(MaxPooling1D(model6.output_shape[1]))
    model6.add(Flatten())



    merged = Merge([model1, model2, model3, model4, model5, model6], mode='concat')
    
    final_model = Sequential()
    final_model.add(merged)    
    #final_model.add(Flatten())
    final_model.add(Dense(150))
    final_model.add(Dropout(0.5))
    final_model.add(Activation('relu'))
    final_model.add(Dense(100))
    final_model.add(Dropout(0.5))
    final_model.add(Activation('relu'))
    final_model.add(Dense(7))
    final_model.add(Activation('softmax'))  

    sgd = SGD(lr=0.005)
    ada = Adadelta()
    adag = Adagrad()
    final_model.compile(optimizer='Adadelta',loss='categorical_crossentropy',metrics=['acc'])

    if x_word.shape[0] == x_sen.shape[0]:
        indices = np.arange(x_word.shape[0])
        np.random.shuffle(indices)
        x_word = x_word[indices]
        y_word = y_word[indices]
        x_sen = x_sen[indices]
        y_sen = y_sen[indices]
        print 'shuffle done'
        p_valid = 0.2
        p_test = 0.1
        l = len(x_word)
        l1 = int ( l * (1.0 - p_valid - p_test) )
        l2 = int ( l * (1.0 - p_test) )
        print 'datasize =', l
        x_train_word = x_word[:l2]
        y_train_word = y_word[:l2]
        x_test_word = x_word[l2:]
        y_test_word = y_word[l2:]
        x_train_sen = x_sen[:l2]
        y_train_sen = y_sen[:l2]
        x_test_sen = x_sen[l2:]
        y_test_sen = y_sen[l2:]

    final_model.fit([x_train_word,x_train_word,x_train_word,x_train_sen,x_train_sen,x_train_sen], y_train_word, validation_split=0.2,
          nb_epoch=10, batch_size=25, shuffle = True)

    score = final_model.evaluate([x_test_word,x_test_word,x_test_word,x_test_sen,x_test_sen,x_test_sen], y_test_word,batch_size=16)   
    print score

    final_model.save('model.h5')

if __name__ == '__main__':
    main()
