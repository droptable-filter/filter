#!/usr/bin/env python2

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.feature_selection import VarianceThreshold
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import sys

# we need function that determines if message passed in is SPAM
def isSpam(msg):

    #email_subject = msg['subject']
    #email_from = msg['from']

    messageText = ""
    #print ('From : ' + email_from + '\n')
    #print ('Subject : ' + email_subject + '\n')
    for part in msg.walk():
#        each part is a either non-multipart, or another multipart message
#        that contains further parts... Message is organized like a tree
       if part.get_content_type() == 'text/plain':
           messageText=part.get_payload() # prints the raw text
    print('\n')
    #print messageText
    wordList = messageText.split(" ")
    #wordList = removeBigWords(wordList)
    for i in wordList:
        print (i)
    return True

def removeBigWords(wordList):
    wordListLen = len(wordList)
    for i in range(0, wordListLen - 1):
        if len(wordList[i]) > 99:
           wordList.pop(i)
    return wordList
