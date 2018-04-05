# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.contrib.rnn import BasicLSTMCell
import pickle
from keras.preprocessing import sequence
import numpy as np
import os

# vocabulory size = 43872;

model_path = '/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/model'

nData = pickle.load(open('/Users/mac/Documents/CODE/GraduateDesign/Word2Vector/data/model/vector.pkl','rb'))
trainData = nData.trainGrams
valData = nData.validGrams

vocab_size = 43872
n_epchs = 1000
learning_rate = 0.0005

dim_hidden = 128
batch_size = 16
n_lstm_steps = 4 + 2
maxlen = 4
embedding_size = 16
graph = tf.Graph()
with graph.as_default():
    sentence = tf.placeholder(tf.int32, [batch_size, n_lstm_steps])
    mask = tf.placeholder(tf.float32, [batch_size, n_lstm_steps])
    current_emb = tf.placeholder(tf.int32, [batch_size, n_lstm_steps])
    embed_word_W = tf.Variable(tf.random_normal([vocab_size]))

    with tf.device("/cpu:0"):
        Wemb = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -0.1, 0.1), name='Wemb')
    bemb = tf.Variable(tf.zeros([embedding_size], name='bemb'))
    


