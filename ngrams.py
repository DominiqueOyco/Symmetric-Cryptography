#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:37:26 2019

@author: Dominique Oyco (014605758)
         LAB ASSIGNMENT 1 SUPPLEMENTARY FILE - ngrams
"""

"""
Courtesy of http://practicalcryptography.com - however some parts were
modified to cooperate with the part 1 decryptor file

Allows scoring of text using n-gram probabilities
Needed for the part 1 decryptor to work
"""
from math import log10

#Courtesy of http://practicalcryptography.com
class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        """ load a file containing ngrams and counts, calculate log probabilities """
        self.ngrams = {}
        for line in open(ngramfile):
            key, count = line.split(sep)
            self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())
        #calculate log probabilities
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
        self.floor = log10(0.01 / self.N)

    def score(self, text):
        """ compute the score of text """
        score = 0
        ngrams = self.ngrams.__getitem__

        #MODIFICATIONS
        trueScore = 0  #score used for reference. It incremements in the for-loop
        
        for i in range(len(text) - self.L + 1):
            if text[i:i + self.L] in self.ngrams:
                score += ngrams(text[i:i + self.L])
            else:
                score += self.floor

            loopScore = ngrams('TION') #Get the ngram score of 'TION', which has the highest
            trueScore += loopScore  #Add the reference score for every loop
    
        return score / trueScore