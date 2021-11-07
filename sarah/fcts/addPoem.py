#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 10:46:43 2019

@author: Ning
"""
import pandas as pd
import datetime

def addPoem(options):
    
    resultCSV = options['resultNameBase']+'.csv'
    
    currTime = datetime.datetime.now()
    todayDate = currTime.strftime('%Y-%m-%d')
    
    record = pd.read_csv(resultCSV)
    nRec = len(record.index)
    newRec = {'iPoem':nRec+1,'Poem':options['newPoemName'],'nReviews':0,'lastDate':todayDate,'sinceLastDate':0}
    record = record.append(newRec, ignore_index=True)
    
    record.to_csv(resultCSV, index = False)