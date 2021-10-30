# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:08:01 2019

@author: Ning
"""

from recitePoem import recitePoem
from addPoem import addPoem

options = {}
# number of poems to recite
options['nPrevPoems'] = 2
# list of poems to review
options['fileName'] = '../data/poemlist.txt'
# name of result file, will export CSV file
options['resultNameBase'] = '../result/result' 
# whether to show diag info
options['verbosity'] = 0

# recite poems
recitePoem(options)

# learn new poem
while True:
    learnNew = input('Add new poem?[y/N]')
    if len(learnNew) == 0:
        print('No new poem added.')
        break
    elif learnNew[0] == 'y':
        newPoemName = input('Please type the name of the poem you are learning:')
        if len(newPoemName) == 0:
            print('No new poem added.')
            break
        else:
            print('New poem title: '+newPoemName)
            options['newPoemName'] = newPoemName
            addPoem(options)
            print('New poem '+newPoemName+' added to your record.')
    else:
        print('No new poem added.')
        break
print('You are done for today. Good job!')
