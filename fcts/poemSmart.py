# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:08:01 2019

@author: Ning
"""

from recitePoem import recitePoem
from addPoem import addPoem

options = dict([])
# number of poems to recite
options['nPrevPoems'] = 2
# list of poems to review
options['fileName'] = '../data/poemlist.txt'
# name of result file, will export CSV file
options['resultNameBase'] = '../result/result' 

# recite poems
recitePoem(options)

# learn new poem
learnNew = input('Do you want to learn new poem today?[y/n]')
if learnNew[0] == 'y':
    newPoemName = input('Please type the name of the poem you are learning:')
    if len(newPoemName) == 0:
        print('No new poem added. Quit.')
    else:
        print('New poem name: '+newPoemName)
        options['newPoemName'] = newPoemName
        addPoem(options)
        print('New poem '+newPoemName+' added to your record.')
    
print('You are done for today. Good job!')
