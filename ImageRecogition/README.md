Image Recognition
=================
This is most simple basic classification program by using Sequential Model to recognize the fashion name according to given images.

Model 
=====
Sequential Model

1. Flatten 2d (28x28 pixals images) into 1-D Array of 28*28 = 784 pixals.

2. 1st Layer

128 Neurons 

Activation Method=RELU

3. 2nd Layer

10 Neurons

Activation Method=softmax

"softmax" is typically used to classify the result in an array of 10 probability scores to sum to 1.
Each score indicates the probability that the current image belongs to one of the 10 classes.


Loss Function
=============
Spare Categorial Crossentropy

Optimizer
=========
Adam

Metrics
=======
Accuracy