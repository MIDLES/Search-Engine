import pandas as pd
import numpy as np
import re
from TME03.Query import Query

class QueryParser:
    
    def __init__(self,path_q,path_r):
        self.dict_q=dict()
        fichier_q=open(path_q,'r').read().replace('\n',' ')
        self.liste_q=re.split('\.I ',fichier_q)[1:]
        r_vector=np.array(pd.read_csv('data/cacm/cacm.rel' , delimiter=' '))[:,:2]
        r_vector=r_vector.astype(int)
        for i in range(len(self.liste_q)):
            q_split=re.split('\.W ',self.liste_q[i])
            
            if (' .T ' in q_split[0]):
                ident=re.split('\.T ',q_split[0])[0]
                list_id_doc=r_vector[np.where(r_vector[:,0]==int(ident))][:,1]
                self.dict_q[int(ident)]=Query(int(ident),re.split('\.[NABKX]',q_split[1])[0],list_id_doc)
            else:
                list_id_doc=r_vector[np.where(r_vector[:,0]==int(q_split[0]))][:,1]
                self.dict_q[int(q_split[0])]=Query(int(q_split[0]),re.split('\.[NABKX]',q_split[1])[0],list_id_doc)