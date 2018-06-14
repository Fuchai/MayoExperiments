# environment setup took me exceptionally long time. I will need to do domainadapt first.
import torch


if __name__ == "__main__":

    story_limit = 150
    epoch_batches_count = 64
    epochs_count = 1024
    lr = 1e-5
    pgd = PreGenData(param.bs)
    computer = Computer()
    optim = None
    starting_epoch = -1

    # if load model
    computer, optim, starting_epoch = load_model(computer)

    computer = computer.cuda()
    if optim is None:
        optimizer = torch.optim.Adam(computer.parameters(), lr=lr)
    else:
        print('use Adadelta optimizer with learning rate ', lr)
        optimizer = torch.optim.Adadelta(computer.parameters(), lr=lr)

    # starting with the epoch after the loaded one
    train(computer, optimizer, story_limit, batch_size, pgd, int(starting_epoch) + 1)
