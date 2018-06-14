# this is a script that trains a sample network
# we will calculate the average absolute value to see how active backprop is for each weight in the matrix
# I am interested in whether I can modify the backprop method so that I can reinitialize the less active weights.

# from autoprune import pathsetup
import cv2
import torch
from torch.autograd import Variable
import sys
import DNC

for i, j in enumerate(sys.path):
    print(i, j)

from pretrained.utee import selector
