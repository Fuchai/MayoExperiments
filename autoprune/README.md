I would like to experiment with a new form of regularization that reinitializes the modules/paths/weights that do not
matter.

## reinitialize weights

I have made the assumption that not all weights play central role in a neural network. It's possible that some have
activations permanents stuck at low values. It's possible that some weights receive very low gradients due to
vanishing gradient problem, if the weights it interact with are of low weights too.

I would like to reinitialize the weights that do not have a strong influence on the final value. "Influence" is measured
by the activity of backprop gradients. If the average absolute value of gradient backprop to a particular weight is
high, then the weight is deemed of high influence.

I want to see if 1) there are indeed some weights that are of low influence. 2) whether I can reinitialize those
low influence wights during training, as a form of regularization or a way to get out of local minimum.

This model comes from the idea of forgetting something that a machine has learnt. Besides the benefits I have
mentioned, it's likely that a higher-order forgetting method can help prune the network and eliminate unnecessary
branches, and help reduce the size of the network and help it grow deeper.

I am not convinced that reinitialize the weights would be useful. It might destroy learning. The weights that are of
high influence may depend on the low-influence ones.

## pruning branches

In some architectures such as ResNext, the model is divided into different pathways are are highly modular.

I would like to devise a scheme to examine the importance module by module. I would like to train them by shuffling
and obscuring some, eliminating some, reinitializing some. See if this improves training.