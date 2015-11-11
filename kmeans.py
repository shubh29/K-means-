# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 15:46:43 2015

@author: Shubham
Mahesh
Abhishek
"""

################################## Imports ####################################
import os, random
import nltk,re,sys
# Get stop words
stopwords = nltk.corpus.stopwords.words('english')

################################## Initialize##################################
# { <filename> : <list of terms (not unique)> }
documentTerms = {}

cluster = {}


try:
    # Read all .txt files in the current working directory
    for file in os.listdir(os.getcwd()):
         if file.endswith(".txt"):
              fOpen = open(file,'r')
              fRead = fOpen.read()
              # Get all tokens in the document
              documentTerms[file] = [w.lower() for w in nltk.word_tokenize(fRead) if w.lower() not in stopwords]
              print(documentTerms)
except:
     print('Something went wrong while reading the file')
     #quit python
     sys.exit(0)
################################## Methods ####################################

def distanceFromCentroid():
    
## centroid shoud not change

    
