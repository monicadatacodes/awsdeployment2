#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:33:17 2022

@author: monicadata
"""

class readArticles:
    
    def __init__(self):      #executed whenever an object is created for this class = 
        
        self.dataPath = "/Users/monicadata/Desktop/Datascience/Awsdeployment2/aws/data/train/article1.txt"
        self.stopWordPath = "/Users/monicadata/Desktop/Datascience/Awsdeployment2/aws/data/stopWords.txt"
        self.specialCharPath = "/Users/monicadata/Desktop/Datascience/Awsdeployment2/aws/data/specialChar.txt"
    
   # def loadConfig():
        
    
    
    def loadArticleFromFile(self):   # read files present in the path and read the content and return
        with open(self.dataPath,'r') as fl:
            text = fl.read()
        return text    

    def loadStopWordFromFile(self):   # read files present in the path and read the content and return
        with open(self.stopWordPath,'r') as fs:
            text = fs.read()
        return text.split('\n')           

    def loadSpecialCharFromFile(self):   # read files present in the path and read the content and return
        with open(self.specialCharPath,'r') as fsc:
            text = fsc.read()
        return text.split('\n')  

    def loadArticleFromDB(self):   # read files present in the path and read the content and return
        pass    

    def loadArticleFromAPI(self):   # read files present in the path and read the content and return
        pass    

      

# readObject = readArticles()
# articleText =readObject.loadArticleFromFile() 
# print("This text is :\n\n{}".format(articleText))       

# stopWordText = readObject.loadStopWordFromFile()
# print ("\n Stop Words are\n {}".format(stopWordText))

# specialCharText = readObject.loadSpecialCharFromFile()
# print ("\n Special Char are\n {}".format(specialCharText))