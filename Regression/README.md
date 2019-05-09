This Regression Model is to predict the fuel efficiency of late-1970s and early 1980s automobiles. 
This program download a dataset of many automobiles from that time period. 
The raw dataset includes attributes like: cylinders, displacement, horsepower, and weight.
Aim to predict the output of a continuous value, like a price or a probability

Sequential Model
================
Predict MPG

1st Layer
=========
Hidden Units : 64
Activation Method : RELU


2nd Layer
=========
Hidden Units : 64
Activation Method : RELU

3rd Layer
=========
Hidden Unit : 1

Optimizer 
=========
RMSprop = 0.001

LOSS Function
=============
Mean Squared Error

Metrics
=======
Mean Absolute Error


Use an EarlyStopping callback that tests a training condition for every epoch. 
If a set amount of epochs elapses without showing improvement, then automatically stop the training.
