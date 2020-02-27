#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from TME01.Document import Document




class Parser:
    def __init__(self, path):
        self.dict_doc=dict()
        fichier=open(path,'r').read().replace('\n',' ')
        self.liste_doc=re.split('\.I ',fichier)[1:]
        for i in range(len(self.liste_doc)):
            doc_split=re.split('\.T',self.liste_doc[i])
            if (' .W ' in doc_split[1]):
                self.dict_doc[int(doc_split[0])]=Document(int(doc_split[0]),re.split('\.[NABKX]',re.split('\.W ',self.liste_doc[i])[1])[0])
            else:
                self.dict_doc[int(doc_split[0])]=Document(int(doc_split[0]),'')
    
   