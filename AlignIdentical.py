import random
from GlobalName import *


class classIdentical:

    def tambahAlign(self, alignResult, i):
        global sudahAlign
        sudahAlign.append([])
        for k in range(len(alignResult)):
            if alignResult[k] not in sudahAlign[i] :
                temp = [alignResult[k]]
                sudahAlign[i].extend(temp)
        return sudahAlign

    def alignIdenticalWords(self, kalimatDasar1, kalimatDasar2):
        identicalWords = []
        global sudahAlign
        t = 1
        #fungsi random untuk menghitung batas bawah
        #kanan = []
        #kiri = []
        for i in range(len(kalimatDasar1)):
            for j in range(len(kalimatDasar2)):
                if kalimatDasar1[i].lower() and kalimatDasar2[j].lower() not in punctuations:
                    if kalimatDasar1[i].lower() == kalimatDasar2[j].lower() and kalimatDasar2[j] not in punctuations:
                        identicalWords.append([j+1,t])
                        #kanan.append(t)
                        #kiri.append(j+1)
            t = t + 1

        #kanan.append(len(kalimat_pertama))
        #kiri.append(len(kalimat_kedua))

        #align tanda baca di akhir kalimat
        identicalWords.append([len(kalimatDasar2),len(kalimatDasar1)])
        #allList = []
        #for z in identicalWords:
            #allList = allList + z
        #k = 0
        #identicalWords2 = []
        #while k < len(identicalWords):
            #identicalWords2.append([random.choice(kiri),random.choice(kanan)])
            #k+=1
        #return identicalWords2
        return identicalWords

