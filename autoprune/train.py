# this is a script that trains a sample network
# we will calculate the average absolute value to see how active backprop is for each weight in the matrix
# I am interested in whether I can modify the backprop method so that I can reinitialize the less active weights.

import torch
from torch.autograd import Variable
from utee import selector
model_raw, ds_fetcher, is_imagenet = selector.select('mnist')
ds_val = ds_fetcher(batch_size=10, train=False, val=True)
for idx, (data, target) in enumerate(ds_val):
    data =  Variable(torch.FloatTensor(data)).cuda()
    output = model_raw(data)