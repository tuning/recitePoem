# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 12:49:54 2019

@author: Ning
"""
import numpy as np
import pandas as pd
import os.path
import datetime
import pickle

def recitePoem(options):
            
    resultFile = options['resultNameBase']+'.pkl'
    resultCSV = options['resultNameBase']+'.csv'
    
    currTime = datetime.datetime.now()
    todayDate = currTime.strftime('%Y-%m-%d')
    
    # load previous data
    if os.path.exists(resultFile):
        with open(resultFile, 'rb') as f:
            record = pickle.load(f)
    else:
        # create initial record file
        poemDict = readPoemList(options['fileName'])
        nPoem = len(poemDict)
        record = pd.DataFrame.from_dict(poemDict, orient = 'index', columns = ['Poem'])
        record['iPoem'] = record.index
        record['iPoem'] = pd.to_numeric(record['iPoem'])+1
        record['nReviews'] = pd.Series(np.zeros(nPoem), index=record.index)
        record['lastDate'] = pd.Series(todayDate, index=record.index)
        record['sinceLastDate'] = pd.Series(np.zeros(nPoem), index=record.index)
        record = record.sort_values('iPoem')
        cols = ['iPoem','Poem','nReviews','lastDate','sinceLastDate']
        record = record[cols]
    
    poemIdx = selectPoem(record, options)
    
    # update today's review
    for i in range(len(poemIdx)):
        record.iloc[poemIdx[i],record.columns.get_loc('nReviews')] += 1
        lastDate = record.iloc[poemIdx[i],record.columns.get_loc('lastDate')]
        record.iloc[poemIdx[i],record.columns.get_loc('sinceLastDate')] = daysBetween(todayDate, lastDate)
        record.iloc[poemIdx[i],record.columns.get_loc('lastDate')] = todayDate 
        
    # save to file
    with open(resultFile, 'wb') as f:
        pickle.dump(record, f)
    record.to_csv(resultCSV, index = False)

def selectPoem(record, options):
    nPoemRecite = options['nPrevPoems']
    if nPoemRecite > 6:
        print('Gee that is too much! Six titles recommended.')
        nPoemRecite = 6
    nPoem = len(record.index)
    nDays = (np.array(record.loc[:,'sinceLastDate']+1))**2
    nRevs = np.array(record.loc[:,'nReviews'])+1
    prob = nDays/nRevs
    prob = prob/sum(prob)
    probIdx = np.flip(np.argsort(prob))[:min(nPoemRecite,nPoem)]
    poemIdx = probIdx[np.random.permutation(len(probIdx))[:nPoemRecite]]
    
    print("Today's "+str(nPoemRecite)+" poem(s) to review:")
    for i in range(nPoemRecite):
        print('Poem: '+record.iloc[poemIdx[i],record.columns.get_loc('Poem')])
    return poemIdx

def daysBetween(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def readPoemList(filename):
    poemDict = dict([])
    contents = open(filename, encoding="utf8").read()
    poemlist = contents.split('\n')
    print('You are awesome! You can recite '+str(len(poemlist))+' poems now:')
    for i in range(len(poemlist)):
        poemDict[str(i)] = poemlist[i]
        print('Poem '+str(i+1)+': '+poemlist[i])
    return poemDict
