#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TME01.TextRepresenter import PorterStemmer

class Weighter:
    
    def __init__(self,Index):
        self.Index=Index
        self.normalizer=PorterStemmer()
        
        
    def getWeightsForDoc(self,idDoc):
        raise NotImplementedError
        
        
        
    def getWeightsForStem(self,stem):
        raise NotImplementedError
        
        
        
        
    def getWeightsForQuery(self,query):
        raise NotImplementedError

        
class Weighter1(Weighter):
    def __init__(self, Index):
        super().__init__(Index)
        
        
    def getWeightsForDoc(self,idDoc):
        return self.Index.getTfsForDoc(idDoc)
        
        
        
    def getWeightsForStem(self,stem):
        return self.Index.getTfsForStem(stem)
        
        
        
        
    def getWeightsForQuery(self,query):
        return {a : 1 for a in self.normalizer.getTextRepresentation(query).keys()}

    
class Weighter2(Weighter):
    def __init__(self, Index):
        super().__init__(Index)
        
        
    def getWeightsForDoc(self,idDoc):
        return self.Index.getTfsForDoc(idDoc)
        
        
        
    def getWeightsForStem(self,stem):
        return self.Index.getTfsForStem(stem)
        
        
        
        
    def getWeightsForQuery(self,query):
        return self.normalizer.getTextRepresentation(query)

class Weighter3(Weighter):
    def __init__(self, Index):
        super().__init__(Index)
        
        
    def getWeightsForDoc(self,idDoc):
        return self.Index.getTfsForDoc(idDoc)
        
        
        
    def getWeightsForStem(self,stem):
        return self.Index.getTfsForStem(stem)
    
    def getWeightsForQuery(self,query):
        return {stem : self.Index.idf_dict[stem] if stem  in self.Index.idf_dict else 0 for stem in self.normalizer.getTextRepresentation(query).keys()}

        
import math
class Weighter4(Weighter):
    def __init__(self, Index):
        super().__init__(Index)
        
        
    def getWeightsForDoc(self,idDoc):
        return {a: 1+ math.log(b) for (a,b) in self.Index.getTfsForDoc(idDoc).items()}
        
        
        
    def getWeightsForStem(self,stem):
        return {a: 1+ math.log(b) for (a,b) in self.Index.getTfsForStem(stem).items()}
        

       
        
        
    def getWeightsForQuery(self,query):
        return {stem : self.Index.idf_dict[stem] if stem  in self.Index.idf_dict else 0 for stem in self.normalizer.getTextRepresentation(query).keys()}
        
class Weighter5(Weighter):
    def __init__(self, Index):
        super().__init__(Index)
        
        
    def getWeightsForDoc(self,idDoc):
        return {stem: (1+ math.log(tf))*self.Index.idf_dict[stem] for (stem,tf) in self.Index.getTfsForDoc(idDoc).items()}
        
        
        
    def getWeightsForStem(self,stem):
        return {d: (1+ math.log(tf))*self.Index.idf_dict[stem] for (d,tf) in self.Index.getTfsForStem(stem).items()}
        
        
        
        
    def getWeightsForQuery(self,query):
        return {stem : (1+ math.log(tf))*self.Index.idf_dict[stem] if stem  in self.Index.idf_dict else 0  for (stem,tf) in self.normalizer.getTextRepresentation(query).items()}
        
        
        
