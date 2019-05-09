Overfitting
===========
To prevent overfitting 

1) Use more training data which will generalize data better
2) Use Regularization technique to put constrains on the quantity and type of information to model.
3) If a network only affort to memorize small amount of patterns, the optimisation process will focus on the most prominient patterns.

2 Regularization 
================
1) Weight Regularization
a) L1 Regularization -  where the cost added is proportional to the absolute value of the weights coefficients 
(i.e. to what is called the "L1 norm" of the weights).
b) L2 Regularization - where the cost added is proportional to the square of the value of the weights coefficients (i.e. to what is called the squared "L2 norm" of the weights). 
L2 regularization is also called weight decay in the context of neural networks.

2) Dropout
Consists of randomly "dropping out" (i.e. set to zero) a number of output features of the layer during training
A given layer with a vector [0.2, 0.5, 1.3, 0.8, 1.1] during training; after applying dropout, this vector will have a few zero entries distributed at random, e.g. [0, 0.5, 1.3, 0, 1.1]
The "dropout rate" is the fraction of the features that are being zeroed-out; it is usually set between 0.2 and 0.5

Purpose
========
(1) This program firstly define a baseline model with 16 hidden units in each layer.

It demonstrate how to trigger overfitting by define a smaller model (4 hidden units per layer)
and big model (512 hidden units per layer).

pip install numpy==1.16.1

(2) By comparing "Binary Crossentropy" diagram, he smaller network begins overfitting later than the baseline model (after 6 epochs rather than 4)
and its performance degrades much more slowly once it starts overfitting.
larger network begins overfitting almost right away, after just one epoch, and overfits much more severely

(3) Define L2 Regularization to improve overfitting issue.

By comparing ""Binary Crossentropy" diagram, L2 regularized model has become much more resistant to overfitting than the baseline model,

(dotted line is lower than baseline model), even though both models have the same number of parameters.


(4) Define DropOut Regularization to improve fitting issue.

Baseline Model
==============
Sequential Model


1st Layer

Hidden Units : 16

Activation Method=RELU


2rd Layer

Hidden Units : 16

Activation Method=RELU


3rd Layer

Hidden Unit : 1

Activation Method=sigmoid


Optimizer

ADAM


Loss Function

Binary Crossentropy


Epochs : 20

Batch size : 512


Smaller Model
=============
All setup as Baseline Model except below parameters.

lst Layer

Hidden Units : 4


2rd Layer

Hidden Units : 4



Bigger Model
============
1st Layer 

Hidden Units : 512


2rd Layer

Hidden Units : 512


L2 Model
========
1st Layer

Hidden Units : 16

Regularizer = L2 0.001


2rd Layer

Hidden Units : 16

Regularizer = L2 0.001


DropOut Model
=============
1st Layer

Hidden Units : 16

Dropout Rate=0.5


2rd Layer 

Hidden Units : 16

Dropout Rate=0.5
