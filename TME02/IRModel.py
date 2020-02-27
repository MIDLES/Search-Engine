#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import operator
class IRModel:
    
    def __init__(self,Index):
        self.Index=Index
        
        
        
    def getScores(self,query):
        raise NotImplementedError
        
        
        
    def getRanking(self,query):
        raise NotImplementedError
        
        
        
       