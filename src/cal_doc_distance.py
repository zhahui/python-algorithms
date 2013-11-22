'''
@author: Hui Zha
@created: 2013-11-20
@summary: This program calculates the "distance" between two text files.
    The "distance" is calculated as follows:
    1. Read each text file into memory as string(s)
    2. Split the string(s) of each file into a list of alphanumeric "words".
       Non-alphanumeric characters will be replaced by blanks and uppercase
       characters will be converted to lowercase.
    3. Count the frequency of each word, build a frequency dictionary for each
       file, i.e., X for file1 and Y for file2
    4. The distance is defined as follows:
       d(X, Y) = arccos(inner_product(X, Y) / |X|*|Y|)
       where X and Y are the word frequency dictionaries for file1 and file2,
       respectively, and
       where inner_product(X, Y) is defined as follows:
       inner_product(X, Y) = sum_for_all_words_in_X_and_Y(x_word_i * y_word_i),
       and where |X| is defined as follows:
       |X| = sqrt(inner_product(X, X))
    References: http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/
'''
from __future__ import division
from math import sqrt, acos
from string import maketrans, punctuation, uppercase, lowercase
import sys
import cProfile


# translation table copied from MIT course 6.006 code docdist[1-8].py
translation_table = maketrans(punctuation + uppercase,
                              " "*len(punctuation) + lowercase)


def read_and_split_doc_and_build_freq_dict(doc_name):
    """
    Read the text file, split it and build the frequency dict.
    """
    word_freq_dict = {}
    with open(doc_name, 'r') as f:
        all_words = f.read()
    all_words = all_words.translate(translation_table)
    all_words_list = all_words.split()
    for word in all_words_list:
        if word not in word_freq_dict:
            word_freq_dict[word] = 1
        else:
            word_freq_dict[word] += 1
    return word_freq_dict


def cal_distance(freq_dict1, freq_dict2):
    """
    Calculate the distance with the frequency dicts.
    """
    product = 0
    sum1 = 0
    sum2 = 0

    for word in freq_dict1:
        sum1 += freq_dict1[word] * freq_dict1[word]
        if word in freq_dict2:
            product += freq_dict1[word] * freq_dict2[word]
    for word in freq_dict2:
        sum2 += freq_dict2[word] * freq_dict2[word]
    return acos(product / sqrt(sum1 * sum2))


def run_cal_distance():
    doc1 = sys.argv[1]
    doc2 = sys.argv[2]

    freq_dict1 = read_and_split_doc_and_build_freq_dict(doc1)
    freq_dict2 = read_and_split_doc_and_build_freq_dict(doc2)

    distance = cal_distance(freq_dict1, freq_dict2)
    print "The distance is: %f" % distance

if __name__ == '__main__':
    cProfile.run("run_cal_distance()")
