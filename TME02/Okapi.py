import numpy as np
from TME01.TextRepresenter import PorterStemmer
import math
from TME02.IRModel import IRModel
from TME03.EvalMesure import Precision

import operator

class Okapi(IRModel):
    
    def __init__(self,Index,k1=1.2,b=0.75):
        super().__init__(Index)
        self.normalizer=PorterStemmer()
        self.taille_doc={doc : sum(list(dic_stem.values()))for (doc,dic_stem) in Index.index.items() }
        self.k1=k1
        self.b=b
        
        self.taille_avg=np.mean(list(self.taille_doc.values()))
        
        
        
    def getScores(self,query):
        query_rep=self.normalizer.getTextRepresentation(query.texte)
        rsv_dic={doc:0 for doc in self.Index.index.keys()}
        for stem in query_rep.keys():
            if (stem in self.Index.index_inverse.keys()):
                idf=self.Index.idf_dict[stem]
                for id_doc,tf in self.Index.index_inverse[stem].items():
                    rsv_dic[id_doc]+=idf * tf/(tf+self.k1*((1-self.b)+self.b*(self.taille_doc[id_doc])/self.taille_avg))
        return rsv_dic       
        

    def getRanking(self,query):
        rangs=sorted(self.getScores(query).items(), key=operator.itemgetter(1),reverse=True)
        return rangs
    
    def train(self,ens_q,mesure,gridK1,gridB):
        bestScore,bestk1,bestb=0,0,0
        for k1 in gridK1:
            for b in gridB:
                okapi=Okapi(self.Index,k1,b)
                Score=np.mean([mesure.evalQuery(okapi.getRanking(q),q)for q in ens_q])
                if (Score>bestScore):
                    bestScore=Score
                    bestk1=k1
                    bestb=b
        self.k1=bestk1
        self.b=bestb
        return {'bestTrainingScore':round(bestScore,3),'k1': round(bestk1,4), 'b':round(bestb,4)}
        

