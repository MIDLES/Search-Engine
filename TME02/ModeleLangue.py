import numpy as np
from TME01.TextRepresenter import PorterStemmer
from TME02.IRModel import IRModel
import math
import operator

class ModeleLangue(IRModel):
    
    def __init__(self,Index,l=0.8):
        super().__init__(Index)
        self.l=l
        self.normalizer=PorterStemmer()
        self.index_inverse_corpus={stem : sum(list(dic_doc.values()))for (stem,dic_doc) in Index.index_inverse.items() }
        
        
    def getScores(self,query):
        query_rep=self.normalizer.getTextRepresentation(query.texte)
        rsv_dic={doc:0 for doc in self.Index.index.keys()}
        for stem in query_rep.keys():
            if (stem in self.Index.index_inverse.keys()):
                beta=self.index_inverse_corpus[stem]/sum(list(self.index_inverse_corpus.values()))
                #beta=self.index_inverse_corpus[stem]/sum([self.index_inverse_corpus[stem2] for stem2 in query_rep.keys()])
                tf_stem=query_rep[stem]
                for id_doc,tf in self.Index.index_inverse[stem].items():
                #alpha=tf/sum([self.Index.index_inverse[stem2][id_doc] if id_doc in self.Index.index_inverse[stem2].keys() else 0  for stem2 in query_rep.keys()])
                    alpha=tf/sum(list(self.Index.index[id_doc].values()))
                    rsv_dic[id_doc]+= math.log(((1-self.l)*alpha )+ (self.l* beta))*tf_stem
        return rsv_dic       
        

    def getRanking(self,query):
        rangs=sorted(self.getScores(query).items(), key=operator.itemgetter(1),reverse=False)
        return rangs
    
    
    
    
    def train(self,ens_q,mesure,gridLambda):
        bestScore,bestLambda=0,0
        for l in gridLambda:
            ml=ModeleLangue(self.Index,l)
            Score=np.mean([mesure.evalQuery(ml.getRanking(q),q)for q in ens_q])
            if (Score>bestScore):
                bestScore=Score
                bestLambda=l
        self.l=bestLambda
        return {'bestTrainingScore ':round(bestScore,3),'Lambda':round(self.l,3)}
    
    
    
    
