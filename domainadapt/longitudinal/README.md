If people can use CNN on natural language data, then I can port any model on natural language data.
There have been many advances in the field of machine vision, and NLP is lagging way behind.

I would like to try and adapt a few models on EHR similar data. High-dimensional labels. Highly relational/logical.
Contains natural language paragraphs like doctor's script.

## DNC

To use DNC or MAC, we need to

#### Adapt longitudinal data
We are no longer dealing with time series, since the signals are very sparse.

* I am going to turn a time series to be longitudinal, insert
arbitrary blanks that do not contain any information.

* At the moment, all the inputs will have te same input lenghts. Insertion
of longitudinal blanks will need to be arbitrary in the end, but right now,
I will insert a fixed number of blanks at sampled locations.

#### Deal with multi-faceted data
We are no longer dealing with a single data type. This is a mix of many different types of data. Somehow everything
needs to be projected onto the same dimension and be considered together.

#### Implement sliding window
Sliding window is a great data augmentation and the only natural way to interpret each EHR sequence.

## C-LSTM and attention

Most likely we will need to adapt LSTM to the EHR domain. EHR spans a very long period of time, and attention can be
a solution. EHR is longitudinal, and C-LSTM can be a solution.

## Dense and residual

I have never seen any application of dense net or residual network on the natural language processing domain. This
is very interesting. We can easily change the model to make it so.

## Reinforcement learning

If we understand medication as actions and illness as states, we can turn EHR as a record
of game being playbed by doctors. If we extract basic health information out of the EHR,
we will have our own reward function. EHR is performed by medical professionals, and we
can therefore make it a guided policy search.

The real-world application of this artificial intelligence doctor is not to be overestimated.
Most of the prescription should come from medical professionals. But there will be machine
doctors one day for sure. Otherwise this model can be used for other purposes, such as
discovering outliner treatments, or whatever.

## Generative adversarial network

GAN can be very limited for EHR domain. But after all, we are trying to predict the
next EHR, to some degree. If we train a GAN, the generative model might be useful for
prediction of patient's health records in the future. We let the GAN observe some history,
then the generative model produce some future projection, we sample it and get some
statistics out of it, compare it with actual data.

## MCTS?

Not likely. But there is possibility where it can be combined with reinforcement learning
prescriptions. Natural language with MCTS? It's a bit beyond my league.