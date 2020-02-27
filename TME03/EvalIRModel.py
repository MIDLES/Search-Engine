import numpy as np
from TME02.Weighter import Weighter1,Weighter2,Weighter3,Weighter4,Weighter5
from TME02.Vectoriel import Vectoriel
from TME02.ModeleLangue import ModeleLangue
from TME02.Okapi import Okapi
from TME03.EvalMesure import Precision, Rappel,Fmesure, AvgP,ReciprocalRank,NDCG
import scipy.stats as stat



class EvalIRModel:
    
    def __init__(self,ens_q,modeles):
        self.dict_modeles=modeles
        self.ens_q=ens_q
        
    def afficher(self,dico,mesure):
        for nom,stats in dico.items():
            print('Moyenne de ',mesure,' pour le modele ',nom,' = ',stats[0])
            print('Ecart type = ',stats[1])
            print('------------------------------------------------------------')
        
    def ComparePrecision(self,k=10):
        mesure=Precision(k)
        comp=dict()
        for nom,model in self.dict_modeles.items():
            e=[mesure.evalQuery(model.getRanking(q),q)for q in self.ens_q]
            comp[nom]=(round(np.mean(e),3),round(np.std(e),3))
            
            
        return comp
    
    def CompareRappel(self,k=10):
        mesure=Rappel(k)
        comp=dict()
        for nom,model in self.dict_modeles.items():
            e=[mesure.evalQuery(model.getRanking(q),q)for q in self.ens_q]
            comp[nom]=(round(np.mean(e),3),round(np.std(e),3))
        return comp
    
    
    def CompareFmesure(self,k=10,beta=1):
        mesure=Fmesure(k,beta)
        comp=dict()
        for nom,model in self.dict_modeles.items():
            e=[mesure.evalQuery(model.getRanking(q),q)for q in self.ens_q]
            comp[nom]=(round(np.mean(e),3),round(np.std(e),3))
        return comp
    
    
    def CompareAvgP(self,N=20):
        mesure=AvgP(N)
        comp=dict()
        for nom,model in self.dict_modeles.items():
            e=[mesure.evalQuery(model.getRanking(q),q)for q in self.ens_q]
            comp[nom]=(round(np.mean(e),3),round(np.std(e),3))
        return comp
    
    def CompareRR(self):
        mesure=ReciprocalRank()
        comp=dict()
        for nom,model in self.dict_modeles.items():
            e=[mesure.evalQuery(model.getRanking(q),q)for q in self.ens_q]
            comp[nom]=(round(np.mean(e),3),round(np.std(e),3))
        return comp
    
    def CompareNDCG(self,k=10):
        mesure=NDCG(k)
        comp=dict()
        for nom,model in self.dict_modeles.items():
            e=[mesure.evalQuery(model.getRanking(q),q)for q in self.ens_q]
            comp[nom]=(round(np.mean(e),3),round(np.std(e),3))
        return comp
    
    
    
    def TestDifference(self,model1,model2,mesure):
        X1=[round(mesure.evalQuery(model1.getRanking(q),q),3)for q in self.ens_q]
        X2=[round(mesure.evalQuery(model2.getRanking(q),q),3)for q in self.ens_q]
        return stat.ttest_rel(X1,X2)[1]
        
    
    
 
