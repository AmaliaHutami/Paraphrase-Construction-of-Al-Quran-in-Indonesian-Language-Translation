from GlobalName import *

def loadPFA(ppdbFileName = 'ppdb.txt'):
    global PFASim
    global PFADict
    count = 0
    PFAFile = open(ppdbFileName, 'r')
    for line in PFAFile:
        if line == '\n':
            continue
        tokens = line.split()
        tokens[1] = tokens[1].strip()
        PFADict[(tokens[0], tokens[1])] = PFASim
        count += 1

def presentInPFA(word1, word2):
    global PFADict
    if (word1.lower(), word2.lower()) in PFADict:
        return True
    if (word2.lower(), word1.lower()) in PFADict:
        return True

def wordSim(word1,word2):
    if presentInPFA(word1,word2):
       return PFASim
    else:
        return 0

