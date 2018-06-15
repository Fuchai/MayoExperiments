# this is a script that trains a sample network
# we will calculate the average absolute value to see how active backprop is for each weight in the matrix
# I am interested in whether I can modify the backprop method so that I can reinitialize the less active weights.

from DNC.babi_train.train import runmain


runmain() 