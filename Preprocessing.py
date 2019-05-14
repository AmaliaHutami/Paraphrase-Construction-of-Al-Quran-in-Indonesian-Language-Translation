import os
from GlobalName import *
import nltk
from nltk.tokenize import word_tokenize
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

class PreProcessing:

    #Open Data Stopwords Bahasa Indonesia
    data_stopword = "D:\EKSTENSI S1\semester 3\TA\CD TA Galih Rizky Prabowo\Code Program Galih Rizky Prabowo\Program_1\Resources\stopword.txt"
    file = open(data_stopword)
    stopwords = file.read().splitlines()

    def tokenisasi(self, sentences):
        result = []
        result = word_tokenize(sentences)
        return result

    def stemming(self, sentences):
        result = []
        factory = StemmerFactory()
        for i in range(len(sentences)):
            result.append(stemmer.stem(sentences[i]))
        return result

    def cleanGoldAnno(self):
        global goldAnnotation
        goldAnno = []
        tempo = []
        result= []
        for i in range(len(goldAnnotation)):
            goldAnno.append([])
            for j in range(len(goldAnnotation[i])):
                cek = re.findall('[^p][0-9][0-9]|[^p0-9][0-9]',goldAnnotation[i][j]) #dengan P dihitung->[0-9][0-9]|[0-9] #[0-9][0-9]|[0-9]|p[0-9][0-9]|p[0-9] #tanpa P -> [^p][0-9][0-9]|[^p0-9][0-9]
                for k in range (len(cek)):
                     cek[k] = cek[k].strip()
                goldAnno[i].append(cek)
            result.append(goldAnno)

        return result

    def LowerCase(self, sentence):
        result = [x.lower() for x in sentence]
        return  result

    def hapusNull(self):
        for i in range(len(goldAnnotation)):
            del goldAnnotation[i][0]




