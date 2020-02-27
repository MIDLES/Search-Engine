#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import operator
import numpy as np
from TME02.IRModel import IRModel


class Vectoriel(IRModel):
    
    def __init__(self,Index,weighter,normalized):
        super().__init__(Index)
        self.weighter=weighter
        self.normalized=normalized
        self.index_inverse={stem : self.weighter.getWeightsForStem(stem) for stem in Index.index_inverse.keys()}
        self.list_id=Index.index.keys()
        self.normes_doc={doc : np.sqrt(np.sum(np.array(list(Index.index[doc].values()))**2)) for doc in self.list_id}
        
        
        
    def getScores(self,query):
        query_rep=self.weighter.getWeightsForQuery(query.texte)
        rsv_dic={doc:0 for doc in self.list_id}
        for stem in query_rep.keys():
            if (stem in self.index_inverse.keys()):
                for id_doc,weight in self.index_inverse[stem].items():
                    rsv_dic[id_doc]+=query_rep[stem]*weight
        if(self.normalized):
            X=np.sqrt(np.sum(np.array(list(query_rep.values()))**2))
            rsv_dic={doc: dot/(X+ self.normes_doc[doc]) for (doc,dot) in rsv_dic.items()}
        return rsv_dic
        
    def getRanking(self,query):
        rangs=sorted(self.getScores(query).items(), key=operator.itemgetter(1),reverse=True)
        return rangs
            