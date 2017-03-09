# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 12:18:18 2017

@author: Quantum Liu
"""
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
import wechat_utils #will login automaticly
#wechat_utils.sendmessage()isthe callback class
#wechat_utils.sendmessage()是keras的回调类，fit时传入callbacklist

nb_sample=64*10000
batch_size=64
dim=784

model = Sequential()
model.add(Dense(2048, input_dim=784))
model.add(Activation('relu'))
for i in range(9):
    model.add(Dense(2048))
    model.add(Activation('relu'))
model.add(Dense(1,activation='sigmoid'))

x=np.random.rand(nb_sample,dim)   
y=np.random.randint(2,size=(nb_sample,1))

train_x=x[:390*64]
train_y=y[:390*64]

val_x=x[-10*64:]
val_y=y[-10*64:]

model.compile(optimizer='RMSprop',loss='binary_crossentropy',metrics=['acc','hinge'])
#==============================================================================
# Train
#==============================================================================
model.fit(x=train_x,y=train_y,batch_size=batch_size,nb_epoch=60,validation_data=(val_x,val_y),callbacks=[wechat_utils.sendmessage()])