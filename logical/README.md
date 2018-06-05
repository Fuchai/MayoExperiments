## logical

I want to constrain some weights in the model to be interpretable. For example, constrain the activation function
to be in range [0, 1], and downstream interactions to treat it as if it's a probability. Dense network should feed
forward this probability in the end and use it as part of the calculation in some CNF or even tree like conclusion
method, if I can ever find out what the derivative of a tree is, or even some heuristics.

This is an old idea. I have experimented with it but I failed. With ResNext, this might be easier to do now.