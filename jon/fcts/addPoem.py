#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:46:43 2019

@author: Ning
"""
import pickle
import datetime

def addPoem(options):
    
    resultFile = options['resultNameBase']+'.pkl'
    resultCSV = options['resultNameBase']+'.csv'
    
    currTime = datetime.datetime.now()
    todayDate = currTime.strftime('%Y-%m-%d')
    
    with open(resultFile, 'rb') as f:
        record = pickle.load(f)
    
    nRec = len(record.index)
    newRec = {'iPoem':nRec+1,'Poem':options['newPoemName'],'nReviews':0,'lastDate':todayDate,'sinceLastDate':0}
    record = record.append(newRec, ignore_index=True)
    
    with open(resultFile, 'wb') as f:
        pickle.dump(record, f)
    record.to_csv(resultCSV, index = False)