#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from TME01.TextRepresenter import PorterStemmer
import math

class IndexerSimple:
    def __init__(self,collection):
        self.collection=collection
        self.normalizer=PorterStemmer()
        self.index=dict()
        self.index_inverse=dict()
        self.indexation()
        self.idf_dict=self.construire_idf_dict()
        
    
    
    def indexation(self):
        for key,val in self.collection.items():
            self.index[key]=self.normalizer.getTextRepresentation(val.texte)
        for key1,val1 in self.index.items():
            for key2,val2 in val1.items():
                if(key2 not in self.index_inverse.keys()):
                    self.index_inverse[key2]=dict()
                self.index_inverse[key2][key1]=val2
   

    def construire_idf_dict(self):
        df_dict=dict()
        idf_dict=dict()
        for id_doc in self.collection.keys():
            tf_dict=self.getTfsForDoc(id_doc)
            for key in tf_dict.keys():
                if key not in df_dict.keys():
                    df_dict[key]=1
                else:
                    df_dict[key]+=1
        for terme,dfreq in df_dict.items():
            idf_dict[terme]=math.log((1+len(self.collection.keys()))/(1+dfreq))
        return idf_dict


    def getTfsForDoc(self,id_doc):
        return self.index[id_doc]
    
    def getTfIDFsForDoc(self,id_doc):
        tf_idf_doc=dict()
        for stem,tf in self.getTfsForDoc(id_doc).items():
            tf_idf_doc[stem]=tf*self.idf_dict[stem]
        return tf_idf_doc
    
    def getTfsForStem(self,stem):
        return self.index_inverse[stem]
    
    def getTfIDFsForStem(self,stem):
        tf_idf_stem=dict()
        for doc,tf in self.getTfsForStem(stem).items():
            tf_idf_stem[doc]=tf*self.idf_dict[stem]
        return tf_idf_stem
    
    def getStrDoc(self,ident):
        return self.collection[ident].texte
    
    
    
    
    
        