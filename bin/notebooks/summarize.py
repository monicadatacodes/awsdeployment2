#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:23:28 2022

@author: monicadata
"""

import numpy as np
from preProcessor import preProcessorText

class summarizeArticle():
    
    def __init__(self):
        preprocessObject = preProcessorText()
        self.sentArray = preprocessObject.preProcess()
    
    def groupSentences(self,sentArray):
        firstSentence = sentArray[0]
        restSentences = sentArray[1:]
        
        return firstSentence,restSentences
    
    def sortSentences(self,restSentences):
        
        sentLengths = [len(sent) for sent in restSentences]
        sortedIndex = np.argsort(sentLengths)
        sortedSentences = []
        
        for idx in sortedIndex:
            sortedSentences.append(restSentences[idx])
        
        return sortedSentences


    def combineSentences(self,firstSentence,sortedSentences):
         
         combinedSentences = [firstSentence] + sortedSentences[-5:0]
         summary = ' '.join(combinedSentences)
         return summary
        
            
    def summarize(self):
          
          firstSentence,restSentences = self.groupSentences(self.sentArray)
          sortedSentences2 = self.sortSentences(restSentences)
          summary = self.combineSentences(firstSentence,sortedSentences2)
          
          return summary
        
summaryObject = summarizeArticle()
summary = summaryObject.summarize()
print("\n Summary is : \n\n{}".format(summary))    