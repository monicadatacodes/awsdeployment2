#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 23:03:42 2022

@author: monicadata
"""
import re
from readdata import readArticles


class preProcessorText():
    
    def __init__(self):
        self.stopWords = []
        self.specialChar = []
        readObject = readArticles()
        self.articleText = readObject.loadArticleFromFile()
        self.stopWordText = readObject.loadStopWordFromFile()
        self.specialChartext = readObject.loadSpecialCharFromFile()








    def sentTokenize(self,text):
        """
        Tokenize sentences from article

        Parameters
        ----------
        text : string.

        Returns
        -------
        a list of strings.

        """
        sentArray = text.split('.')
        
        return sentArray
    
    def wordTokenize(self,text):
        """
        Tokenize words in sentences

        Parameters
        ----------
        text : string.

        Returns
        -------
        wordslist.

        """
        return re.split(' |,|;|-',text)
    
    def removeStopWords(self,text):
        
        wordList = self.wordTokenize(text)
        filteredWordList = [word for word in wordList if word not in self.stopWords]
        sentence = ' '.join(filteredWordList)
        return sentence
    
    def removeSpecialChar(self,text):
        
       sentence = ' '.join([char for char in text if char not in self.specialChar])
       return sentence
   
    def convertToLoweCase(self,text):
        
        return text.lower()
    
    def preProcess(self):
        
        text = self.articleText
        sentences = self.sentTokenize(text)
        processedSentenceList = []
        for sentence in sentences:
            text = self.convertToLoweCase(sentence)
            text = self.removeSpecialChar(text)
            text = self.removeStopWords(text)
            processedSentenceList.append(text)
            
        return processedSentenceList    
    
processObject = preProcessorText()  
processedSentenceList = processObject.preProcess() 
print("\n List of processed sentences : \n\n {}".format(processedSentenceList))   