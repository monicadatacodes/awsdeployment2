#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 22:33:17 2022

@author: monicadata
"""

class ReadArticles:
    
    def __init__(self):      #executed whenever an object is created for this class = 
        
        self.dataPath = "/Users/monicadata/Desktop/Datascience/Awsdeployment2/aws/data/train/article1.txt"
        
    
   # def loadConfig():
        
    
    
    def loadArticleFromFile(self):   # read files present in the path and read the content and return
        with open(self.dataPath,'r') as fl:
            text = fl.read()
        return text    
      
    def loadArticleFromDB(self):   # read files present in the path and read the content and return
        pass    

    def loadArticleFromAPI(self):   # read files present in the path and read the content and return
        pass    

      

readObject = ReadArticles()
articleText =readObject.loadArticleFromFile() 
print("This text is :\n\n{}".format(articleText))       