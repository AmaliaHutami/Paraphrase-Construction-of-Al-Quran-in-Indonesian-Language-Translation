import PPDB
from PPDB import *
from GlobalName import *

class classPFA:

    def tambahAlignPFA(self, alignResult, i, cekidentical):
        global sudahAlign
        sudahAlign.append([])
        tempTidakAda = []
        tempKata = []
        for l in range(len(cekidentical)):
            tempKata.append(cekidentical[l][0])
        for j in range(len(alignResult)):
            if alignResult[j][0] not in tempKata:
                tempTidakAda.append(alignResult[j])
        for k in range(len(tempTidakAda)):
            if tempTidakAda[k] not in sudahAlign[i]:
                temp = [tempTidakAda[k]]
                sudahAlign[i].extend(temp)
        return sudahAlign


    def alignWordSimilarity(self, kalimatDasar1, kalimatDasar2):
        global sudahAlign
        wordsSimilarity = []
        t = 1
        #fungsi random untuk menghitung batas bawah
        #kanan = []
        #kiri = []
        for i in range(len(kalimatDasar1)):
            for j in range(len(kalimatDasar2)):
                if kalimatDasar1[i].lower() and kalimatDasar2[j].lower() not in punctuations:
                    if PPDB.presentInPFA(kalimatDasar1[i], kalimatDasar2[j]) is True:
                        wordsSimilarity.append([j + 1, t])
                        #kanan.append(t)
                        #kiri.append(j + 1)
            t += 1
        #kanan.append(len(kalimatDasar1))
        #kiri.append(len(kalimatDasar2))

        res = []
        for m in range(len(wordsSimilarity)):
            if wordsSimilarity[m] not in res:
                res.append(wordsSimilarity[m])

        #allList = []
        #for v in wordsSimilarity:
            #allList = allList + v
        #k = 0
        #wordSim2 = []
        #while k < len(wordsSimilarity):
            #wordSim2.append([random.choice(kiri), random.choice(kanan)])
            #k += 1
        #return wordSim2
        return res



