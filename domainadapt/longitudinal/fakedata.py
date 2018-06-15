# This is a fake data generation file. Time series converted to fake longitudinal.
# What marks a longitudinal data is the signal sparsity by time.
# We will insert longitudinal data, but we do not expect the machine to make
# correct prediction on the sparsity location. Well. I think patient's visit
# timing is largely unpredictable. Also, to generate this dataset, it's convenient
# to insert blanks without rules.

# I think the easiest way to generate fake data is to modify the raw
# text file. Would it be doable?
# On the cost evaluation, those that are not targets will be plainly ignored, so I don't worry
# about the evaluation.

# the blanks can only be inserted between start of a question and the punctuation.
# i.e. the question or information.

import os
from os import listdir,mkdir
from os.path import join,isfile,basename,normpath,exists,abspath,isdir
from domainadapt.longitudinal.datagen import *
import random


def longitudinal_and_encode_data(files_list, lexicons_dictionary, padding_to_length=None, sparsity_prob=0.7):
    """
    add longitudinal sparsity to every line
    encodes the dataset into its numeric form given a constructed dictionary
    padding the vectors to the padding_to_length, by adding dummy symbols in the end

    Parameters:
    ----------
    files_list: list
        the list of files to scan through
    lexicons_dictionary: dict
        the mappings of unique lexicons

    Returns: tuple (dict, int)
        the data in its numeric form, maximum story length
    """

    files = {}
    story_inputs = None
    story_outputs = None
    stories_lengths = []
    answers_flag = False  # a flag to specify when to put data into outputs list
    limit = padding_to_length if not padding_to_length is None else float("inf")

    # add a end padding symbol
    plus_index=len(lexicons_dictionary)
    lexicons_dictionary["+"]=plus_index

    # lookup longitudinal padding symbol ampersand
    amper_index=lexicons_dictionary["&"]

    for indx, filename in enumerate(files_list):

        files[filename] = []

        with open(filename, 'r') as fobj:

            for line in fobj:
                # first seperate . and ? away from words into seperate lexicons
                line = line.replace('.', ' .')
                line = line.replace('?', ' ?')
                line = line.replace(',', ' ')

                answers_flag = False  # reset as answers end by end of line
                # Corpus refers to either question or statement
                # corpus_flag is true after the number and before the punctuations
                # when corpus_flag is true, we can add longitudinal sparsity
                corpus_flag= False

                for i, word in enumerate(line.split()):

                    if word == '1' and i == 0:
                        # beginning of a new story
                        if not story_inputs is None:
                            # if it's not the first story, then we have story_inputs ready to append
                            # end append and put it in the bigger list
                            story_len = len(story_inputs)
                            stories_lengths.append(story_len)
                            if story_len <= limit:
                                # if below limit, padding starts
                                # input is a symbol +
                                story_inputs += [plus_index] * (limit - story_len)

                                files[filename].append({
                                    'inputs': story_inputs,
                                    'outputs': story_outputs
                                })
                            else:
                                # if the story len is somehow too big, then we simply not use it
                                # too much work for prototyping to manipulate the file pointer
                                # or to store the stories blah blah. Not necessary
                                pass
                            # initiate new list for the next story
                        story_inputs = []
                        story_outputs = []

                    # all numbers from the input are ignored.
                    if word.isalpha() or word == '?' or word == '.':
                        if not answers_flag:
                            # what is happening here?
                            # why is story_output not appended when it's not an answer?
                            # TODO
                            story_inputs.append(lexicons_dictionary[word.lower()])
                        else:
                            story_inputs.append(lexicons_dictionary['-'])
                            story_outputs.append(lexicons_dictionary[word.lower()])

                        # set the answers_flags if a question mark is encountered
                        if not answers_flag:
                            answers_flag = (word == '?')

                    # manipulate corpus flag after reading a word but before adding sparsity
                    if i == 0:
                        corpus_flag=True

                    if word=="?":
                        corpus_flag=False

                    # by probability, insert sparsity
                    if corpus_flag==True and random.random()<sparsity_prob:
                        story_inputs.append(amper_index)

            # for the last line, there is no new "1" to trigger appending, so we append
            # manually
            story_len = len(story_inputs)
            stories_lengths.append(story_len)
            if story_len <= limit:
                # if below limit, padding starts
                # input is a symbol +
                story_inputs += [plus_index] * (limit - story_len)

                files[filename].append({
                    'inputs': story_inputs,
                    'outputs': story_outputs
                })
            else:
                # if the story len is somehow too big, then we simply not use it
                # too much work for prototyping to manipulate the file pointer
                # or to store the stories blah blah. Not necessary
                pass


    return files, stories_lengths

def write_babi_with_text_to_longitudinal(story_limit=300):
    # implicitly, I assume that the padding I ran will be 50% the total.
    # modified from write_bab_with_text from datagen.py

    task_dir = os.path.dirname(abspath(__file__))
    data_dir = join(task_dir, 'data')
    joint_train = True
    files_list = []

    if data_dir is None:
        raise ValueError("data_dir argument cannot be None")

    for entryname in listdir(data_dir):
        entry_path = join(data_dir, entryname)
        if isfile(entry_path):
            files_list.append(entry_path)

    lexicon_dictionary = create_dictionary(files_list)
    lexicon_count = len(lexicon_dictionary)

    # append used punctuation to dictionary
    lexicon_dictionary['?'] = lexicon_count
    lexicon_dictionary['.'] = lexicon_count + 1
    lexicon_dictionary['-'] = lexicon_count + 2
    # sparse padding symbol
    lexicon_dictionary['&'] = lexicon_count + 3

    # this is where the time series gets converted to longitudinal data
    encoded_files, stories_lengths = longitudinal_and_encode_data(files_list, lexicon_dictionary, story_limit)

    processed_data_dir = join(task_dir, 'data', basename(normpath(data_dir)))
    train_data_dir = join(processed_data_dir, 'train')
    test_data_dir = join(processed_data_dir, 'test')
    if exists(processed_data_dir) and isdir(processed_data_dir):
        rmtree(processed_data_dir)

    mkdir(processed_data_dir)
    mkdir(train_data_dir)
    mkdir(test_data_dir)

    pickle.dump(lexicon_dictionary, open(join(processed_data_dir, 'lexicon-dict.pkl'), 'wb'))

    joint_train_data = []

    for filename in encoded_files:
        if filename.endswith("test.txt"):
            pickle.dump(encoded_files[filename], open(join(test_data_dir, "test" + '.pkl'), 'wb'))
        elif filename.endswith("train.txt"):
            if not joint_train:
                pickle.dump(encoded_files[filename], open(join(train_data_dir, basename(filename) + '.pkl'), 'wb'))
            else:
                joint_train_data.extend(encoded_files[filename])

    if joint_train:
        pickle.dump(joint_train_data, open(join(train_data_dir, 'train.pkl'), 'wb'))

if __name__=="__main__":
    write_babi_with_text_to_longitudinal()
    pgd=PreGenData(param.bs)
    input_data, target_output, ignore_index = pgd.get_train()
    # at this stage, input_data should have dimension (bs, story_length, vocab_size)
    print("done")