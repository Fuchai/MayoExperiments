# insert empty blanks in the series and deal the unevenness of longitudinal data.
# also helps me run through the kinks and know that DNC will work on our data set.


from domainadapt.longitudinal.runtrain import *

if __name__=="__main__":
    # you should run fakedata.py __main__ method first to generate data.
    story_limit = 150
    epoch_batches_count = 64
    epochs_count = 1024
    lr = 1e-5
    pgd = PreGenData(param.bs)
    computer = Computer()
    optim = None
    starting_epoch = -1