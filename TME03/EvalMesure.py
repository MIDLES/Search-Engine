import numpy as np
class EvalMesure:
         
    def evalQuery(self,liste,query):
        raise NotImplementedError
        
        
        
class Precision(EvalMesure):
    
    def __init__(self,k=10):
        self.k=k
    
    
    
    def evalQuery(self,liste,query):
        return np.mean([1 if liste[i][0] in query.list_id_doc else 0 for i in range(self.k)])
                       
                       
                       
class Rappel(EvalMesure):
    
    def __init__(self,k=10):
        self.k=k
    
    
    
    def evalQuery(self,liste,query):
        return np.sum([1 if liste[i][0] in query.list_id_doc else 0 for i in range(self.k)])/len(query.list_id_doc)
                       
                       
class Fmesure(EvalMesure):
    
    def __init__(self,k=10,beta=1):
        self.k=k
        self.beta=beta
    
    
    
    def evalQuery(self,liste,query):
        p=Precision(self.k)
        r=Rappel(self.k)
        P=p.evalQuery(liste,query)
        R=r.evalQuery(liste,query)
        return ((1+self.beta**2)*P*R)/((self.beta**2)*P+R) if (P!=0 and R!=0) else 0
                       
                       
                       
                       
                       
class AvgP(EvalMesure):
    
    def __init__(self,N=10):
        self.N=N
    
    
    
    def evalQuery(self,liste,query):
        S=0
        for k in range(1,self.N):
            if(liste[k][0] in query.list_id_doc):
                p=Precision(k)
                S+=p.evalQuery(liste,query)
        return S/len(query.list_id_doc)
                       
                       
                       
                       
                       
class ReciprocalRank(EvalMesure):
    
    
    
    def evalQuery(self,liste,query):
        l=list(map(lambda x: x[0],liste))
        return 1/np.min([l.index(id_doc)+1 for id_doc in query.list_id_doc])
                       
                       
                       
import math

class NDCG(EvalMesure):
    
    def __init__(self,k=10):
        self.k=k
        
        
    def calculDCG(self,rel_grad):
        dcg=rel_grad[0]
        for i in range(1,len(rel_grad)):
            dcg+= rel_grad[i]/math.log(i+1)
        return dcg
    
    
    def evalQuery(self,liste,query):
        l=list(map(lambda x: x[0],liste))
        rel_grad=[1 if doc in query.list_id_doc else 0 for doc in l[:self.k] ]
        i_rel_grad=[1 if i<len(query.list_id_doc) else 0 for i in range(len(l[:self.k]))]
        dcg=self.calculDCG(rel_grad)
        idcg=self.calculDCG(i_rel_grad)
        return dcg/idcg                       
                       