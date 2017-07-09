import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation
import keras
import string
from collections import defaultdict

# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    #X = []
    #y = []

    # reshape each 
    #X = np.asarray(X)
    #X.shape = (np.shape(X)[0:2])
    X = np.ndarray(shape=(series.size-window_size,window_size))
    y = np.ndarray(shape=(series.size-window_size, 1))
    #y.shape = (len(y),1)


    for i in range(series.size-window_size):
        X[i]=series[i:i+window_size]
        y[i]=series[i+window_size]
        
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(5, input_shape= (window_size,1)))
    model.add(Dense(1))
    return model


### TODO: list all unique characters in the text and remove any non-english ones
def cleaned_text(text):
    # remove as many non-english characters and character sequences as you can 
    # but don't remove the punctuation given below
    punctuation = ['!', ',', '.', ':', ';', '?']

    cleaned_text=text
    valid_chars=list(string.ascii_letters)+list(punctuation)

    # build a dict of all chars in the text
    chars = defaultdict(int)
    for char in cleaned_text:
        chars[char]=chars[char]+1

    for char in chars:
        if char not in valid_chars:
            cleaned_text=cleaned_text.replace(char,' ')

    return cleaned_text



### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = []
    outputs = []
    i=0
    while i*step_size+window_size<len(text):
        #print("i {}, i*step_size+window_size {}, len text {}".format(i,i*step_size+window_size,len(text)))
        inputs.append(text[i*step_size:i*step_size+window_size])
        outputs.append(text[i*step_size+window_size])
        i=i+1
    
  
    return inputs,outputs

# TODO build the required RNN model: 
# a single LSTM hidden layer with softmax activation, categorical_crossentropy loss 
def build_part2_RNN(window_size,len_chars):
    model = Sequential()
    model.add(LSTM(200, input_shape=(window_size,len_chars) ))
    model.add(Dense(len_chars))
    model.add(Activation('softmax'))

    model.summary()

    return model



