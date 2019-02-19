# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:57:53 2019

@author: tanma
"""
from qabot_predict_answer import QABot
import os

DATA_DIR_PATH = 'gunthercox-corpus'
sequences = []

for file in os.listdir(DATA_DIR_PATH):
    filepath = os.path.join(DATA_DIR_PATH, file)
    if os.path.isfile(filepath):
        lines = open(filepath, 'rt', encoding='utf8').read().split('\n')
        prev_words = []
        for line in lines:
            if line.startswith('- - ') or line.startswith('  - '):
                line = line.replace('- - ', '')
                line = line.replace('  - ', '')
            
            sequences.append(line)
            

for i in sequences:
    print(i,'\n',QABot().reply(i).replace("<UNK>",""),'\n\n')
    
print(QABot().reply('Would you like some candy?').replace("UNK",""))