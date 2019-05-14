from GlobalName import *
from Preprocessing import *
import random

class classWordSequence:

    def tambahAlign(self, alignResult, i):
        global sudahAlign
        sudahAlign.append([])
        for k in range(len(alignResult)):
            if alignResult[k] not in sudahAlign[i] :
                temp = [alignResult[k]]
                sudahAlign[i].extend(temp)
        return sudahAlign

    def isSublist(self, A, B):
        # returns True if A is a sublist of B, False otherwise
        sub = True

        for item in A:
            if item not in B:
                sub = False
                break
        return sub

    # ====================================================================#
    def findAllCommonContiguousSublists(self,A, B, turnToLowerCases=True):
        a = []
        b = []
        for item in A:
            a.append(item)
        for item in B:
            b.append(item)

        if turnToLowerCases:
            for i in range(len(a)):
                a[i] = a[i].lower()
            for i in range(len(b)):
                b[i] = b[i].lower()
        commonContiguousSublists = []
        swapped = False
        if len(a) > len(b):
            temp = a
            a = b
            b = temp
            swapped = True
        maxSize = len(a)
        for size in range(maxSize, 0, -1):
            startingIndicesForA = [item for item in range(0, len(a)-size+1)]
            startingIndicesForB = [item for item in range(0, len(b)-size+1)]
            for i in startingIndicesForA:
                for j in startingIndicesForB:
                    if a[i:i+size] == b[j:j+size]:
                        # check if a contiguous superset has already been inserted; don't insert this one in that case
                        alreadyInserted = False
                        currentAIndices = [item for item in range(i,i+size)]
                        currentBIndices = [item for item in range(j,j+size)]
                        for item in commonContiguousSublists:
                            if classWordSequence().isSublist(currentAIndices, item[0]) and classWordSequence().isSublist(currentBIndices, item[1]):
                                alreadyInserted = True
                                break
                        if not alreadyInserted:
                            commonContiguousSublists.append([currentAIndices, currentBIndices])

        if swapped:
            for item in commonContiguousSublists:
                temp = item[0]
                item[0] = item[1]
                item[1] = temp
        return commonContiguousSublists

    # ====================================================================#
    #align word sequences
    def alignSequences(self,kalimatDasar1,kalimatDasar2):
        alignments = []
        #fungsi random untuk menghitung batas bawah
        #rlist = []
        #llist = []
        sourceWordIndicesAlreadyAligned= []
        targetWordIndicesAlreadyAligned= []
    # align all (>=2)-gram matches with at least one content word
        commonContiguousSublists  = classWordSequence().findAllCommonContiguousSublists(kalimatDasar1, kalimatDasar2, True)
        for item in commonContiguousSublists:
                allStopWords = True
                for jtem in item:
                    if jtem not in PreProcessing.stopwords and jtem not in punctuations:
                        allStopWords = False
                        break
                if len(item[0]) >= 2 and not allStopWords:
                    for j in range(len(item[0])):
                        if item[0][j]+1 not in sourceWordIndicesAlreadyAligned and item[1][j]+1 not in targetWordIndicesAlreadyAligned and [item[0][j]+1, item[1][j]+1] not in alignments:
                            alignments.append([item[1][j]+1, item[0][j]+1])
                            sourceWordIndicesAlreadyAligned.append(item[0][j]+1)
                            targetWordIndicesAlreadyAligned.append(item[1][j]+1)
                            #rlist.append(item[0][j]+1)
                            #llist.append(item[1][j]+1)

        #rlist.append(len(sourceWordIndicesAlreadyAligned))
        #llist.append(len(targetWordIndicesAlreadyAligned))

        #semuaList = []
        #for b in alignments:
            #semuaList = semuaList + b
        #m = 0
        #alignments2 = []
        #while m < len(alignments):
            #alignments2.append([random.choice(llist), random.choice(rlist)])
            #m+= 1
        #return alignments2
        return alignments
    # ====================================================================#
