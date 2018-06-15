# insert empty blanks in the series and deal the unevenness of longitudinal data.
# also helps me run through the kinks and know that DNC will work on our data set.

import DNC.babi_train.training.datagen as datagen
import DNC.archi.param as param
from DNC.babi_train.train import runmain

# datagen.write_babi_with_text()
# pgd=datagen.PreGenData(param.bs)
# input_data, target_output, ignore_index = pgd.get_train()
# print("done")

runmain()