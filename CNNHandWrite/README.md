Hand Writing Number Recognition
===============================
This is yet another interesting Machine Learning model. This model is aimed to recognise different handwriting number images from 0-9 and recognize the correct number.


Model
=====
Convolutional Neural Network (CNN)
Tensorflow Estimator

Convolutional Layer#1
=====================
Applies 32 5x5 filter (extract 5x5 pixel subregions from each image)

Activation Method=RELU

Applies a specified number of convolution filters to image. 
For each subregion, the layer performs a set of mathematical operation to produce a single value in the output feature map.
Convolutional layers then apply RELU function to the output to introduce nonlinearities into the model.


Pooling Layer#1
===============
MAX pooling (from the choice of 'average' or 'max' pooling) 

2x2 filter 

stride of 2 (No overlapping between subregions)

downsample the image data extracted by convolutional layers to reduce the dimensionality of the feature map in order to decrease processing time.
A commonly used pooling algorithm is "MAX POOLING", which extracts subregions of an image (2x2 pixels),
keeps their maximum value and discards all other values.


Convolutional Layer#2
=====================
Apply 64 5x5 filter

Activation Method = RELU

Pooling Layer #2
================
MAX Pooling

2x2 filter

stride of 2

Dense Layer #1
==============
1024 neurons
Regularization=Dropout (0.4 probability)

which performs classification on the feature extracted by convolutional layers and downsampled by pooling layer.
In the Dense Layer, every node in the layer is connected to every node in the preceding layer.

Dense Layer #2
==============
LOGITS layer

10 neurons (each represents each digit 0-9)



Installation Requirement
=========================
get cuDNN failed from python log

conda list | findstr cudnn (using version 7.3.1)

conda uninstall cudnn

install cudnn 7.5.1 manually


Reference
=========
https://www.tensorflow.org/tutorials/estimators/cnn#building_the_cnn_mnist_classifier