## two stage training

I experimented with some logical applications that turned out to be very difficult to learn. For example, I try to
constrict the form of the network to be a logical proposition (Target is iff A and B). The loss does not flow back,
maybe because logical operators are not end-to-end differentiable.

Is it possible to pre-train a model, freeze it, then train the other part? This is an idea similar to the ER algorithm.
Would this solve the logical training problem?
I would like to examine this idea with some logical datasets, such as ShapeSet by Yoshua Bengio.