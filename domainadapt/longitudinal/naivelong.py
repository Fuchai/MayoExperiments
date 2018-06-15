# insert empty blanks in the series and deal the unevenness of longitudinal data.
# also helps me run through the kinks and know that DNC will work on our data set.


from DNC.babi_train.train import runmain
from domainadapt.longitudinal.datagen import *
import DNC.archi.param as param

if __name__=="__main__":
    write_babi_with_text(story_limit=300)
    pgd=PreGenData(param.bs)
    input_data, target_output, ignore_index = pgd.get_train()
    print("done")
