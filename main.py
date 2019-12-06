# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:34:37 2019

@author: saivalini
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

def department(column):
    return sorted(set(pd.Series(column)))


frequencystopwords = ["dear","pole no","no","pole","non","not","glowing","working","burning","complained","light",
                      "citizen","please","rectify","sir","madam","street"]

# Function to Generate Frequency
def frequency_generator(column):
    """
    Function to Genrate Word Frequencies from preprocess text from a DataFrame Column
    
    input: 
    column: Text Coloumn of Data Frame
    stopwords: Stop Words (Stanadard/Custom Defined)
    
    output: Returns Input Data Frame After Processing
    """
    corpus = column
    vec = CountVectorizer(ngram_range=(3, 3), stop_words=frequencystopwords).fit(corpus)
    bag_of_words = vec.transform(corpus) 
    #matrix where each row represents a specific text in corpus and each column 
    #represents a word in vocabulary, that is, all words found in corpus.
    sum_words = bag_of_words.sum(axis=0) 
    #sum_words is a vector that contains the sum of each word occurrence in all
    #texts in the corpus. In other words, we are adding the elements for each 
    #column of bag_of_words matrix.
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True) 
    ## sorts based on the value given to key, i.e., the word and their 
    #occurrence in the ascending order
    return words_freq

