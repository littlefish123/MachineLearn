Movie Comment Classification
============================
This example reads movie comment from a dataset. Define a 4 layer Neural Network to learn 
whether the movie comment is GOOD or BAD.


(1) The first layer is an Embedding layer. This layer takes the integer-encoded vocabulary 
and looks up the embedding vector for each word-index. These vectors are learned as the model trains. 
The vectors add a dimension to the output array. 
The resulting dimensions are: (batch, sequence, embedding).

(2) A GlobalAveragePooling1D layer returns a fixed-length output vector for each example by averaging over the sequence dimension. 
This allows the model to handle input of variable length, in the simplest way possible.

(3) This fixed-length output vector is piped through a fully-connected (Dense) layer with 16 hidden units.

(4) The last layer is densely connected with a single output node. 
Using the sigmoid activation function, this value is a float between 0 and 1, representing a probability, or confidence level.


LOSS Function
=============
This is a Binary classification problem to classify comment "GOOD" or "BAD" only.
and the model outputs a probability (a single-unit layer with a sigmoid activation), 
we'll use the binary_crossentropy loss function.

e.g. Another loss function choice :
mean_squared_error