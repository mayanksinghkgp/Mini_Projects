# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:42:22 2022
Wordel Solver
@author: Mayank 
"""
from nltk.corpus import words
#import pandas as pd

### PARAMETERS ###
word_list = words.words()
wordle_len = 5
not_repeat = 1 #1-> no repetition of alphabets; 0-> repetition allowed

### CHANGE THESE 3 LINES ###
corr = 'ed45' #'ane345' : Add the correct words here and location (green)
incorr = 'llli3512'  # 'arra1245': Add wrongly located words here (yellow)
exclude = 'tascrun' #Add the words to be excluded
###
exclist = list(set(list(exclude)))
inclist = list(set(list(incorr[:int((len(incorr)/2))])).union(list(corr[:int((len(corr)/2))])))

wordle_list = []
posslist = []

corr_alpha = []
corr_loc = []
corralpha_dict = {}
if len(corr)>0:
    corr_alpha = list(corr[:int((len(corr)/2))])
    corr_loc = list(corr[int(len(corr)/2):])
    
    for i,j in zip(corr_alpha,corr_loc):
        corralpha_dict[i] = int(j)
        
incorr_alpha = []
incorr_loc = []
incorralpha_dict = []
if len(incorr)>0:
    incorr_alpha = list(incorr[:int((len(incorr)/2))])
    incorr_loc = list(incorr[int(len(incorr)/2):])
    
    for i,j in zip(incorr_alpha,incorr_loc):
        incorralpha_dict.append([i,int(j)])

for i in word_list:
    if len(i) == wordle_len:
        wordle_list.append(i.lower())
        
def correct_alpha(word, alpha, loc):
    if word[loc-1] == alpha:
        return True
    
def incorrect_alpha(word, alpha, loc):
    if word[loc-1] == alpha:
        return True

def include_alpha(word, inclist):
    flag = True
    for i in inclist:
        if i not in word:
            flag = False
    return flag

def exclude_alpha(word, exclist):
    flag = True
    for i in exclist:
        if i in word:
            flag = False
    return flag

for i in wordle_list:
    c1 = True
    c2 = True
    c3 = True
    c4 = True
    c2 = include_alpha(i, inclist)
    c3 = exclude_alpha(i, exclist)
    for j in corralpha_dict:
        if not correct_alpha(i, j, corralpha_dict.get(j)):
            c1 = False
    for j in incorralpha_dict:
        if incorrect_alpha(i, j[0], j[1]):
            c4 = False
    if not_repeat == 1:
        c5 = len(set(list(i))) == wordle_len
    try:
        if c1 and c2 and c3 and c4 and c5:
            posslist.append(i)
    except:
        if c1 and c2 and c3 and c4:
            posslist.append(i)

print(posslist)