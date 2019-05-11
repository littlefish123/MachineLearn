Predict Next Word 
=================
This program is very interesting. Firstly, feed in a paragraph of story into the training model.

The model is able to predict the next word after input the 3 words which had been identified in the story.


Model
=====

Recurrent Neural Network (RNN)

Long Short-Term Memory(LSTM) - Long term dependency to reference back to proceeding words.


https://towardsdatascience.com/lstm-by-example-using-tensorflow-feb0c1968537

The generation of LSTM products a 112-elemment vector of probabilities for prediction of next symbol normalized by softmax() function.
The index of the element with highest probability is the predicted index of symbol in the reverse dictionary.
(one-hot vector) 

Next Input activation = one-hot vector*weight(out) + biases(out)

After the model is trained, this program prompts to input 3 words and it'll automatically continue
to predict up to 32 predictions.


Parameters
==========
Layer=2 (each layer with 512 hidden units)

Learning Rate=0.001

Training Iteration=50000

Step=1000

Hidden Units=512

Loss Function
=============
Softmax CrossEntropy with LOGIT

Optimizer
=========
RMSProp 
Learning Rate=0.001



